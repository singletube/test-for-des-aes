from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore    import *                           
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import * 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)



class Widget(QWidget):
    def __init__(self, parent):
        super(Widget, self).__init__(parent)
        self.setFixedSize(1400, 1700)

        widget = QWidget()
        layout = QVBoxLayout(self)
        pixmap = QPixmap('Aesteory.png')
        image = QLabel()
        image.setPixmap(pixmap)
        layout.addWidget(image)
        widget.setLayout(layout)
        layout.setGeometry(QtCore.QRect(0, 0, 700, 700))
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        scroll.setWidget(widget)
        vLayout = QVBoxLayout(self)
        vLayout.addWidget(scroll)
        self.setLayout(vLayout)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.widget = Widget(self.centralwidget)

        self.grid = QGridLayout(self.centralwidget)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()  # QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())