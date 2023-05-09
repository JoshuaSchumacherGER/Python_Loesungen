import sys
import csv
import random
import string
from ui import SerialNumberUI
from PyQt5.QtWidgets import QApplication
from typing import NamedTuple, List

serial_length = 10
data_file = "data.csv"

SerialNumber = NamedTuple(
    "SerialNumber", [
        ("serial_number", str),
        ("used", bool)
    ]
)


class SerialNumberGenerator:
    def __init__(self, ui: SerialNumberUI):
        super().__init__()
        self.ui = ui
        self.data = self.load_data()
        self.ui.generate_button.clicked.connect(self.generate_button_clicked)
        self.ui.check_button.clicked.connect(self.check_button_clicked)

    def generate_button_clicked(self):
        serial_type = self.ui.serial_type.currentData()

        if serial_type == "digits":
            serial_number = self.generate_serial_number(string.digits)
        elif serial_type == "letters":
            serial_number = self.generate_serial_number(string.ascii_letters)
        else:
            serial_number = self.generate_serial_number(
                string.ascii_letters + string.digits
            )
        self.data.append(SerialNumber(serial_number, False))
        self.ui.serial_input.setText(serial_number)
        self.save_data()

    def check_button_clicked(self):
        entered_serial = self.ui.serial_input.text()
        self.check_serial_number(entered_serial)
        self.save_data()

    def generate_serial_number(self, characters):
        return "".join(random.choices(characters, k=serial_length))

    def check_serial_number(self, serial_number):
        for index, data in enumerate(self.data):
            if data.serial_number == serial_number:
                if data.used:
                    self.ui.result_label.setText("Seriennnummer bereits verwendet")
                else:
                    self.ui.result_label.setText("Seriennnummer akzeptiert")
                    self.data[index] = SerialNumber(serial_number, True)
                return

        self.ui.result_label.setText("Seriennummer ungültig")

    def load_data(self) -> List[SerialNumber]:
        serial_numbers = []

        with open(data_file, "r") as csvfile:
            csv_reader = csv.reader(csvfile)

            for row in csv_reader:
                serial_numbers.append(SerialNumber(row[0], row[1] == "used"))

        return serial_numbers

    def save_data(self):
        with open(data_file, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)

            for serial_number in self.data:
                csv_writer.writerow(
                    [
                        serial_number.serial_number,
                        "used" if serial_number.used else "not_used"
                    ]
                )


def main():
    app = QApplication(sys.argv)
    ui = SerialNumberUI()
    ui.show()
    generator = SerialNumberGenerator(ui)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
