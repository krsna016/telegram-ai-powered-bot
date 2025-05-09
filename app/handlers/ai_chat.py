from app.services.db_logger import save_conversation, get_recent_conversations
from aiogram import types
from aiogram import Dispatcher
from app.services.gemini_ai_service import get_gemini_response

# 🧠 Refined behavior template
def build_prompt(user_msg, past_convo):
    return f"""
You are Astra — Anurag’s elite AI assistant: articulate, creative, and deeply helpful.
Your job is to reply like a world-class mentor — using clarity, examples, structure, and light storytelling.

📘 PAST CONVERSATION:
{past_convo}

🗣️ NEW USER MESSAGE:
{user_msg}

✅ INSTRUCTIONS:
- Avoid using asterisks (*, **) or markdown-style formatting unless explicitly asked.(IMPORTANT)
- 🔹, 📌, ✨, 📘, 💡, ✅ for headers or highlights
- NO *, **, _, or __ for emphasis
- Clear line spacing and paragraphing, like a human-written note
- Use emojis 🔹📌✨ to create friendly, visual bullet points.
- Keep language friendly and inspiring, not robotic.
- Use line breaks to improve readability, like a human messaging in chat.
- Reply with high emotional and intellectual clarity.
- Use analogies, breakdowns, and examples when helpful.
- Default: concise answers in 3–4 lines with clear structure and value.\n
- Avoid repeating user’s question. Dive into the explanation if asked.
- Use emojis like ✅📘💡 where appropriate.
- Keep tone professional, engaging, and sharp.
- End with a short takeaway if possible.
- Speak like a helpful friend 🧠✨ — use emojis often to make replies lively.\n"
- Sound warm, clear, and confident. No robotic tone, no over-selling.\n"
- Use short bullets, analogies, and fun expressions when helpful.\n\n"

Reply in the above format and follow all rules strictly.

🎯 NOW REPLY:
"""

# 💬 Handler function
async def handle_user_message(message: types.Message):
    user_id = message.from_user.id
    user_msg = message.text

    # 🧠 Fetch last conversations
    history = get_recent_conversations(user_id)

    # 🧾 Format conversation string
    past_convo = ""
    for chat in history:
        past_convo += f"User: {chat.user_msg}\nBot: {chat.ai_msg}\n"

    # 🧠 Build smart prompt
    full_prompt = build_prompt(user_msg, past_convo)

    # 💡 Get AI reply
    ai_reply = get_gemini_response(full_prompt)

    # ✍️ Store the interaction
    save_conversation(user_id, user_msg, ai_reply)

    # 🚀 Send it to the user
    await message.reply(ai_reply)

# ✅ Register for router
def register_ai_chat_handler(dp: Dispatcher):
    dp.register_message_handler(handle_user_message)