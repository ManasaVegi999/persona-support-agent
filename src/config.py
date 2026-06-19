import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
