import time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import random


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(500, 200, 500, 500)
        self.setWindowTitle("Выбор еды")
        self.bg = QtWidgets.QProgressBar(self)
        self.bg.move(200, 100)
        self.main_text2 = QtWidgets.QLabel(self)
        self.main_text1 = QtWidgets.QLabel(self)
        self.main_text1.move(200, 150)
        self.main_text2.move(200, 200)
        self.btn = QtWidgets.QToolButton(self)
        self.btn.move(200, 400)
        self.btn.setText("Сгенерировать")
        self.btn.adjustSize()
        self.btn.clicked.connect(self.add_label)

    def add_label(self):
        bk = ['abaya', 'baitur', 'temer', 'moskva']
        mak = ['abaya1', 'baitur1', 'temer1', 'moskva1']
        kfc = ['abaya2', 'baitur2', 'temer2', 'moskva2']
        lists = [kfc, bk, mak]
        cafe = random.choice(lists)
        for name, value in list(locals().items()):
            if cafe is value:
                for i in range(101):
                    time.sleep(0.05)
                    self.bg.setValue(i)
                values = random.choice(cafe)
                self.main_text1.setText("Заведение: " + name)
                self.main_text2.setText("Адресс: " + values)
                self.main_text1.adjustSize()
                self.main_text2.adjustSize()
                break


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
