from app.services.db_logger import save_conversation, get_recent_conversations
from aiogram import types
from aiogram import Dispatcher
from app.services.gemini_ai_service import get_gemini_response


async def handle_user_message(message: types.Message):
    user_id = message.from_user.id
    user_msg = message.text

    # 🧠 Get recent chats
    history = get_recent_conversations(user_id)

    # 🧾 Create history string
    past_convo = ""
    for chat in history:
        past_convo += f"User: {chat.user_msg}\nBot: {chat.ai_msg}\n"

    # 📤 Combine history + new message
    full_prompt = f"""You are a helpful assistant for Anurag's AI company.

Previous conversation:
{past_convo}

Now user says: {user_msg}
Reply smartly based on context."""

    # 💬 AI reply
    ai_reply = get_gemini_response(full_prompt)

    # ✍️ Save to DB
    save_conversation(user_id, user_msg, ai_reply)

    # 🚀 Reply to user
    await message.reply(ai_reply)


# ✅ Register function for main.py import
def register_ai_chat_handler(dp: Dispatcher):
    dp.register_message_handler(handle_user_message)