from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QDoubleSpinBox, QPushButton, QVBoxLayout
import sys

class Converter(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUi()
        self.initSignals()
        self.initLayouts()



    def initUi(self):
        self.setWindowTitle('Конветер валют')
        self.srcLabel =QLabel('Сумма в рублях', self)
        self.srcAmount = QDoubleSpinBox(self)
        self.srcAmount.setMaximum(9999999999)

        self.resultLabel = QLabel('Сумма в долларах', self)
        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(999999999999)

        self.convertBtn = QPushButton('Перевести', self)


    def initSignals(self):
        pass

    def initLayouts(self):
        w = QWidget(self)
        self.mainlayout = QVBoxLayout(w)
        self.mainlayout.addWidget(self.srcLabel)
        self.mainlayout.addWidget(self.srcAmount)
        self.mainlayout.addWidget(self.resultLabel)
        self.mainlayout.addWidget(self.resultAmount)
        self.mainlayout.addWidget(self.convertBtn)

        self.setCentralWidget(w)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    cc = Converter()
    cc.show()
    sys.exit(app.exec())