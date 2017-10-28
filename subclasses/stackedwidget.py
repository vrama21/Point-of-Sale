from PyQt5.QtWidgets import QStackedWidget, QMainWindow


class StackedWidget(QStackedWidget):
    def __init__(self, parent=None):
        QStackedWidget.__init__(self, parent)

    def setCurrentIndex(self, index):
        self.window = QMainWindow(self.currentWidget(), self.widget(index))
        QStackedWidget.setCurrentIndex(self, index)

    def page0(self):
        # Home Page
        self.setCurrentIndex(0)

    def page1(self):
        # Order Page
        self.setCurrentIndex(1)