from kafka import KafkaConsumer
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from config.settings import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC, GOOGLE_API_KEY
import json

def get_summary():
    """
    Listens to Kafka topic, collects all chunks, and summarizes using Gemini.
    """
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='earliest',
        consumer_timeout_ms=10000
    )

    # Collect all chunks
    chunks = {}
    total_chunks = None

    for message in consumer:
        data = message.value
        chunk_id = data['chunk_id']
        total_chunks = data['total_chunks']
        chunks[chunk_id] = data['content']
        print(f"Received chunk {chunk_id + 1} of {total_chunks}")

        if total_chunks and len(chunks) == total_chunks:
            break

    consumer.close()

    if not chunks:
        return "No content received from Kafka"

    # Reconstruct ordered text as LangChain Documents
    ordered_chunks = [chunks[i] for i in sorted(chunks.keys())]
    docs = [Document(page_content=chunk) for chunk in ordered_chunks]

    # Summarize using Gemini via LangChain
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=GOOGLE_API_KEY
    )

    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.run(docs)

    return summary