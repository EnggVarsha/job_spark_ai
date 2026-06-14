import google.generativeai as genai
from config.settings import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

print("Testing Gemini Connection...")
print()

for model in genai.list_models():
    print(model.name)