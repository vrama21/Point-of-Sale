from PyQt5.QtWidgets import *

from gui.homepage import HomePage
from gui.customerentrygui import CustomerEntry
from gui.orderwindow import OrderWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setMinimumSize(1024, 768)
        self.setMaximumSize(1024, 768)
        self.setWindowTitle("Swayblade's POS")

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.home()

    def home(self):
        home_page_widget = HomePage(self)
        self.stacked_widget.addWidget(home_page_widget)
        self.stacked_widget.setCurrentWidget(home_page_widget)

        home_page_widget.Button_1.clicked.connect(self.order_window)
        home_page_widget.Button_2.clicked.connect(self.customer_entry)

    def customer_entry(self):
        customer_entry_widget = CustomerEntry(self)
        self.stacked_widget.addWidget(customer_entry_widget)
        self.stacked_widget.setCurrentWidget(customer_entry_widget)

    def order_window(self):
        order_window_widget = OrderWindow(self)
        self.stacked_widget.addWidget(order_window_widget)
        self.stacked_widget.setCurrentWidget(order_window_widget)

    # def set_connections(self):
        # Clicked Connections for Buttons
        # self.ui.pushButton.clicked.connect()
        # self.stacked.pushButton_2.clicked.connect(self.stacked_widget.setCurrentIndex(1))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
