import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QGraphicsDropShadowEffect,
)
from PySide6.QtGui import QColor, QFont

# Modern Styling using Qt Style Sheets (QSS)
MODERN_STYLE = """
    QMainWindow {
        background-color: #121214;
    }
    
    QWidget #cardContainer {
        background-color: #1a1a1e;
        border-radius: 12px;
        border: 1px solid #2a2a30;
    }
    
    QLabel #titleLabel {
        color: #ffffff;
        font-weight: bold;
    }
    
    QLabel #subtitleLabel {
        color: #a0a0aa;
    }
    
    QLineEdit {
        background-color: #26262b;
        color: #ffffff;
        border: 2px solid #26262b;
        border-radius: 8px;
        padding: 10px 14px;
        selection-background-color: #007acc;
    }
    
    QLineEdit:focus {
        border: 2px solid #007acc;
        background-color: #1a1a1e;
    }
    
    QPushButton {
        background-color: #007acc;
        color: #ffffff;
        border: none;
        border-radius: 8px;
        padding: 12px;
        font-weight: bold;
    }
    
    QPushButton:hover {
        background-color: #0098ff;
    }
    
    QPushButton:pressed {
        background-color: #005999;
    }
    
    QLabel #resultLabel {
        color: #4ade80;
        font-weight: 500;
    }
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configure Window
        self.setWindowTitle("Modern PySide6 App")
        self.setMinimumSize(QSize(400, 500))

        # Main Layout Wrapper
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Styled Visual Card Container
        card = QWidget()
        card.setObjectName("cardContainer")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(24, 24, 24, 24)
        card_layout.setSpacing(16)

        # Subtle Drop Shadow Effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 160))
        shadow.setOffset(0, 4)
        card.setGraphicsEffect(shadow)

        # Typography & Headers
        self.title_label = QLabel("Welcome Back !")
        self.title_label.setObjectName("titleLabel")
        self.title_label.setFont(QFont("Segoe UI", 22))

        self.subtitle_label = QLabel("Enter your name to interact with the system.")
        self.subtitle_label.setObjectName("subtitleLabel")
        self.subtitle_label.setFont(QFont("Segoe UI", 10))
        self.subtitle_label.setWordWrap(True)

        # Form Controls
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your name here...")
        self.input_field.setFont(QFont("Segoe UI", 11))

        # Interactive Button
        self.action_btn = QPushButton("Continue")
        self.action_btn.setFont(QFont("Segoe UI", 11))
        self.action_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        # Output Area
        self.result_label = QLabel("")
        self.result_label.setObjectName("resultLabel")
        self.result_label.setFont(QFont("Segoe UI", 11))
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Assembling Layouts
        card_layout.addWidget(self.title_label)
        card_layout.addWidget(self.subtitle_label)
        card_layout.addWidget(self.input_field)
        card_layout.addWidget(self.action_btn)
        card_layout.addWidget(self.result_label)

        main_layout.addWidget(card)

        # Connect signals to slots
        self.action_btn.clicked.connect(self.handle_submission)
        self.input_field.returnPressed.connect(self.handle_submission)

    def handle_submission(self):
        """Slot to process user submission input."""
        user_text = self.input_field.text().strip()
        if user_text:
            self.result_label.setText(f"Hello, {user_text}! Access granted.")
        else:
            self.result_label.setText("Please fill out the text field first.")
            self.result_label.setStyleSheet("color: #f87171;")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
