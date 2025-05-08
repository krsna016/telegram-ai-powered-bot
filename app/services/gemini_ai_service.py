import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
# 🔐 Tokens
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Step 1: Configure API key
genai.configure(api_key=GEMINI_API_KEY)  # 🔁 Replace with your actual Gemini API key

# Step 2: Gemini response function
def get_gemini_response(user_input: str) -> str:
    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"❌ Error generating response: {e}"