# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from email_window import Ui_email_window
from message_window import Ui_Message_To_Be_send


class Ui_second_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(661, 352)
        MainWindow.setStyleSheet("background-color: rgb(229, 229, 229);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        #This contains the make email
        self.CREATEmails = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.open_window4())
        self.CREATEmails.setGeometry(QtCore.QRect(100, 100, 171, 131))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(220, 255, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 255, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 255, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 179, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(148, 186, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 255, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 255, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 255, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 179, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(148, 186, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 255, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 255, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 255, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(148, 186, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        self.CREATEmails.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(9)
        self.CREATEmails.setFont(font)
        self.CREATEmails.setStyleSheet("background-color: rgb(220,255, 250);")
        self.CREATEmails.setObjectName("CREATEmails")
        self.viewMAILS = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.open_window3())
        self.viewMAILS.setGeometry(QtCore.QRect(360, 100, 181, 131))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(9)
        self.viewMAILS.setFont(font)
        self.viewMAILS.setStyleSheet("background-color: rgb(242, 250, 209);\n"
"")
        self.viewMAILS.setObjectName("viewMAILS")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 661, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Email"))
        self.CREATEmails.setText(_translate("MainWindow", "Create New mails"))
        self.viewMAILS.setText(_translate("MainWindow", "view mails "))

    def open_window3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_email_window()
        self.ui.sent_window(self.setpassword(self.email,self.password))
        self.ui.setupUi(self.window)
        self.window.show()

    def open_window4(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Message_To_Be_send()
        self.ui.setupUi(self.window)
        self.window.show()


    def setpassword(self,email,password):
        self.email=email
        self.password=password
        return ([email,password])



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_second_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
