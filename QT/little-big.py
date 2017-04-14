import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class LittleBig(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        #свойство увеличивать или уменьшать окно
        self.__increment = True


        self.initUi()
        self.initSignals()

    def initUi(self):
        self.resize(400,300)
        self.setMinimumSize(300,200)
        self.setMaximumSize(600,400)

        self.btn = QPushButton('We will push the button',self)
        self.setCentralWidget(self.btn)

    #метод для улавливания сигналов
    def initSignals(self):
        self.btn.clicked.connect(self.onClick)

    def onClick(self):
        if self.__increment:
            self.resize(self.width() + 10, self.height() + 10)
        else:
            self.resize(self.width() - 10, self.height() - 10)
        if self.width() <= self.minimumWidth():
            self.__increment = True
        if self.width() >= self.maximumWidth():
            self.__increment = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    lb = LittleBig()
    lb.show()
    sys.exit(app.exec())