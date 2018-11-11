from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QToolTip
from PyQt5.QtCore import QCoreApplication
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Window"
        self.top = 100  # 距离屏幕的高
        self.left = 100
        self.width = 680  # 窗口的宽
        self.height = 500

        self.setWindowIcon(QtGui.QIcon("D:\达内python\AID1808\object\skunk.ico"))

        button = QPushButton("Chick Me", self)
        button.move(270, 250)
        button.setToolTip("<h3>This is Chick Button</h3>")
        button.clicked.connect(self.close)

        self.InitWindow()
        self.paintEventse()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintEventse(self):
        # self.setStyleSheet("Window{background-color:yellow}")
        self.setStyleSheet("Window{background-image:url('D:\达内python\AID1808\object\2.jpg')}")

    def close(self):
        QCoreApplication.instance().quit()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
