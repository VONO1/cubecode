from PyQt5.QtWidgets import QApplication,  QMainWindow
#QWidger - абстрактный класс виджета
#QApplication - абстрактный класс приложения
import  sys


#главное окно всегда настледуется от QMainWindow
class Start(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(400,300)


if __name__ == '__main__':
    # Конструктор
    # Передаём аргументы командной строки
    app = QApplication(sys.argv)

    w = Start()
    w.show()

    # Запуск приложения
    sys.exit(app.exec_())

"""
Основные модули:
QtCore
QtGui
QtWidgets
QtNetwork


QSql
QWebKit
QWebKitWidgets
"""
