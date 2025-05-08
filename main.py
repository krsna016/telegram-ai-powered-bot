import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# 🔐 Tokens
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Logging setup
logging.basicConfig(level=logging.INFO)

# Aiogram Bot + Dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# 📦 Import Handlers
from app.handlers.start import register_start_handler
from app.handlers.ai_chat import register_ai_chat_handler

# Register handlers
register_start_handler(dp)
register_ai_chat_handler(dp)

# 🟢 Launch bot
if __name__ == "__main__":
    print("Bot is running...")
    executor.start_polling(dp, skip_updates=True)