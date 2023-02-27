from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

db_url = "postgresql://username:password@db:5432/fastapi"

engine = create_engine(db_url, pool_size=5, pool_recycle=3600)

Base = declarative_base()
metadata = Base.metadata
SessionLocal = sessionmaker(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

