from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QApplication, QMainWindow
import sys

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setGeometry(500,200, 500,500)
    window.setWindowTitle("Выбор еды")
    main_text = QtWidgets.QLabel(window)
    main_text.setText("Хватит жрать123456789")
    main_text.move(200,250)
    main_text.adjustSize()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()