import google.generativeai as genai
from dotenv import load_dotenv
from app.utils.context_loader import load_company_context
import os

# Load environment variables
load_dotenv()
# 🔐 Tokens
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Step 1: Configure API key
genai.configure(api_key=GEMINI_API_KEY)  # 🔁 Replace with your actual Gemini API key

# Step 2: Gemini response function
def get_gemini_response(user_input):
    try:
        company_context = load_company_context()
        model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

        # Start persistent chat session (memory-aware)
        chat = model.start_chat()

        # Combine user input + your company context
        prompt = f"""
You are an AI assistant who works for Anurag's AI Solutions.

Here is important company context you must always remember:
{company_context}

Now respond helpfully to this user query, using context **if relevant**:
{user_input}
"""

        response = chat.send_message(prompt)
        return response.text

    except Exception as e:
        return f"❌ Error: {e}"