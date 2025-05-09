from prettytable import PrettyTable
from app.db.models import SessionLocal, ChatLog

def print_chat_logs(limit=10):
    session = SessionLocal()
    chats = session.query(ChatLog).order_by(ChatLog.timestamp.desc()).limit(limit).all()

    table = PrettyTable()
    table.field_names = ["ID", "User ID", "User Message", "AI Message", "Timestamp"]

    for chat in chats:
        table.add_row([
            chat.id,
            chat.user_id,
            chat.user_msg[:40] + "..." if len(chat.user_msg) > 40 else chat.user_msg,
            chat.ai_msg[:40] + "..." if len(chat.ai_msg) > 40 else chat.ai_msg,
            chat.timestamp.strftime("%Y-%m-%d %H:%M")
        ])

    print(table)

if __name__ == "__main__":
    print_chat_logs(limit=500000)