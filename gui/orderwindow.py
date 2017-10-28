from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class OrderWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # MainWindow.central_widget.addWidget(self)
        # MainWindow.central_widget.setCentralWidget(self)

        self.init_ui()

    def init_ui(self):
        """ Frame Layouts"""
        self.main_frame = QWidget(self)

        self.menu_grid = QWidget(self.main_frame)
        self.menu_grid.setGeometry(QRect(310, 0, 700, 625))

        self.nav_bar = QWidget(self.main_frame)
        self.nav_bar.setGeometry(QRect(0, 615, 1015, 131))

        self.Navigation_Bar = QHBoxLayout(self.nav_bar)
        self.Navigation_Bar.setContentsMargins(10, 10, 10, 10)
        self.Navigation_Bar.setSpacing(0)

        self.Menu_Buttons = QGridLayout(self.menu_grid)
        self.Menu_Buttons.setSizeConstraint(QLayout.SetMinimumSize)
        self.Menu_Buttons.setContentsMargins(10, 10, 10, 10)
        self.Menu_Buttons.setSpacing(0)

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

        """ Navigation Buttons """

        self.btn_back = QPushButton(self.nav_bar)
        self.create_nav_buttons(self.btn_back)
        self.Navigation_Bar.addWidget(self.btn_back)
        # self.btn_back.clicked.connect(self.back_button)

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
        # mainwindow.Window.setCentralWidget(self.main_frame)

        self.btn_back.setText("Back")
        self.btnQty.setText("Quantity")
        self.pushButton_2.setText("1")
        self.pushButton_5.setText("2")
        self.btnNext.setText("Next")

        # self.btn01.clicked.connect(self.add_item(1, "Test", 9.99))


        """ Table """

        self.tableWidget = QTableWidget(self.main_frame)
        ticket_table = self.tableWidget
        ticket_table.setGeometry(QRect(10, 10, 305, 600))
        ticket_table.setShowGrid(True)
        ticket_table.setColumnCount(3)
        ticket_table.setRowCount(19)
        ticket_table.setEditTriggers(QTableWidget.NoEditTriggers)  # Disable text input into table
        ticket_table.verticalHeader().setVisible(False)

        item1 = QTableWidgetItem()
        item2 = QTableWidgetItem()
        item3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item1)
        self.tableWidget.setHorizontalHeaderItem(1, item2)
        self.tableWidget.setHorizontalHeaderItem(2, item3)

        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        header1 = self.tableWidget.horizontalHeaderItem(0)
        header2 = self.tableWidget.horizontalHeaderItem(1)
        header3 = self.tableWidget.horizontalHeaderItem(2)
        header1.setText("Qty")
        header2.setText("Items")
        header3.setText("Price")
        # table.ResizeDelegate(ticket_table, header1)
        # QHeaderView.setSectionResizeMode(QHeaderView.setSectionResizeMode(fixed))


    @pyqtSlot()
    def add_item(self, qty, item, price):
        table_widget = self.tableWidget
        table_widget.setItem(1, 0, qty)
        table_widget.setItem(1, 1, item)
        table_widget.setItem(1, 2, price)

    def menu_event(self, event):
        menu = QMenu(self)
        editAction = menu.addAction("Edit")
        action = menu.exec_(self.mapToGlobal(event.pos()))

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

    def table(self):
        layout = QGridLayout()
        self.led = QLineEdit("Sample")
        self.table = QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(5)
        layout.addWidget(self.led, 0, 0)
        layout.addWidget(self.table, 1, 0)
        self.table.setItem(1, 0, QTableWidgetItem(self.led.text()))