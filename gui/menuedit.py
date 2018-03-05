from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MenuEdit(QWidget):
    def __init__(self, parent=None):
        super(MenuEdit, self).__init__(parent)
        self.init_ui(self)

    def init_ui(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(598, 259)
        self.label = QLabel(Widget)
        self.label.setGeometry(QRect(250, 0, 101, 31))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QPushButton(Widget)
        self.pushButton.setGeometry(QRect(10, 40, 161, 171))
        font = QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setGeometry(QRect(190, 60, 251, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QLabel(Widget)
        self.label_2.setGeometry(QRect(180, 40, 111, 21))
        font = QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(Widget)
        self.label_3.setGeometry(QRect(180, 100, 111, 21))
        font = QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QLineEdit(Widget)
        self.lineEdit_2.setGeometry(QRect(190, 130, 251, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setGeometry(QRect(480, 200, 111, 51))
        font = QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QLineEdit(Widget)
        self.lineEdit_3.setGeometry(QRect(190, 200, 111, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QLabel(Widget)
        self.label_4.setGeometry(QRect(160, 180, 111, 21))
        font = QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Widget)
        QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.label.setText(_translate("Widget", "Button 1"))
        self.pushButton.setText(_translate("Widget", "Image"))
        self.label_2.setText(_translate("Widget", "Button Text"))
        self.label_3.setText(_translate("Widget", "Ticket Text"))
        self.pushButton_2.setText(_translate("Widget", "Finished"))
        self.label_4.setText(_translate("Widget", "Price"))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MenuEdit()
    window.show()
    sys.exit(app.exec_())