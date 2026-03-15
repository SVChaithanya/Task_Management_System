from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:surya_851973@localhost:5432/multi_user"
)

engine = create_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()