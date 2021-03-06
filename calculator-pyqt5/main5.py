# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(560, 435)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(560, 435))
        MainWindow.setMaximumSize(QtCore.QSize(560, 435))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("calculator_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.button_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_7.setObjectName("button_7")
        self.gridLayout.addWidget(self.button_7, 2, 0, 1, 1)
        self.button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.button_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_9.setObjectName("button_9")
        self.gridLayout.addWidget(self.button_9, 2, 2, 1, 1)
        self.button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_3.setObjectName("button_3")
        self.gridLayout.addWidget(self.button_3, 6, 2, 1, 1)
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_1.setObjectName("button_1")
        self.gridLayout.addWidget(self.button_1, 6, 0, 1, 1)
        self.parenthesis_close = QtWidgets.QPushButton(self.centralwidget)
        self.parenthesis_close.setFocusPolicy(QtCore.Qt.NoFocus)
        self.parenthesis_close.setObjectName("parenthesis_close")
        self.gridLayout.addWidget(self.parenthesis_close, 4, 5, 1, 1)
        self.button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.button_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_8.setObjectName("button_8")
        self.gridLayout.addWidget(self.button_8, 2, 1, 1, 1)
        self.divide = QtWidgets.QPushButton(self.centralwidget)
        self.divide.setFocusPolicy(QtCore.Qt.NoFocus)
        self.divide.setObjectName("divide")
        self.gridLayout.addWidget(self.divide, 2, 3, 1, 1)
        self.button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.button_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_6.setObjectName("button_6")
        self.gridLayout.addWidget(self.button_6, 4, 2, 1, 1)
        self.add = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add.sizePolicy().hasHeightForWidth())
        self.add.setSizePolicy(sizePolicy)
        self.add.setFocusPolicy(QtCore.Qt.NoFocus)
        self.add.setObjectName("add")
        self.gridLayout.addWidget(self.add, 6, 3, 2, 1)
        self.remainder = QtWidgets.QPushButton(self.centralwidget)
        self.remainder.setFocusPolicy(QtCore.Qt.NoFocus)
        self.remainder.setObjectName("remainder")
        self.gridLayout.addWidget(self.remainder, 7, 2, 1, 1)
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_2.setObjectName("button_2")
        self.gridLayout.addWidget(self.button_2, 6, 1, 1, 1)
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.reset_button.setObjectName("reset_button")
        self.gridLayout.addWidget(self.reset_button, 2, 5, 1, 1)
        self.decimal = QtWidgets.QPushButton(self.centralwidget)
        self.decimal.setFocusPolicy(QtCore.Qt.NoFocus)
        self.decimal.setObjectName("decimal")
        self.gridLayout.addWidget(self.decimal, 7, 1, 1, 1)
        self.equals = QtWidgets.QPushButton(self.centralwidget)
        self.equals.setFocusPolicy(QtCore.Qt.NoFocus)
        self.equals.setObjectName("equals")
        self.gridLayout.addWidget(self.equals, 7, 4, 1, 2)
        self.button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.button_0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_0.setObjectName("button_0")
        self.gridLayout.addWidget(self.button_0, 7, 0, 1, 1)
        self.square_root = QtWidgets.QPushButton(self.centralwidget)
        self.square_root.setFocusPolicy(QtCore.Qt.NoFocus)
        self.square_root.setObjectName("square_root")
        self.gridLayout.addWidget(self.square_root, 6, 5, 1, 1)
        self.button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.button_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_4.setObjectName("button_4")
        self.gridLayout.addWidget(self.button_4, 4, 0, 1, 1)
        self.parenthesis_open = QtWidgets.QPushButton(self.centralwidget)
        self.parenthesis_open.setFocusPolicy(QtCore.Qt.NoFocus)
        self.parenthesis_open.setObjectName("parenthesis_open")
        self.gridLayout.addWidget(self.parenthesis_open, 4, 4, 1, 1)
        self.button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.button_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_5.setObjectName("button_5")
        self.gridLayout.addWidget(self.button_5, 4, 1, 1, 1)
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setFocusPolicy(QtCore.Qt.NoFocus)
        self.minus.setObjectName("minus")
        self.gridLayout.addWidget(self.minus, 6, 4, 1, 1)
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_button.setObjectName("clear_button")
        self.gridLayout.addWidget(self.clear_button, 2, 4, 1, 1)
        self.multiply = QtWidgets.QPushButton(self.centralwidget)
        self.multiply.setFocusPolicy(QtCore.Qt.NoFocus)
        self.multiply.setObjectName("multiply")
        self.gridLayout.addWidget(self.multiply, 4, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 6)
        self.output_window = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_window.sizePolicy().hasHeightForWidth())
        self.output_window.setSizePolicy(sizePolicy)
        self.output_window.setFocusPolicy(QtCore.Qt.NoFocus)
        self.output_window.setObjectName("output_window")
        self.gridLayout.addWidget(self.output_window, 0, 0, 1, 6)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.parenthesis_close.setText(_translate("MainWindow", ")"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.divide.setText(_translate("MainWindow", "/"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.add.setText(_translate("MainWindow", "+"))
        self.remainder.setText(_translate("MainWindow", "%"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.reset_button.setText(_translate("MainWindow", "AC"))
        self.decimal.setText(_translate("MainWindow", "."))
        self.equals.setText(_translate("MainWindow", "="))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.square_root.setText(_translate("MainWindow", "√"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.parenthesis_open.setText(_translate("MainWindow", "("))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.clear_button.setText(_translate("MainWindow", "CLR"))
        self.multiply.setText(_translate("MainWindow", "*"))

#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

