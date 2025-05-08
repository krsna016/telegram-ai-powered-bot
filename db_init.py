from app.db.models import Base, engine

# ✅ Run this ONCE to create the DB
def init_db():
    print("📦 Creating database schema...")
    Base.metadata.create_all(bind=engine)
    print("✅ DB initialized successfully.")

if __name__ == "__main__":
    init_db()