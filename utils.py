import hashlib


def get_hash(data: str) -> str:
    return hashlib.sha512(data.encode("utf-8")).hexdigest()[:6]
