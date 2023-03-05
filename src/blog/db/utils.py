import logging
from functools import wraps
from sqlalchemy.orm import Session


def database_exception_handler(func):
    @wraps
    def wrapper(db: Session):
        try:
            res = func(db)
        except Exception as e:
            logging.error(f"Transaction was rolledback. Due to the error: {e}")
            db.rollback()
        return res
    return wrapper
