# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helpme.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_helpme(object):
    def setupUi(self, helpme):
        helpme.setObjectName("helpme")
        helpme.resize(600, 435)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(helpme.sizePolicy().hasHeightForWidth())
        helpme.setSizePolicy(sizePolicy)
        helpme.setMinimumSize(QtCore.QSize(600, 435))
        helpme.setMaximumSize(QtCore.QSize(600, 435))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(12)
        helpme.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        helpme.setWindowIcon(icon)
        helpme.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(helpme)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.help_label = QtWidgets.QLabel(helpme)
        font = QtGui.QFont()
        font.setFamily("Hack")
        self.help_label.setFont(font)
        self.help_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.help_label.setWordWrap(True)
        self.help_label.setObjectName("help_label")
        self.verticalLayout.addWidget(self.help_label)

        self.retranslateUi(helpme)
        QtCore.QMetaObject.connectSlotsByName(helpme)

    def retranslateUi(self, helpme):
        _translate = QtCore.QCoreApplication.translate
        helpme.setWindowTitle(_translate("helpme", "Помощь"))
        self.help_label.setText(_translate("helpme", "<html><head/><body><p align=\"center\">Помощь:</p><p align=\"justify\">1. В случае с +, -, * и / программа работает по принципу:<br/>[первое число] [дейстивие] [второе число]<br/><br/>2. В случае ^ программа работает по принципу:<br/>[первое число] в степени [второе число]<br/><br/>3. В случае √ программа работает по принципу:<br/>корень в степени[второе число] от [первое число]<br/><br/>4. В случае НОД программа ищет наибольший общий делитель.<br/></p><p align=\"justify\">5. В случае ОСТ программа ищет остаток от деление первого числа на второе число.</p></body></html>"))
