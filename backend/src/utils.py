import base64
import hashlib
import random

from sqlalchemy.orm import Session

from .models import Url


def get_hash(url: str) -> str:
    sha256_hash = hashlib.sha256(url.encode()).digest()

    base64_encoded = base64.b64encode(sha256_hash).decode("utf-8")

    custom_base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    custom_hash_string = "".join([custom_base64_chars[ord(c) % 62] for c in base64_encoded if c in custom_base64_chars])

    return custom_hash_string[:4]


def check_hash_exists(hashdata: str, db: Session) -> bool:
    return bool(db.query(Url).get(hashdata))


def generate_new_hash(url: str, db: Session) -> str:
    failed = True
    h = url

    while failed:
        url += str(random.randint(1, 100))
        h = get_hash(url)
        failed = check_hash_exists(h, db)

    return h
