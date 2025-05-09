from aiogram import types, Dispatcher
from app.services.gemini_ai_service import get_gemini_response
from app.services.db_logger import save_conversation  # Update this line

async def handle_user_message(message: types.Message):
    user_id = message.from_user.id
    user_msg = message.text

    # 🧠 Get AI response
    ai_reply = get_gemini_response(user_msg)

    # ✍️ Save conversation to DB
    save_conversation(user_id, user_msg, ai_reply)  # Use save_conversation here

    # 💬 Send AI reply
    await message.reply(ai_reply)

def register_ai_chat_handler(dp: Dispatcher):
    dp.register_message_handler(handle_user_message)