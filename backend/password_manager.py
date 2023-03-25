import hashlib


def encrypt_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def check_password(password_login: str, password_user: str) -> bool:
    if encrypt_password(password_login) == encrypt_password(password_user):
        return True
    return False

