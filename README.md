# Real-Time Document Summarization Pipeline

<img width="526" height="628" alt="image" src="https://github.com/user-attachments/assets/db6e8c1c-839e-490a-b5eb-87d1bf193c3a" />


A production-style document summarization system that uses Apache Kafka for 
real-time streaming, LangChain and Google Gemini API for intelligent summarization, 
and Streamlit for an interactive user interface.


## Architecture
<img width="731" height="471" alt="image" src="https://github.com/user-attachments/assets/96c30838-6973-4444-92ff-f5dfb00315c0" />

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
