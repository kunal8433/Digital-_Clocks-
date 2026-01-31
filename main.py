import sys

from PyQt5.QtWidgets import QApplication, QWidget , QLabel,QVBoxLayout 
from PyQt5.QtCore import QTimer , QTimer , Qt ,QTime

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_lable = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("KUNAL CLOCK")
        self.setGeometry(600,400,300,100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_lable)
        self.setLayout(vbox)

        self.time_lable.setAlignment(Qt.AlignCenter)

        self.time_lable.setStyleSheet("font-size:150px;"
                                      "font-family:Arial")
        self.setStyleSheet("background - colour: black;")

        self.update_time()
        
    def update_time(self):
            current_time = QTime.currentTime().toString("hh:mm:ss AP")
            self.time_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())

