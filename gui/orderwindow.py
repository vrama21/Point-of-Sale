from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class OrderWindow(QWidget):
    def __init__(self, parent=None):
        super(OrderWindow, self).__init__(parent)

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
        self.add_button('btn01', 'Category 01', self.menu_grid, 0, 0)
        self.add_button('btn02', 'Category 02', self.menu_grid, 0, 1)
        self.add_button('btn03', 'Category 03', self.menu_grid, 0, 2)
        self.add_button('btn04', 'Category 04', self.menu_grid, 0, 3)
        self.add_button('btn05', 'Category 05', self.menu_grid, 0, 4)
        self.add_button('btn06', 'Category 06', self.menu_grid, 1, 0)
        self.add_button('btn07', 'Category 07', self.menu_grid, 1, 1)
        self.add_button('btn08', 'Category 08', self.menu_grid, 1, 2)
        self.add_button('btn09', 'Category 09', self.menu_grid, 1, 3)
        self.add_button('btn10', 'Category 10', self.menu_grid, 1, 4)
        self.add_button('btn11', 'Category 11', self.menu_grid, 2, 0)
        self.add_button('btn12', 'Category 12', self.menu_grid, 2, 1)
        self.add_button('btn13', 'Category 13', self.menu_grid, 2, 2)
        self.add_button('btn14', 'Category 14', self.menu_grid, 2, 3)
        self.add_button('btn15', 'Category 15', self.menu_grid, 2, 4)
        self.add_button('btn16', 'Category 16', self.menu_grid, 3, 0)
        self.add_button('btn17', 'Category 17', self.menu_grid, 3, 1)
        self.add_button('btn18', 'Category 18', self.menu_grid, 3, 2)
        self.add_button('btn19', 'Category 19', self.menu_grid, 3, 3)
        self.add_button('btn20', 'Category 20', self.menu_grid, 3, 4)
        self.add_button('btn21', 'Category 21', self.menu_grid, 4, 0)
        self.add_button('btn22', 'Category 22', self.menu_grid, 4, 1)
        self.add_button('btn23', 'Category 23', self.menu_grid, 4, 2)
        self.add_button('btn24', 'Category 24', self.menu_grid, 4, 3)
        self.add_button('btn25', 'Category 25', self.menu_grid, 4, 4)

        """ Navigation Buttons """

        self.btn_back = QPushButton(self.nav_bar)
        self.create_nav_buttons(self.btn_back)
        self.Navigation_Bar.addWidget(self.btn_back)
        self.btn_back.setText("Back")

        self.btnQty = QPushButton(self.nav_bar)
        self.create_nav_buttons(self.btnQty)
        self.Navigation_Bar.addWidget(self.btnQty)
        self.btnQty.setText("Quantity")

        self.btn_next = QPushButton(self.nav_bar)
        self.create_nav_buttons(self.btn_next)
        self.Navigation_Bar.addWidget(self.btn_next)
        self.btn_next.setText("1")

        self.btn_back_5 = QPushButton(self.nav_bar)
        self.create_nav_buttons(self.btn_back_5)
        self.Navigation_Bar.addWidget(self.btn_back_5)
        self.btn_back_5.setText("2")

        self.btn_next = QPushButton(self.nav_bar)
        self.create_nav_buttons(self.btn_next)
        self.Navigation_Bar.addWidget(self.btn_next)
        self.btn_next.setText("Next")


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

        # self.table_iter()
        # self.btn01.clicked.connect(lambda: self.insert_item('1', 'Large Pizza', '12.00'))
        # self.btn01.clicked.connect(self.on_click)

    def add_button(self, name, text, widget, idx, idy):
        self.name = name
        self.name = QPushButton(widget)
        self.create_menu_buttons(self.name)
        self.Menu_Buttons.addWidget(self.name, idx, idy, 1, 1)
        self.name.setText(text)

    def on_click(self):
        print("Button has been clicked!")

    def row_iter(self):
        row = -1
        if self.on_click():
            rows = row + 1
            return rows

    def insert_item(self, qty, item, price):
        self.row_iter()
        table_widget = self.tableWidget
        table_widget.setItem(rows, 0, QTableWidgetItem(qty))
        table_widget.setItem(rows, 1, QTableWidgetItem(item))
        table_widget.setItem(rows, 2, QTableWidgetItem(price))
        # table_widget.setItem(0, 0, QTableWidgetItem(qty))
        # table_widget.setItem(0, 1, QTableWidgetItem(item))
        # table_widget.setItem(0, 2, QTableWidgetItem(price))

    def test(self):
        table_widget = self.tableWidget
        selection = table_widget.row(0)
        # if self.btn01.clicked() =True:

    # def table_iter(self):
    #     row = 0
    #     while self.on_click():
    #         rows = row + 1
    #     return rows
    #     print(rows)

        # for irow in range(self.tableWidget.rowCount()):
        #     row = []
        #     for icol in range(self.tableWidget.columnCount()):
        #         cell = self.tableWidget.commitData(self.tableWidget.create(irow, icol))
        #         row.append(cell)
        #     print(', '.join(str(c) for c in row))

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

        font = QFont("Ubuntu")
        font.setPointSize(14)
        button_num.setFont(font)

    def create_nav_buttons(self, button_name):
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(button_name.sizePolicy().hasHeightForWidth())
        button_name.setSizePolicy(sizePolicy)

        font = QFont("Ubuntu")
        font.setPointSize(24)
        button_name.setFont(font)

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


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = OrderWindow()
    window.show()
    sys.exit(app.exec_())