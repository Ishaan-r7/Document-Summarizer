# Real-Time Document Summarization Pipeline

A production-style document summarization system that uses Apache Kafka for 
real-time streaming, LangChain and Google Gemini API for intelligent summarization, 
and Streamlit for an interactive user interface.

## Architecture
```
PDF Upload (Streamlit)
      ↓
Producer → Kafka Topic (pdf-chunks)
      ↓
Consumer → LangChain + Gemini API
      ↓
Summary → Streamlit UI
```

## Tech Stack

- **Apache Kafka** — asynchronous message streaming
- **LangChain** — text chunking and summarization chains
- **Google Gemini API** — LLM for summarization
- **Streamlit** — user interface
- **PyPDF2** — PDF text extraction
- **Docker** — local Kafka infrastructure

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/document-summarizer.git
cd document-summarizer
```

### 2. Install dependencies
```bash
pip3 install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file in the root folder:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```
Get your free Gemini API key at [aistudio.google.com](https://aistudio.google.com)

### 4. Start Kafka with Docker
```bash
docker-compose up -d
```

### 5. Run the app
```bash
streamlit run app.py
```

## Project Structure
```
document-summarizer/
├── docker-compose.yml       
├── requirements.txt         
├── README.md                
├── producer.py              
├── consumer.py              
├── app.py                   
├── utils/
│   ├── pdf_extractor.py     
│   └── chunker.py           
└── config/
    └── settings.py          
```

## Key Features

- Asynchronous PDF processing via Kafka message queue
- Intelligent text chunking using LangChain's RecursiveCharacterTextSplitter
- Map-reduce summarization for handling large multi-page documents
- Clean Streamlit UI with real-time processing feedback
```

---

That's all the files done. Your folder should now look like this:
```
document-summarizer/
├── .env
├── .gitignore
├── docker-compose.yml
├── requirements.txt
├── README.md
├── producer.py
├── consumer.py
├── app.py
├── utils/
│   ├── __init__.py
│   ├── pdf_extractor.py
│   └── chunker.py
└── config/
    ├── __init__.py
    └── settings.py
Now whe