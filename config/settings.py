import os
from dotenv import load_dotenv, find_dotenv

# --------------------------------------------------
# Load .env file
# --------------------------------------------------

dotenv_path = find_dotenv()

if dotenv_path:
    print(f"✅ .env file found at: {dotenv_path}")
    load_dotenv(dotenv_path)
else:
    print("❌ .env file not found!")

# --------------------------------------------------
# API Keys
# --------------------------------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

# --------------------------------------------------
# Debug (Remove after testing)
# --------------------------------------------------

print("Current Working Directory:", os.getcwd())

if GROQ_API_KEY:
    print("✅ GROQ API Loaded")
else:
    print("❌ GROQ API NOT Loaded")

if PEXELS_API_KEY:
    print("✅ PEXELS API Loaded")
else:
    print("❌ PEXELS API NOT Loaded")

# --------------------------------------------------
# AI Model
# --------------------------------------------------

MODEL_NAME = "llama-3.3-70b-versatile"

# --------------------------------------------------
# App Settings
# --------------------------------------------------

APP_NAME = "AI PPT Generator"

DEFAULT_SLIDES = 10

DEFAULT_THEME = "Blue"

DEFAULT_STYLE = "Professional"

DEFAULT_LANGUAGE = "English"

DEFAULT_FONT = "Calibri"

DEFAULT_FONT_SIZE = 24

DEFAULT_CREATIVITY = 0.7

OUTPUT_FOLDER = "output"