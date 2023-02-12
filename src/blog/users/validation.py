import hashlib
from .models import User


def check_password(password: str, user: User) -> bool:
    """Check Password return True if it's correct.

    Args:
        password (str): password for check.
        user (User): user profile which has old password.

    Returns:
        bool: True or False returns.
    """
    old_pass = ""
    hashed_pass = hash_password(password=password)
    if user:
        old_pass = user["password"]
    if old_pass == hashed_pass:
        return True
    return False


def hash_password(password: str) -> str:
    """Hashing password with sha256 algorithm.

    Args:
        password (str): password string.

    Returns:
        str: hashed password.
    """
    hashed_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_pass
