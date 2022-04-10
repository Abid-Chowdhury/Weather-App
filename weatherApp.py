import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from time import strftime, gmtime
from requests import get

from UIMainWindow import Ui_mainWindow

from functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        # makes window rounded & removes background
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # move window
        def moveWindow(event):
            if Ui_mainWindow.returnStatus() == 1:
                Ui_mainWindow.maximize_restore(self)
            
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
                
        self.ui.frame.mouseMoveEvent = moveWindow
        
        self.show()
        
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())