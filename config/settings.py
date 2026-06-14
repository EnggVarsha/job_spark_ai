from dotenv import load_dotenv
import os

load_dotenv()

# Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Rapid API
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

# Theme Colors
PRIMARY_COLOR = "#6C63FF"
SECONDARY_COLOR = "#4ECDC4"
BACKGROUND_COLOR = "#0F172A"
CARD_COLOR = "#1E293B"
TEXT_COLOR = "#FFFFFF"