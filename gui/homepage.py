# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow, QPushButton, QHBoxLayout


class HomePage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(HomePage, self).__init__(parent)
        self.init_ui(self)

    def init_ui(self, HomePage):
        layout = QHBoxLayout()
        self.Button_1 = QPushButton('New Order')
        self.Button_2 = QPushButton('Customer Entry')
        self.Button_3 = QPushButton('Ticket View')
        self.Button_4 = QPushButton('Test')
        layout.addWidget(self.Button_1)
        layout.addWidget(self.Button_2)
        layout.addWidget(self.Button_3)
        layout.addWidget(self.Button_4)
        self.setLayout(layout)


