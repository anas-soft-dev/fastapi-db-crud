from app.database import SessionLocal

def get_db():
    db = SessionLocal()
    print("before yeild")
    yield db
    print("after yeild")
    db.close()