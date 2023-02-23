import hashlib


def hash_password(password: str) -> str:
    """Hashing password with sha256 algorithm.

    Args:
        password (str): password string.

    Returns:
        str: hashed password.
    """
    hashed_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_pass
