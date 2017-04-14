import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class LittleBig(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lb = LittleBig()
    lb.show()
    sys.exit(app.exec())