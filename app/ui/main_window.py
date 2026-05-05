from PySide6.QtWidgets import QMainWindow, QTabWidget

from ui.views.encrypt_view import EncryptView
from ui.views.decrypt_view import DecryptView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("KeyCrypt")
        self.resize(600, 450)

        self.tabs = QTabWidget()

        # Tabs
        self.encrypt_tab = EncryptView()
        self.decrypt_tab = DecryptView()

        self.tabs.addTab(self.encrypt_tab, "Encrypt")
        self.tabs.addTab(self.decrypt_tab, "Decrypt")

        self.setCentralWidget(self.tabs)
