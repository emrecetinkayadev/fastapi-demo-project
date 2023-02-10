import hashlib
from .service import get


def check_password(password: str, user_id: int) -> bool:
    old_pass = ""
    hashed_pass = hashlib.sha256(password.encode('utf-8'))
    user = get(user_id=user_id)
    if user:
        old_pass = user["password"]
    if old_pass == hashed_pass:
        return True
    return False


def hash_password(password: str) -> str:
    hashed_pass = hashlib.sha256(password.encode('utf-8'))
    return hashed_pass
