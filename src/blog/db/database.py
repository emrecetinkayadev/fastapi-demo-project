from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://username:password@db:5432/fastapi"

engine = create_engine(db_url, pool_size=5, pool_recycle=3600)

Base = declarative_base()


def create_tables():
    Base.metadata.create_all(bind=engine)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
