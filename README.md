# 🚀 TELEGRAM AI BUSSINESS TALK BOT:

An intelligent, memory-aware AI chatbot for Telegram — powered by Google Gemini AI.  
It serves as your 24/7 business assistant, handling both company-specific queries and open-domain conversations. 🚀

---

## ✅ Features

- 🤖 Gemini-powered AI for natural, helpful conversations  
- 🧠 Chat memory for personalized user sessions  
- 🏢 Loads your business profile from `company_profile.txt`  
- 🗂️ Clean architecture (handlers, services, DB, utils)  
- 💬 Handles both business-specific and general questions  
- 🛢️ SQLite DB to log user queries and responses  
- ⚙️ Easily customizable context and behavior

---

## 🔧 Setup Guide

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt

## Create a .env file in the root directory:
- GEMINI_API_KEY=your_google_gemini_api_key
- BOT_TOKEN=your_telegram_bot_token

## Add your company context:
- add content to: app/assets/company_profile.txt

## Initialize the database:
- python db_init.py

## Run the bot:
- python main.py
