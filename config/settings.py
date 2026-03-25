import os
from dotenv import load_dotenv

load_dotenv()

# Kafka
KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'
KAFKA_TOPIC = 'pdf-chunks'

# Gemini
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# LangChain chunking
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100
```

Also create a `.env` file in the root folder:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```

This is where you'll paste your actual Gemini API key from aistudio.google.com. The `.env` file keeps your key out of your code so you don't accidentally expose it on GitHub.

**Important** — also create a `.gitignore` file and add this so the key never gets uploaded:
```
.env
__pycache__/
*.pyc