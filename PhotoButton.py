import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QMessageBox, QApplication)
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from GUI import Windows


class PhotoButton():

    def __init__(self, windows, path, size1, size2, location):
        self.path = path
        self.size1 = size1
        self.size2 = size2
        self.location = location
        # self.LeagueButton(windows)
        self.btn = self.LeagueButton(windows)

    def LeagueButton(self, windows):
        botton = QPushButton(windows)
        botton.setIcon(QIcon(self.path))
        botton.setIconSize(QtCore.QSize(self.size1, self.size2))
        botton.setToolTip('Choose one league you want')
        botton.resize(botton.sizeHint())
        botton.setGeometry(0, self.location, 200, 100)
        return botton
