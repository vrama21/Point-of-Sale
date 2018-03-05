from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class TicketView(QWidget):
    def __init__(self, parent=None):
        super(TicketView, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, TicketView):
        self.nav_bar = QWidget(self)
        self.nav_bar.setGeometry(QRect(0, 615, 1015, 131))
        self.Navigation_Bar = QHBoxLayout(self.nav_bar)
        self.btn_back = QPushButton(self.nav_bar)
        self.btn_next = QPushButton(self.nav_bar)
        self.btn_back.setText('Back')
        self.btn_next.setText('Next')
        self.Navigation_Bar.addWidget(self.btn_back)
        self.Navigation_Bar.addWidget(self.btn_next)

        self.gridLayoutWidget = QWidget(self)
        self.gridLayoutWidget.setGeometry(QRect(50, 60, 921, 500))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(0)
        self.tableWidget_4 = QTableWidget(self.gridLayoutWidget)
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_4, 2, 1, 1, 1)
        self.tableWidget_8 = QTableWidget(self.gridLayoutWidget)
        self.tableWidget_8.setColumnCount(0)
        self.tableWidget_8.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_8, 9, 1, 1, 1)
        self.tableWidget = QTableWidget(self.gridLayoutWidget)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 8, 1, 1, 1)
        self.tableWidget_3 = QTableWidget(self.gridLayoutWidget)
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_3, 3, 1, 1, 1)
        self.tableWidget_5 = QTableWidget(self.gridLayoutWidget)
        self.tableWidget_5.setColumnCount(0)
        self.tableWidget_5.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_5, 4, 1, 1, 1)
        self.tableWidget_2 = QTableWidget(self.gridLayoutWidget)
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_2, 7, 1, 1, 1)
        self.tableWidget_6 = QTableWidget(self.gridLayoutWidget)
        self.tableWidget_6.setColumnCount(0)
        self.tableWidget_6.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_6, 5, 1, 1, 1)
        self.tableWidget_9 = QTableWidget(self.gridLayoutWidget)
        self.tableWidget_9.setColumnCount(0)
        self.tableWidget_9.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_9, 11, 1, 1, 1)
        self.tableWidget_7 = QTableWidget(self.gridLayoutWidget)
        self.tableWidget_7.setColumnCount(0)
        self.tableWidget_7.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_7, 6, 1, 1, 1)
        self.tableWidget_11 = QTableWidget(self.gridLayoutWidget)
        self.tableWidget_11.setColumnCount(0)
        self.tableWidget_11.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_11, 12, 1, 1, 1)
        self.TableHeader = QTableWidget(self)
        self.TableHeader.setEnabled(True)
        self.TableHeader.setGeometry(QRect(50, 30, 920, 31))



        font = QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.TableHeader.setFont(font)
        self.TableHeader.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.TableHeader.setShowGrid(True)
        self.TableHeader.setWordWrap(True)
        self.TableHeader.setCornerButtonEnabled(True)
        self.TableHeader.setObjectName("TableHeader")
        self.TableHeader.setColumnCount(9)
        self.TableHeader.setRowCount(0)
        item = QTableWidgetItem()
        self.TableHeader.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.TableHeader.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.TableHeader.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.TableHeader.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.TableHeader.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()
        self.TableHeader.setHorizontalHeaderItem(5, item)
        item = QTableWidgetItem()
        self.TableHeader.setHorizontalHeaderItem(6, item)
        item = QTableWidgetItem()
        self.TableHeader.setHorizontalHeaderItem(7, item)
        item = QTableWidgetItem()
        self.TableHeader.setHorizontalHeaderItem(8, item)
        self.TableHeader.horizontalHeader().setVisible(True)
        self.TableHeader.horizontalHeader().setCascadingSectionResizes(False)
        self.TableHeader.horizontalHeader().setDefaultSectionSize(100)
        self.TableHeader.horizontalHeader().setHighlightSections(True)
        self.TableHeader.horizontalHeader().setMinimumSectionSize(55)
        self.TableHeader.horizontalHeader().setSortIndicatorShown(False)
        self.TableHeader.horizontalHeader().setStretchLastSection(True)
        self.TableHeader.verticalHeader().setVisible(False)
        self.TableHeader.verticalHeader().setCascadingSectionResizes(False)
        self.TableHeader.verticalHeader().setMinimumSectionSize(0)

        _translate = QCoreApplication.translate
        item = self.TableHeader.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Ticket"))
        item = self.TableHeader.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Time"))
        item = self.TableHeader.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Order By"))
        item = self.TableHeader.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Status"))
        item = self.TableHeader.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Type"))
        item = self.TableHeader.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Total"))
        item = self.TableHeader.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Location"))
        item = self.TableHeader.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Elapsed"))
        item = self.TableHeader.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Driver"))


