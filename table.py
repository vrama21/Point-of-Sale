from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import gui

class Table(QTableWidget):
    def __init__(self, parent=gui.OrderWindowWidget):
        super().__init__(parent)
        self.tableWidget = QTableWidget(gui.OrderWindowWidget.main_frame)
        ticket_table = self.tableWidget
        ticket_table.setGeometry(QRect(10, 10, 305, 600))
        ticket_table.setShowGrid(True)
        ticket_table.setObjectName("Ticket_Table")
        ticket_table.setColumnCount(3)
        ticket_table.setRowCount(15)
        ticket_table.setEditTriggers(QTableWidget.NoEditTriggers)  # Disable text input into table
        ticket_table.verticalHeader().setVisible(False)

        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        # item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        # item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 50)

        header1 = self.tableWidget.horizontalHeaderItem(0)
        header2 = self.tableWidget.horizontalHeaderItem(1)
        header3 = self.tableWidget.horizontalHeaderItem(2)
        header1.setText("Quantity")
        header2.setText("Items")
        header3.setText("Price")


class ResizeDelegate(QStyledItemDelegate):

    def __init__(self, table, stretch_column, *args, **kwargs):
        super(ResizeDelegate, self).__init__(*args, **kwargs)
        self.table = table
        self.stretch_column = stretch_column

    def sizeHint(self, option, index):
        size = super(ResizeDelegate, self).sizeHint(option, index)
        if index.column() == self.stretch_column:
            total_width = self.table.viewport().size().width()
            calc_width = size.width()
            for i in range(self.table.columnCount()):
                if i != index.column():
                    option_ = QStyleOptionViewItem()
                    index_ = self.table.model().index(index.row(), i)
                    self.initStyleOption(option_, index_)
                    size_ = self.sizeHint(option_, index_)
                    calc_width += size_.width()
            if calc_width < total_width:
                size.setWidth(size.width() + total_width - calc_width)
        return size
