# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jaavUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jaavUI(object):
    def setupUi(self, jaavUI):
        jaavUI.setObjectName("jaavUI")
        jaavUI.resize(1365, 762)
        self.centralwidget = QtWidgets.QWidget(jaavUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1361, 761))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(5, 1, 23);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\\Users\\USER\\Desktop\\atlas\\aed11d6975231b91c8e992c02b8376da.gif"))
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 560, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1080, 560, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 530, 761, 101))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(72)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(216, 215, 222);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        jaavUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(jaavUI)
        QtCore.QMetaObject.connectSlotsByName(jaavUI)

    def retranslateUi(self, jaavUI):
        _translate = QtCore.QCoreApplication.translate
        jaavUI.setWindowTitle(_translate("jaavUI", "JAAV,A Virtual Assistant"))
        self.pushButton.setText(_translate("jaavUI", "RUN"))
        self.pushButton_2.setText(_translate("jaavUI", "EXIT"))
        self.label_2.setText(_translate("jaavUI", "J . A . A . V"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jaavUI = QtWidgets.QMainWindow()
    ui = Ui_jaavUI()
    ui.setupUi(jaavUI)
    jaavUI.show()
    sys.exit(app.exec_())
