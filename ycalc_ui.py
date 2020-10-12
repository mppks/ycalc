# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ycalc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(233, 229)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.directionBox = QComboBox(self.centralwidget)
        self.directionBox.setObjectName(u"directionBox")

        self.horizontalLayout_7.addWidget(self.directionBox)

        self.currencyBox = QComboBox(self.centralwidget)
        self.currencyBox.setObjectName(u"currencyBox")

        self.horizontalLayout_7.addWidget(self.currencyBox)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.giveInput = QLineEdit(self.centralwidget)
        self.giveInput.setObjectName(u"giveInput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.giveInput.sizePolicy().hasHeightForWidth())
        self.giveInput.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.giveInput, 0, 1, 1, 1)

        self.commissionCurLabel = QLabel(self.centralwidget)
        self.commissionCurLabel.setObjectName(u"commissionCurLabel")
        sizePolicy.setHeightForWidth(self.commissionCurLabel.sizePolicy().hasHeightForWidth())
        self.commissionCurLabel.setSizePolicy(sizePolicy)
        self.commissionCurLabel.setScaledContents(False)

        self.gridLayout.addWidget(self.commissionCurLabel, 1, 2, 1, 1)

        self.giveCurLabel = QLabel(self.centralwidget)
        self.giveCurLabel.setObjectName(u"giveCurLabel")

        self.gridLayout.addWidget(self.giveCurLabel, 0, 2, 1, 1)

        self.receiveCurLabel = QLabel(self.centralwidget)
        self.receiveCurLabel.setObjectName(u"receiveCurLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.receiveCurLabel.sizePolicy().hasHeightForWidth())
        self.receiveCurLabel.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.receiveCurLabel, 5, 2, 1, 1)

        self.netLabel = QLabel(self.centralwidget)
        self.netLabel.setObjectName(u"netLabel")

        self.gridLayout.addWidget(self.netLabel, 3, 0, 1, 1)

        self.commissionMoneyLabel = QLabel(self.centralwidget)
        self.commissionMoneyLabel.setObjectName(u"commissionMoneyLabel")

        self.gridLayout.addWidget(self.commissionMoneyLabel, 2, 0, 1, 1)

        self.commissionLabel = QLabel(self.centralwidget)
        self.commissionLabel.setObjectName(u"commissionLabel")

        self.gridLayout.addWidget(self.commissionLabel, 1, 0, 1, 1)

        self.rateInput = QLineEdit(self.centralwidget)
        self.rateInput.setObjectName(u"rateInput")

        self.gridLayout.addWidget(self.rateInput, 4, 1, 1, 1)

        self.netCurLabel = QLabel(self.centralwidget)
        self.netCurLabel.setObjectName(u"netCurLabel")

        self.gridLayout.addWidget(self.netCurLabel, 3, 2, 1, 1)

        self.receiveInput = QLineEdit(self.centralwidget)
        self.receiveInput.setObjectName(u"receiveInput")
        self.receiveInput.setStyleSheet(u"QLineEdit{ background-color: rgb(226, 226, 226) }")
        self.receiveInput.setReadOnly(True)

        self.gridLayout.addWidget(self.receiveInput, 5, 1, 1, 1)

        self.giveLabel = QLabel(self.centralwidget)
        self.giveLabel.setObjectName(u"giveLabel")

        self.gridLayout.addWidget(self.giveLabel, 0, 0, 1, 1)

        self.rateLabel = QLabel(self.centralwidget)
        self.rateLabel.setObjectName(u"rateLabel")

        self.gridLayout.addWidget(self.rateLabel, 4, 0, 1, 1)

        self.commissionMoneyCurLabel = QLabel(self.centralwidget)
        self.commissionMoneyCurLabel.setObjectName(u"commissionMoneyCurLabel")
        sizePolicy.setHeightForWidth(self.commissionMoneyCurLabel.sizePolicy().hasHeightForWidth())
        self.commissionMoneyCurLabel.setSizePolicy(sizePolicy)
        self.commissionMoneyCurLabel.setScaledContents(False)

        self.gridLayout.addWidget(self.commissionMoneyCurLabel, 2, 2, 1, 1)

        self.receiveLabel = QLabel(self.centralwidget)
        self.receiveLabel.setObjectName(u"receiveLabel")

        self.gridLayout.addWidget(self.receiveLabel, 5, 0, 1, 1)

        self.commissionInput = QLineEdit(self.centralwidget)
        self.commissionInput.setObjectName(u"commissionInput")
        sizePolicy1.setHeightForWidth(self.commissionInput.sizePolicy().hasHeightForWidth())
        self.commissionInput.setSizePolicy(sizePolicy1)
        self.commissionInput.setCursorPosition(3)

        self.gridLayout.addWidget(self.commissionInput, 1, 1, 1, 1)

        self.commissionMoneyInput = QLineEdit(self.centralwidget)
        self.commissionMoneyInput.setObjectName(u"commissionMoneyInput")
        sizePolicy1.setHeightForWidth(self.commissionMoneyInput.sizePolicy().hasHeightForWidth())
        self.commissionMoneyInput.setSizePolicy(sizePolicy1)
        self.commissionMoneyInput.setStyleSheet(u"QLineEdit{ background-color: rgb(226, 226, 226) }")
        self.commissionMoneyInput.setCursorPosition(10)
        self.commissionMoneyInput.setReadOnly(True)

        self.gridLayout.addWidget(self.commissionMoneyInput, 2, 1, 1, 1)

        self.rateCurLabel = QLabel(self.centralwidget)
        self.rateCurLabel.setObjectName(u"rateCurLabel")

        self.gridLayout.addWidget(self.rateCurLabel, 4, 2, 1, 1)

        self.netInput = QLineEdit(self.centralwidget)
        self.netInput.setObjectName(u"netInput")
        sizePolicy1.setHeightForWidth(self.netInput.sizePolicy().hasHeightForWidth())
        self.netInput.setSizePolicy(sizePolicy1)
        self.netInput.setStyleSheet(u"QLineEdit{ background-color: rgb(226, 226, 226) }\n"
"")
        self.netInput.setReadOnly(True)

        self.gridLayout.addWidget(self.netInput, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.refreshButton = QPushButton(self.centralwidget)
        self.refreshButton.setObjectName(u"refreshButton")

        self.horizontalLayout.addWidget(self.refreshButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440", None))
        self.giveInput.setInputMask("")
        self.giveInput.setText(QCoreApplication.translate("MainWindow", u"0.00000000", None))
        self.commissionCurLabel.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.giveCurLabel.setText(QCoreApplication.translate("MainWindow", u"usd", None))
        self.receiveCurLabel.setText(QCoreApplication.translate("MainWindow", u"btc", None))
        self.netLabel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u0430\u044e - \u041a\u043e\u043c.:", None))
        self.commissionMoneyLabel.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u0438\u0441\u0441\u0438\u044f:", None))
        self.commissionLabel.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u0438\u0441\u0441\u0438\u044f:", None))
        self.rateInput.setText(QCoreApplication.translate("MainWindow", u"0.00000000", None))
        self.netCurLabel.setText(QCoreApplication.translate("MainWindow", u"usd", None))
        self.receiveInput.setText(QCoreApplication.translate("MainWindow", u"0.00000000", None))
        self.giveLabel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u0430\u044e:", None))
        self.rateLabel.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0443\u0440\u0441:", None))
        self.commissionMoneyCurLabel.setText(QCoreApplication.translate("MainWindow", u"usd", None))
        self.receiveLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0430\u044e:", None))
        self.commissionInput.setInputMask("")
        self.commissionInput.setText(QCoreApplication.translate("MainWindow", u"0.2", None))
        self.commissionMoneyInput.setInputMask("")
        self.commissionMoneyInput.setText(QCoreApplication.translate("MainWindow", u"0.00000000", None))
        self.rateCurLabel.setText(QCoreApplication.translate("MainWindow", u"usd", None))
        self.netInput.setText(QCoreApplication.translate("MainWindow", u"0.00000000", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u043a\u0443\u0440\u0441", None))
    # retranslateUi

