from app.db.models import SessionLocal, ChatLog

def save_conversation(user_id, user_message, bot_response):
    """Save the conversation to the database."""
    db_session = SessionLocal()
    try:
        chat_session = ChatLog(
            user_id=user_id,
            user_msg=user_message,
            ai_msg=bot_response
        )
        db_session.add(chat_session)
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        print(f"❌ Error saving conversation: {e}")
    finally:
        db_session.close()