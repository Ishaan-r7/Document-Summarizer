from kafka import KafkaProducer
from utils.pdf_extractor import extract_text_from_pdf
from utils.chunker import chunk_text
from config.settings import KAFKA_BOOTSTRAP_SERVERS, KAFKA_TOPIC
import json

def send_to_kafka(file_bytes):
    """
    Extracts text from PDF, chunks it, and sends each chunk to Kafka topic.
    """
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    # Extract text from PDF
    text = extract_text_from_pdf(file_bytes)
    if not text:
        print("No text extracted from PDF")
        return False

    # Chunk the text
    chunks = chunk_text(text)
    print(f"Sending {len(chunks)} chunks to Kafka...")

    # Send each chunk to Kafka
    for i, chunk in enumerate(chunks):
        producer.send(KAFKA_TOPIC, value={
            "chunk_id": i,
            "total_chunks": len(chunks),
            "content": chunk
        })

    producer.flush()
    print("All chunks sent to Kafka successfully")
    return True