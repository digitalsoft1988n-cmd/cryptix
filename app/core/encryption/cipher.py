from cryptography.fernet import Fernet
import base64
import hashlib


def generate_key(password: str) -> bytes:
    digest = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(digest)


def encrypt(text: str, password: str) -> bytes:
    key = generate_key(password)
    return Fernet(key).encrypt(text.encode())


def decrypt(token: bytes, password: str) -> str:
    key = generate_key(password)
    return Fernet(key).decrypt(token).decode()


if __name__ == "__main__":
    password = "SuperSecret@4566"
    key = generate_key(password=password)

    print("Key:", key)