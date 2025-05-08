from app.db.models import SessionLocal, ChatLog

def log_chat(user_id: int, user_msg: str, ai_msg: str):
    db = SessionLocal()
    try:
        chat_log = ChatLog(user_id=user_id, user_msg=user_msg, ai_msg=ai_msg)
        db.add(chat_log)
        db.commit()
    except Exception as e:
        db.rollback()
        print("❌ Error logging chat:", e)
    finally:
        db.close()