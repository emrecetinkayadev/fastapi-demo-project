import logging
from functools import wraps


def database_exception_handler(func):
    @wraps(func)
    def wrapper(*args, **kwrds):
        res = None
        try:
            res = func(*args, **kwrds)
        except Exception as SQLAlchemy:
            logging.error(f"SQLAlchemy got some error and rolledbacked. Error: {SQLAlchemy}")
            kwrds["db"].rollback()
        return res
    return wrapper
