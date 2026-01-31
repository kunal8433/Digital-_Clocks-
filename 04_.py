import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt, QTime


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()

        self.time_label = QLabel(self)
        self.timer = QTimer(self)

        self.initUI()

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def initUI(self):
        self.setWindowTitle("KUNAL CLOCK")
        self.resize(400, 200)

        layout = QVBoxLayout()
        layout.addWidget(self.time_label)
        self.setLayout(layout)

        # center me
        self.time_label.setAlignment(Qt.AlignCenter)

        # big size
        self.time_label.setStyleSheet(
            "font-size: 60px;"
            "font-family: Arial;"
            "color: white;"
        )

        self.setStyleSheet("background-color: black;")

    def update_time(self):
        # 12-hour real clock format (10:28 PM)
        current_time = QTime.currentTime().toString("hh:mm AP")
        self.time_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec())
