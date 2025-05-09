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
You are Anurag's professional AI assistant.

You can talk to users about *anything* they ask — whether it's casual, technical, or business-related.

🏢 But also, here is some important company context you should **remember and use when it's relevant**:

{company_context}

When replying:
- Be clear, concise, and helpful.
- If the question is about the company, use the context above.
- If it's unrelated (like tech, fun, or facts), just be helpful normally.
- Keep your tone friendly and professional.

User message:
{user_input}
"""

        response = chat.send_message(prompt)
        return response.text

    except Exception as e:
        return f"❌ Error: {e}"