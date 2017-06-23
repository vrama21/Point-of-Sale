# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Programming\Point of Sale\Design\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import *
from PyQt5.QtCore import (QSize, QCoreApplication, QRect, QMetaObject)
from PyQt5.QtWidgets import (QSizePolicy, QMainWindow, QApplication, QStatusBar, QToolBar,
                             QPushButton, QTableWidgetItem, QGridLayout, QWidget, QLayout,
                             QTableWidget, QHBoxLayout, QMessageBox)

# from .functions import *

def close_application(self):
    choice = QMessageBox.question(self, 'Alert!',
                                  "Are you sure you want to close the program?",
                                  QMessageBox.Yes | QMessageBox.No)
    if choice == QMessageBox.Yes:
        print("Closing Application")
        sys.exit()
    if choice == QMessageBox.No:
        pass


class OrderWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QSize(1024, 768))
        MainWindow.setMaximumSize(QSize(1024, 768))

        """ Frame Layouts"""
        self.main_frame = QWidget(MainWindow)
        self.main_frame.setObjectName("Main_Frame")

        self.menu_grid = QWidget(self.main_frame)
        self.menu_grid.setGeometry(QRect(310, 0, 700, 625))
        self.menu_grid.setObjectName("Menu_Grid")

        self.nav_bar = QWidget(self.main_frame)
        self.nav_bar.setGeometry(QRect(0, 615, 1015, 131))
        self.nav_bar.setObjectName("Navigation_Bar")

        self.Navigation_Bar = QHBoxLayout(self.nav_bar)
        self.Navigation_Bar.setContentsMargins(10, 10, 10, 10)
        self.Navigation_Bar.setSpacing(0)
        self.Navigation_Bar.setObjectName("Navigation_Bar_Layout")

        self.Menu_Buttons = QGridLayout(self.menu_grid)
        self.Menu_Buttons.setSizeConstraint(QLayout.SetMinimumSize)
        self.Menu_Buttons.setContentsMargins(10, 10, 10, 10)
        self.Menu_Buttons.setSpacing(0)
        self.Menu_Buttons.setObjectName("Menu_Grid_Layout")

        self.tableWidget = QTableWidget(self.main_frame)
        ticket_table = self.tableWidget
        ticket_table.setGeometry(QRect(10, 10, 305, 600))
        ticket_table.setShowGrid(True)
        ticket_table.setObjectName("Ticket_Table")
        ticket_table.setColumnCount(3)
        ticket_table.setRowCount(15)

        """ Menu Buttons"""
        self.btn01 = QPushButton(self.menu_grid)
        self.btn02 = QPushButton(self.menu_grid)
        self.btn03 = QPushButton(self.menu_grid)
        self.btn04 = QPushButton(self.menu_grid)
        self.btn05 = QPushButton(self.menu_grid)
        self.btn06 = QPushButton(self.menu_grid)
        self.btn07 = QPushButton(self.menu_grid)
        self.btn08 = QPushButton(self.menu_grid)
        self.btn09 = QPushButton(self.menu_grid)
        self.btn10 = QPushButton(self.menu_grid)
        self.btn11 = QPushButton(self.menu_grid)
        self.btn12 = QPushButton(self.menu_grid)
        self.btn13 = QPushButton(self.menu_grid)
        self.btn14 = QPushButton(self.menu_grid)
        self.btn15 = QPushButton(self.menu_grid)
        self.btn16 = QPushButton(self.menu_grid)
        self.btn17 = QPushButton(self.menu_grid)
        self.btn18 = QPushButton(self.menu_grid)
        self.btn19 = QPushButton(self.menu_grid)
        self.btn20 = QPushButton(self.menu_grid)
        self.btn21 = QPushButton(self.menu_grid)
        self.btn22 = QPushButton(self.menu_grid)
        self.btn23 = QPushButton(self.menu_grid)
        self.btn24 = QPushButton(self.menu_grid)
        self.btn25 = QPushButton(self.menu_grid)

        self.create_menu_buttons(self.btn01)
        self.create_menu_buttons(self.btn02)
        self.create_menu_buttons(self.btn03)
        self.create_menu_buttons(self.btn04)
        self.create_menu_buttons(self.btn05)
        self.create_menu_buttons(self.btn06)
        self.create_menu_buttons(self.btn07)
        self.create_menu_buttons(self.btn08)
        self.create_menu_buttons(self.btn09)
        self.create_menu_buttons(self.btn10)
        self.create_menu_buttons(self.btn11)
        self.create_menu_buttons(self.btn12)
        self.create_menu_buttons(self.btn13)
        self.create_menu_buttons(self.btn14)
        self.create_menu_buttons(self.btn15)
        self.create_menu_buttons(self.btn16)
        self.create_menu_buttons(self.btn17)
        self.create_menu_buttons(self.btn18)
        self.create_menu_buttons(self.btn19)
        self.create_menu_buttons(self.btn20)
        self.create_menu_buttons(self.btn21)
        self.create_menu_buttons(self.btn22)
        self.create_menu_buttons(self.btn23)
        self.create_menu_buttons(self.btn24)
        self.create_menu_buttons(self.btn25)

        self.Menu_Buttons.addWidget(self.btn01, 0, 0, 1, 1)
        self.Menu_Buttons.addWidget(self.btn02, 0, 1, 1, 1)
        self.Menu_Buttons.addWidget(self.btn03, 0, 2, 1, 1)
        self.Menu_Buttons.addWidget(self.btn04, 0, 3, 1, 1)
        self.Menu_Buttons.addWidget(self.btn05, 0, 4, 1, 1)
        self.Menu_Buttons.addWidget(self.btn06, 1, 0, 1, 1)
        self.Menu_Buttons.addWidget(self.btn07, 1, 1, 1, 1)
        self.Menu_Buttons.addWidget(self.btn08, 1, 2, 1, 1)
        self.Menu_Buttons.addWidget(self.btn09, 1, 3, 1, 1)
        self.Menu_Buttons.addWidget(self.btn10, 1, 4, 1, 1)
        self.Menu_Buttons.addWidget(self.btn11, 2, 0, 1, 1)
        self.Menu_Buttons.addWidget(self.btn12, 2, 1, 1, 1)
        self.Menu_Buttons.addWidget(self.btn13, 2, 2, 1, 1)
        self.Menu_Buttons.addWidget(self.btn14, 2, 3, 1, 1)
        self.Menu_Buttons.addWidget(self.btn15, 2, 4, 1, 1)
        self.Menu_Buttons.addWidget(self.btn16, 3, 0, 1, 1)
        self.Menu_Buttons.addWidget(self.btn17, 3, 1, 1, 1)
        self.Menu_Buttons.addWidget(self.btn18, 3, 2, 1, 1)
        self.Menu_Buttons.addWidget(self.btn19, 3, 3, 1, 1)
        self.Menu_Buttons.addWidget(self.btn20, 3, 4, 1, 1)
        self.Menu_Buttons.addWidget(self.btn21, 4, 0, 1, 1)
        self.Menu_Buttons.addWidget(self.btn22, 4, 1, 1, 1)
        self.Menu_Buttons.addWidget(self.btn23, 4, 2, 1, 1)
        self.Menu_Buttons.addWidget(self.btn24, 4, 3, 1, 1)
        self.Menu_Buttons.addWidget(self.btn25, 4, 4, 1, 1)

        """ T"""
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 50)

        """ Navigation Buttons """

        self.btn_back = QPushButton(self.nav_bar)
        self.create_nav_buttons(self.btn_back)
        self.Navigation_Bar.addWidget(self.btn_back)
        # self.btn_back.clicked.connect(close_application(OrderWindow))

        self.btnQty = QPushButton(self.nav_bar)
        self.create_nav_buttons(self.btnQty)
        self.Navigation_Bar.addWidget(self.btnQty)

        self.pushButton_2 = QPushButton(self.nav_bar)
        self.create_nav_buttons(self.pushButton_2)
        self.Navigation_Bar.addWidget(self.pushButton_2)

        self.pushButton_5 = QPushButton(self.nav_bar)
        self.create_nav_buttons(self.pushButton_5)
        self.Navigation_Bar.addWidget(self.pushButton_5)

        self.btnNext = QPushButton(self.nav_bar)
        self.create_nav_buttons(self.btnNext)
        self.Navigation_Bar.addWidget(self.btnNext)
        MainWindow.setCentralWidget(self.main_frame)

        # self.menuBar = QMenuBar(MainWindow)
        # self.menuBar.setGeometry(QRect(0, 0, 1024, 21))
        # self.menuBar.setObjectName("menuBar")
        # MainWindow.setMenuBar(self.menuBar)

        # self.mainToolBar = QToolBar(MainWindow)
        # self.mainToolBar.setObjectName("mainToolBar")
        # MainWindow.addToolBar(QtWidget.ToolBarArea, self.mainToolBar)

        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Swayblade's Point of Sale"))
        self.btn01.setText(_translate("MainWindow", "Category 1"))
        self.btn02.setText(_translate("MainWindow", "Category 2"))
        self.btn03.setText(_translate("MainWindow", "Category 3"))
        self.btn04.setText(_translate("MainWindow", "Category 4"))
        self.btn05.setText(_translate("MainWindow", "Category 5"))
        self.btn06.setText(_translate("MainWindow", "Category 6"))
        self.btn07.setText(_translate("MainWindow", "Category 7"))
        self.btn08.setText(_translate("MainWindow", "Category 8"))
        self.btn09.setText(_translate("MainWindow", "Category 9"))
        self.btn10.setText(_translate("MainWindow", "Category 10"))
        self.btn11.setText(_translate("MainWindow", "Category 11"))
        self.btn12.setText(_translate("MainWindow", "Category 12"))
        self.btn13.setText(_translate("MainWindow", "Category 13"))
        self.btn14.setText(_translate("MainWindow", "Category 14"))
        self.btn15.setText(_translate("MainWindow", "Category 15"))
        self.btn16.setText(_translate("MainWindow", "Category 16"))
        self.btn17.setText(_translate("MainWindow", "Category 17"))
        self.btn18.setText(_translate("MainWindow", "Category 18"))
        self.btn19.setText(_translate("MainWindow", "Category 19"))
        self.btn20.setText(_translate("MainWindow", "Category 20"))
        self.btn21.setText(_translate("MainWindow", "Category 21"))
        self.btn22.setText(_translate("MainWindow", "Category 22"))
        self.btn23.setText(_translate("MainWindow", "Category 23"))
        self.btn24.setText(_translate("MainWindow", "Category 24"))
        self.btn25.setText(_translate("MainWindow", "Category 25"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Items"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))

        self.btn_back.setText(_translate("MainWindow", "Back"))
        self.btnQty.setText(_translate("MainWindow", "Quantity"))
        self.pushButton_2.setText(_translate("MainWindow", "1"))
        self.pushButton_5.setText(_translate("MainWindow", "2"))
        self.btnNext.setText(_translate("MainWindow", "Next"))

    def add_item(self, qty, item, price):
        table_widget = self.tableWidget
        self.qty = qty
        self.item = item
        self.price = price
        table_widget.setItem(1, 0, qty)
        table_widget.setItem(1, 1, item)
        table_widget.setItem(1, 2, price)

    def create_menu_buttons(self, button_num):
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(button_num.sizePolicy().hasHeightForWidth())
        button_num.setSizePolicy(sizePolicy)
        button_num.setObjectName(str(button_num))

    def create_nav_buttons(self, button_name):
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(button_name.sizePolicy().hasHeightForWidth())
        button_name.setSizePolicy(sizePolicy)

        font = QFont()
        font.setPointSize(24)

        button_name.setFont(font)
        button_name.setObjectName(str(button_name))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = OrderWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

