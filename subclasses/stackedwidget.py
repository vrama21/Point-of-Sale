from PyQt5.QtWidgets import QStackedWidget, QMainWindow


class StackedWidget(QStackedWidget):
    def __init__(self, parent=None):
        # Inherits base class of QStackedWidget
        QStackedWidget.__init__(self, parent)

    def setCurrentIndex(self, index):
        self.window = QMainWindow(self.currentWidget(), self.widget(index))
        QStackedWidget.setCurrentIndex(self, index)

    def set_connections(self):
        # Clicked Connections for Buttons
        self.ui.pushButton.clicked.connect()
        self.stacked.pushButton_2.clicked.connect(self.stacked_widget.setCurrentIndex(1))

    # def page0(self):
    #     # Home Page
    #     self.setCurrentIndex(0)
    #
    # def page1(self):
    #     # Order Page
    #     self.setCurrentIndex(1)

