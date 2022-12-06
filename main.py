import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import *


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r'C:\Users\79082\PycharmProjects\pythonProject4\venv\untitled.ui', self)  # Загружаем дизайн
        self.run()
        self.array = []

    def run(self):
        self.pushButton.clicked.connect(self.hello)

    def hello(self):
        self.n = QListWidget(self)
        s = self.calendarWidget.selectedDate().toString(
            'dd.MM.yyyy') + " " + self.timeEdit.time().toString() + ' ' + self.lineEdit.text()
        self.listWidget.addItem(s)
        self.listWidget.sortItems()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
