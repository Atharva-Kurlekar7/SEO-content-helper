import os
from dotenv import load_dotenv

def load_config():
    """Load configuration from environment variables."""
    load_dotenv()
    
    return {
        'YOUTUBE_API_KEY': os.getenv('YOUTUBE_API_KEY'),
        'GEMINI_API_KEY': os.getenv('GEMINI_API_KEY'),  # Changed from OPENAI_API_KEY
        'DEBUG': os.getenv('DEBUG', 'True').lower() == 'true'
    }