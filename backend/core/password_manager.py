import hashlib


def encrypt_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password_login: str, password_user: str) -> bool:
    if encrypt_password(password_login) == password_user:
        return True
    return False
