import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt, QTime


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()

        self.time_label = QLabel("00:00:00", self)
        self.timer = QTimer(self)

        self.initUI()

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def initUI(self):
        self.setWindowTitle("KUNAL CLOCK")
        self.setGeometry(600, 400, 300, 100)

        layout = QVBoxLayout()
        layout.addWidget(self.time_label)
        self.setLayout(layout)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet(
            "font-size: 40px;"
            "font-family: Arial;"
            "color: white;"
        )

        self.setStyleSheet("background-color: black;")

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec())
