from services.encryption_service import EncryptionService


class EncryptionController:
    def __init__(self):
        self.service = EncryptionService()

    def encrypt(self, text, password):
        return self.service.encrypt_text(text, password)

    def decrypt(self, text, password):
        return self.service.decrypt_text(text, password)
