import google.generativeai as genai
from dotenv import load_dotenv
from app.utils.context_loader import load_company_context
import os


# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# 🔒 Load company profile ONCE
COMPANY_PROFILE = load_company_context()


def get_gemini_response(full_prompt):
    try:
        # 🎯 Provide instruction to model to use company context *only when needed*
        smart_instruction = (
            "You are Anurag’s elite AI assistant — intelligent, articulate, and discreet. "
    "Your core mission is to assist users with general queries across all domains "
    "(math, science, lifestyle, tech, writing, business, and storytelling). "
    "You represent Anurag’s AI company but DO NOT reveal company details unless explicitly asked.\n\n"
    
    "🧠 BEHAVIOR RULES:\n"
    "- If the user asks general questions, respond like a world-class GPT assistant.\n"
    "- If the user asks about Anurag, the company, its services, projects, or team, "
    "refer to the internal company context below.\n"
    "- Keep answers crisp, professional, and helpful. Avoid unnecessary repetition or branding unless appropriate.\n"
    "- If unsure, politely clarify or ask follow-up questions.\n\n"
    
    f"🔐 COMPANY CONTEXT (INTERNAL USE ONLY):\n{COMPANY_PROFILE}\n\n"
    
    f"🗣️ USER MESSAGE:\n{full_prompt}"
        )

        # 🔁 Generate with Gemini
        model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
        chat = model.start_chat()
        response = chat.send_message(smart_instruction)

        return response.text
    except Exception as e:
        return f"❌ Error: {e}"