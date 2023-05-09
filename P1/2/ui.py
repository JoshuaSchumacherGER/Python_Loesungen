from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
from PyQt5.QtCore import Qt


serial_types = {
    "digits": "Nur Zahlen",
    "letters": "Nur Buchstaben",
    "alphanumeric": "Zahlen und Buchstaben"
}


class SerialNumberUI(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.setWindowTitle("Seriennummern")
        self.setMinimumSize(500, 400)

    def init_ui(self):
        layout = QVBoxLayout()

        self.serial_type = QComboBox()

        for key, value in serial_types.items():
            self.serial_type.addItem(value, key)

        layout.addWidget(self.serial_type)

        self.generate_button = QPushButton("Seriennummer generieren")
        layout.addWidget(self.generate_button)

        self.serial_input = QLineEdit()
        layout.addWidget(self.serial_input)

        self.check_button = QPushButton("Seriennummer überprüfen")
        layout.addWidget(self.check_button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)
