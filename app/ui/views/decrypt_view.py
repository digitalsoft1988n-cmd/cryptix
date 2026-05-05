from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QMessageBox,
    QHBoxLayout,
)
from PySide6.QtGui import QGuiApplication

from ui.controllers.encryption_controller import EncryptionController


class DecryptView(QWidget):
    def __init__(self):
        super().__init__()

        self.controller = EncryptionController()
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout()

        # Key
        layout.addWidget(QLabel("Decryption Key:"))
        self.key_input = QLineEdit()
        layout.addWidget(self.key_input)

        # Encrypted input
        layout.addWidget(QLabel("Encrypted Text:"))
        self.input_text = QTextEdit()
        layout.addWidget(self.input_text)

        # Decrypt button
        self.decrypt_btn = QPushButton("Decrypt")
        self.decrypt_btn.clicked.connect(self.handle_decrypt)
        layout.addWidget(self.decrypt_btn)

        # Output
        layout.addWidget(QLabel("Decrypted Text:"))
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        # Copy button
        row = QHBoxLayout()
        self.copy_btn = QPushButton("Copy")
        self.copy_btn.clicked.connect(self.copy_output)
        row.addWidget(self.copy_btn)

        layout.addLayout(row)
        self.setLayout(layout)

    def handle_decrypt(self):
        key = self.key_input.text()
        text = self.input_text.toPlainText()

        if not key or not text:
            QMessageBox.warning(self, "Error", "Key and encrypted text are required.")
            return

        try:
            result = self.controller.decrypt(text, key)
            self.output_text.setPlainText(result)
        except Exception:
            QMessageBox.critical(self, "Error", "Invalid key or corrupted data.")

    def copy_output(self):
        text = self.output_text.toPlainText()

        if not text:
            QMessageBox.information(self, "Info", "Nothing to copy.")
            return

        QGuiApplication.clipboard().setText(text)
        QMessageBox.information(self, "Copied", "Copied to clipboard.")
