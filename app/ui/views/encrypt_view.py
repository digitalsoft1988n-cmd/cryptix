from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit,
    QTextEdit, QPushButton, QMessageBox, QHBoxLayout
)
from PySide6.QtGui import QGuiApplication

from ui.controllers.encryption_controller import EncryptionController


class EncryptView(QWidget):
    def __init__(self):
        super().__init__()

        self.controller = EncryptionController()
        self._setup_ui()

    def _setup_ui(self):
        layout = QVBoxLayout()

        # Key
        layout.addWidget(QLabel("Encryption Key:"))
        self.key_input = QLineEdit()
        layout.addWidget(self.key_input)

        # Plain text
        layout.addWidget(QLabel("Text to Encrypt:"))
        self.input_text = QTextEdit()
        layout.addWidget(self.input_text)

        # Encrypt button
        self.encrypt_btn = QPushButton("Encrypt")
        self.encrypt_btn.clicked.connect(self.handle_encrypt)
        layout.addWidget(self.encrypt_btn)

        # Output
        layout.addWidget(QLabel("Encrypted Text:"))
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

    def handle_encrypt(self):
        key = self.key_input.text()
        text = self.input_text.toPlainText()

        if not key or not text:
            QMessageBox.warning(self, "Error", "Key and text are required.")
            return

        try:
            result = self.controller.encrypt(text, key)
            self.output_text.setPlainText(result)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def copy_output(self):
        text = self.output_text.toPlainText()

        if not text:
            QMessageBox.information(self, "Info", "Nothing to copy.")
            return

        QGuiApplication.clipboard().setText(text)
        QMessageBox.information(self, "Copied", "Copied to clipboard.")