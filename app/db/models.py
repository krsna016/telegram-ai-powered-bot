from sqlalchemy import create_engine, Column, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import pytz  # ← Add this
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Define your timezone (e.g., Asia/Kolkata for IST)
IST = pytz.timezone("Asia/Kolkata")

def current_ist_time():
    return datetime.now(IST)

class ChatLog(Base):
    __tablename__ = "chat_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    user_msg = Column(Text)
    ai_msg = Column(Text)
    timestamp = Column(DateTime, default=current_ist_time)  # ✅ IST-based