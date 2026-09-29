import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Current model
MODEL_NAME = os.getenv(
    "GROQ_MODEL",
    "openai/gpt-oss-120b"
)

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing. Please configure it in your .env file."
    )

print("CONFIG LOADED")
print("ACTIVE MODEL:", MODEL_NAME)