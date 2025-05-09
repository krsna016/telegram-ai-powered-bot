from app.db.models import SessionLocal, ChatLog
from app.db.models import ChatLog
from app.db.models import SessionLocal

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


def get_recent_conversations(user_id, limit=5):
    """Fetch last `limit` chat logs for a user."""
    session = SessionLocal()
    try:
        chats = session.query(ChatLog)\
            .filter(ChatLog.user_id == user_id)\
            .order_by(ChatLog.timestamp.desc())\
            .limit(limit)\
            .all()
        return chats[::-1]  # Return in chronological order
    finally:
        session.close()