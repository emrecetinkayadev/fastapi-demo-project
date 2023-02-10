import typing as t
import hashlib


def max_id(entities) -> t.Optional[int]:
    return max(entities, key=lambda entity: entity["id"]).get("id")


def hash_password(password: str) -> t.Optional[str]:
    hashed_pass = hashlib.sha256(password.encode('utf-8'))
    return hashed_pass
