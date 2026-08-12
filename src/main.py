import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

APP_VERSION = "1.0.3"

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("LMS Tracker - Test Build")
        self.setGeometry(100, 100, 360, 200)

        layout = QVBoxLayout()
        self.label = QLabel(f"<b>LMS Tracker Client</b><br>Version: {APP_VERSION}", self)
        layout.addWidget(self.label)

        self.btn = QPushButton("Test Application Status", self)
        self.btn.clicked.connect(self.on_click)
        layout.addWidget(self.btn)

        self.setLayout(layout)

    def on_click(self):
        self.label.setText(f"<b>LMS Tracker Client</b><br>Status: Active and Running! (v{APP_VERSION})")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())