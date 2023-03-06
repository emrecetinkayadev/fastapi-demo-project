import logging
from functools import wraps
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


def database_exception_handler(func):
    def wrapper(*args, **kwrds):
        res = None
        try:
            res = func(*args, **kwrds)
        except Exception as e:
            logging.error(f"Transaction was rolledback. Due to the error: {e}")
            kwrds["db"].rollback()
            res = HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=[{"msg": "Bad Request."}]
            )
        return res
    return wrapper
