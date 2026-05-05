from core.encryption.cipher import encrypt, decrypt


class EncryptionService:
    def encrypt_text(self, text: str, password: str) -> str:
        return encrypt(text, password).decode()

    def decrypt_text(self, text: str, password: str) -> str:
        return decrypt(text.encode(), password)
