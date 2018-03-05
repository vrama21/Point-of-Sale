from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from gui.orderwindow import OrderWindow


class OrderWindowController:

    def __init__(self):
        order_window = OrderWindow
        btn01 = order_window.btn01()
        btn01.clicked.connect(self.insert_item)

    def insert_item(self, qty, item, price):
        table_widget = self.order_window.tableWidget
        table_widget.setItem(1, 0, qty)
        table_widget.setItem(1, 1, item)
        table_widget.setItem(1, 2, price)




