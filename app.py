import os
import sys
import PyQt5
pyqt = os.path.dirname(PyQt5.__file__)
os.environ['QT_PLUGIN_PATH'] = os.path.join(pyqt, "Qt5/plugins")

from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QWidget, QVBoxLayout

from q_group_box import QVersionBox

class App(QMainWindow):

    def __init__(self):
        super().__init__()

        # app geometry
        self.width = 800
        self.height = 600
        # app position
        self.left = int(abs((QDesktopWidget().screenGeometry().width() - self.width) / 2.0))
        self.top = int(abs((QDesktopWidget().screenGeometry().height() - self.height) / 2.0))

        self.setGeometry(self.left, self.top, self.width, self.height)
        # self.showFullScreen()

        self.mainWidget = QWidget()
        self.layout = QVBoxLayout()
        self.box = QVersionBox()
        self.layout.addWidget(self.box)
        self.mainWidget.setLayout(self.layout)

        self.setCentralWidget(self.mainWidget)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('widowsvista')
    ex = App()
    ex.show()
    sys.exit(app.exec_())
