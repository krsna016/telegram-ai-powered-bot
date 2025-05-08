from aiogram import types, Dispatcher

async def start_command(message: types.Message):
    await message.reply("👋 Hello! I’m your AI-powered assistant. Ask me anything!")

def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])