from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost:5432/st"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

app = FastAPI(
    title="ApplogiQ Report"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
