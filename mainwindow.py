from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from gui.orderwindow import OrderWindow
from gui.homepage import HomePage
from gui.ticketview import TicketView
from gui.customerentrygui import CustomerEntry
from gui.menuedit import MenuEdit
from subclasses.stackedwidget import StackedWidget


class MainWindow(QMainWindow):

    trigger = pyqtSignal()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setMinimumSize(1024, 768)
        self.setMaximumSize(1024, 768)
        self.setWindowTitle("Swayblade's POS")

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        home = HomePage()
        home.Button_1.clicked.connect(self.order_window)
        home.Button_2.clicked.connect(self.customer_entry)
        home.Button_3.clicked.connect(self.ticket_view)
        home.Button_4.clicked.connect(self.next_page)

        order_window = OrderWindow()
        order_window.btn_back.clicked.connect(self.prev_page)
        order_window.btn_next.clicked.connect(self.next_page)

        customer_entry = CustomerEntry()
        customer_entry.btn_back.clicked.connect(self.prev_page)
        customer_entry.btn_next.clicked.connect(self.next_page)

        ticket_view = TicketView()
        ticket_view.btn_back.clicked.connect(self.prev_page)
        ticket_view.btn_next.clicked.connect(self.next_page)

        # All Pages are in a Stacked Widget
        self.stacked_widget.addWidget(home)             #0
        self.stacked_widget.addWidget(order_window)     #1
        self.stacked_widget.addWidget(ticket_view)      #2
        self.stacked_widget.addWidget(customer_entry)   #3

        self.home_page()

    def prev_page(self):
        index = self.stacked_widget.currentIndex()
        self.stacked_widget.setCurrentIndex(index - 1)

    def next_page(self):
        index = self.stacked_widget.currentIndex()
        # Checks if at the``1q last page of index
        if index < self.stacked_widget.count() - 1:
            self.stacked_widget.setCurrentIndex(index + 1)
        # Else it returns back to home page
        else:
            self.stacked_widget.setCurrentIndex(0)

    def home_page(self):
        self.stacked_widget.setCurrentIndex(0)
        self.widget_log()

    def order_window(self):
        self.stacked_widget.setCurrentIndex(1)
        self.widget_log()

    def ticket_view(self):
        self.stacked_widget.setCurrentIndex(2)
        self.widget_log()

    def customer_entry(self):
        self.stacked_widget.setCurrentIndex(3)
        self.widget_log()
        
    def page_to_stack(self, index):
        self.stacked_widget.setCurrentIndex(index)
        self.widget_log()
        

    def widget_log(self):
        print('Current Index:', self.stacked_widget.currentIndex())
        print('Current Widget:', self.stacked_widget.currentWidget())

    def close_event(self, event):
        choice = QMessageBox.question(self, 'Alert!',
                                      "Are you sure you want to close the program?",
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Closing Application")
            event.accept()
        if choice == QMessageBox.No:
            event.ignore()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
