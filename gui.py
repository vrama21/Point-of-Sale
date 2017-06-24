# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Programming\Point of Sale\Design\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


# from .functions import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        """ Stack all the widgets on top of one another """
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        """ Sets Home Page as Main Window """
        home_widget = HomeWidget(self)
        home_widget.button.clicked.connect(self.new_order_widget)
        self.central_widget.addWidget(home_widget)

        """ Sets Customer Entry as Main Window """
        customer_widget = HomeWidget(self)
        customer_widget.button.clicked.connect(self.customer_widget)
        self.central_widget.addWidget(customer_widget)

    """ New Order Widget to the top of the Stack """
    def new_order_widget(self):
        logged_in_widget = OrderWindowWidget(self)
        self.central_widget.addWidget(logged_in_widget)
        self.central_widget.setCurrentWidget(logged_in_widget)

    """ Customer Entry Widget to the top of the Stack """
    def customer_entry_widget(self):
        logged_in_widget = CustomerEntryWidget(self)
        self.central_widget.addWidget(logged_in_widget)
        self.central_widget.setCurrentWidget(logged_in_widget)


class HomeWidget(QWidget):
    def __init__(self, parent=None):
        super(HomeWidget, self).__init__(parent)
        layout = QHBoxLayout()
        self.button = QPushButton('New Order')
        self.button1 = QPushButton('Customer Entry')
        layout.addWidget(self.button)
        layout.addWidget(self.button1)
        self.setLayout(layout)


class OrderWindowWidget(QWidget):

    def __init__(self, parent=QMainWindow):
        super().__init__(parent)

        self.initUI(self)

    def initUI(self, MainWindow):
        self.resize(1024, 768)
        self.setMinimumSize(QSize(1024, 768))
        self.setMaximumSize(QSize(1024, 768))
        self.setWindowTitle("Swayblade's POS")

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

        self.btn01.setText("Category 1")
        self.btn02.setText("Category 2")
        self.btn03.setText("Category 3")
        self.btn04.setText("Category 4")
        self.btn05.setText("Category 5")
        self.btn06.setText("Category 6")
        self.btn07.setText("Category 7")
        self.btn08.setText("Category 8")
        self.btn09.setText("Category 9")
        self.btn10.setText("Category 10")
        self.btn11.setText("Category 11")
        self.btn12.setText("Category 12")
        self.btn13.setText("Category 13")
        self.btn14.setText("Category 14")
        self.btn15.setText("Category 15")
        self.btn16.setText("Category 16")
        self.btn17.setText("Category 17")
        self.btn18.setText("Category 18")
        self.btn19.setText("Category 19")
        self.btn20.setText("Category 20")
        self.btn21.setText("Category 21")
        self.btn22.setText("Category 22")
        self.btn23.setText("Category 23")
        self.btn24.setText("Category 24")
        self.btn25.setText("Category 25")

        """ Table """
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 50)

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Quantity")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("Items")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("Price")


        """ Navigation Buttons """

        self.btn_back = QPushButton(self.nav_bar)
        self.create_nav_buttons(self.btn_back)
        self.Navigation_Bar.addWidget(self.btn_back)
        # self.btn_back.clicked.connect((self.closeDialog()))

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
        # MainWindow.setCentralWidget(self.main_frame)

        self.btn_back.setText("Back")
        self.btnQty.setText("Quantity")
        self.pushButton_2.setText("1")
        self.pushButton_5.setText("2")
        self.btnNext.setText("Next")

        # self.menuBar = QMenuBar(MainWindow)
        # self.menuBar.setGeometry(QRect(0, 0, 1024, 21))
        # self.menuBar.setObjectName("menuBar")
        # MainWindow.setMenuBar(self.menuBar)

        # self.mainToolBar = QToolBar(MainWindow)
        # self.mainToolBar.setObjectName("mainToolBar")
        # MainWindow.addToolBar(QtWidget.ToolBarArea, self.mainToolBar)

        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        # MainWindow.setStatusBar(self.statusBar)

        QMetaObject.connectSlotsByName(MainWindow)

        self.show()


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

    def closeEvent(self, event):
        choice = QMessageBox.question(self, 'Alert!',
                                      "Are you sure you want to close the program?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Closing Application")
            event.accept()
        if choice == QMessageBox.No:
            event.ignore()

    def closeDialog(self):

        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.le.setText(str(text))
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class CustomerEntryWidget(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1208, 734)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget.setGeometry(QtCore.QRect(70, 160, 591, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setKerning(False)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(500)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.comboBox = QtWidgets.QComboBox(self.centralWidget)
        self.comboBox.setGeometry(QtCore.QRect(840, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        firstnameitem = self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 580, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(890, 580, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(770, 90, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralWidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(70, 100, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        self.tableWidget_3.horizontalHeader().setVisible(False)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(500)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(100)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralWidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(210, 430, 172, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.tableWidget_2.raise_()
        self.tableWidget.raise_()
        self.comboBox.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.tableWidget_3.raise_()
        self.commandLinkButton.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1208, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "First Name"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Last Name"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Address 1"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Address 2"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "City"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Zip Code"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Default"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Residence"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Business"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Hotel"))
        self.comboBox.setItemText(4, _translate("MainWindow", "School"))
        self.pushButton.setText(_translate("MainWindow", "Back"))
        self.pushButton_2.setText(_translate("MainWindow", "Next"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Presets:"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Phone"))
        self.commandLinkButton.setWhatsThis(_translate("MainWindow", "test"))
        self.commandLinkButton.setText(_translate("MainWindow", "CommandLinkButton"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

