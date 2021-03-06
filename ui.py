# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 500)
        MainWindow.setMinimumSize(QtCore.QSize(422, 500))
        MainWindow.setMaximumSize(QtCore.QSize(422, 520))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\ui\\../img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.subtraction = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(94)
        sizePolicy.setVerticalStretch(28)
        sizePolicy.setHeightForWidth(self.subtraction.sizePolicy().hasHeightForWidth())
        self.subtraction.setSizePolicy(sizePolicy)
        self.subtraction.setMinimumSize(QtCore.QSize(94, 28))
        self.subtraction.setObjectName("subtraction")
        self.horizontalLayout_2.addWidget(self.subtraction)
        self.division = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(94)
        sizePolicy.setVerticalStretch(28)
        sizePolicy.setHeightForWidth(self.division.sizePolicy().hasHeightForWidth())
        self.division.setSizePolicy(sizePolicy)
        self.division.setMinimumSize(QtCore.QSize(94, 28))
        self.division.setObjectName("division")
        self.horizontalLayout_2.addWidget(self.division)
        self.root = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(94)
        sizePolicy.setVerticalStretch(28)
        sizePolicy.setHeightForWidth(self.root.sizePolicy().hasHeightForWidth())
        self.root.setSizePolicy(sizePolicy)
        self.root.setMinimumSize(QtCore.QSize(94, 28))
        self.root.setObjectName("root")
        self.horizontalLayout_2.addWidget(self.root)
        self.remainder = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(94)
        sizePolicy.setVerticalStretch(28)
        sizePolicy.setHeightForWidth(self.remainder.sizePolicy().hasHeightForWidth())
        self.remainder.setSizePolicy(sizePolicy)
        self.remainder.setMinimumSize(QtCore.QSize(94, 28))
        self.remainder.setObjectName("remainder")
        self.horizontalLayout_2.addWidget(self.remainder)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 5)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.second_num_edit = QtWidgets.QTextEdit(self.groupBox_2)
        self.second_num_edit.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.second_num_edit.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.second_num_edit.setObjectName("second_num_edit")
        self.verticalLayout_2.addWidget(self.second_num_edit)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addition = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(94)
        sizePolicy.setVerticalStretch(28)
        sizePolicy.setHeightForWidth(self.addition.sizePolicy().hasHeightForWidth())
        self.addition.setSizePolicy(sizePolicy)
        self.addition.setMinimumSize(QtCore.QSize(94, 28))
        self.addition.setObjectName("addition")
        self.horizontalLayout.addWidget(self.addition)
        self.multiplication = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(94)
        sizePolicy.setVerticalStretch(28)
        sizePolicy.setHeightForWidth(self.multiplication.sizePolicy().hasHeightForWidth())
        self.multiplication.setSizePolicy(sizePolicy)
        self.multiplication.setMinimumSize(QtCore.QSize(94, 28))
        self.multiplication.setObjectName("multiplication")
        self.horizontalLayout.addWidget(self.multiplication)
        self.exponentiation = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(94)
        sizePolicy.setVerticalStretch(28)
        sizePolicy.setHeightForWidth(self.exponentiation.sizePolicy().hasHeightForWidth())
        self.exponentiation.setSizePolicy(sizePolicy)
        self.exponentiation.setMinimumSize(QtCore.QSize(94, 28))
        self.exponentiation.setObjectName("exponentiation")
        self.horizontalLayout.addWidget(self.exponentiation)
        self.gdc = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(94)
        sizePolicy.setVerticalStretch(28)
        sizePolicy.setHeightForWidth(self.gdc.sizePolicy().hasHeightForWidth())
        self.gdc.setSizePolicy(sizePolicy)
        self.gdc.setMinimumSize(QtCore.QSize(94, 28))
        self.gdc.setObjectName("gdc")
        self.horizontalLayout.addWidget(self.gdc)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.helpme = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(94)
        sizePolicy.setVerticalStretch(28)
        sizePolicy.setHeightForWidth(self.helpme.sizePolicy().hasHeightForWidth())
        self.helpme.setSizePolicy(sizePolicy)
        self.helpme.setMinimumSize(QtCore.QSize(94, 28))
        self.helpme.setObjectName("helpme")
        self.horizontalLayout_3.addWidget(self.helpme)
        self.about = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(94)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about.sizePolicy().hasHeightForWidth())
        self.about.setSizePolicy(sizePolicy)
        self.about.setObjectName("about")
        self.horizontalLayout_3.addWidget(self.about)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_3, 7, 0, 1, 5)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.first_num_edit = QtWidgets.QTextEdit(self.groupBox)
        self.first_num_edit.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.first_num_edit.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.first_num_edit.setObjectName("first_num_edit")
        self.verticalLayout.addWidget(self.first_num_edit)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 5)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.result = QtWidgets.QTextBrowser(self.groupBox_3)
        self.result.setObjectName("result")
        self.verticalLayout_3.addWidget(self.result)
        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.first_num_edit, self.second_num_edit)
        MainWindow.setTabOrder(self.second_num_edit, self.result)
        MainWindow.setTabOrder(self.result, self.addition)
        MainWindow.setTabOrder(self.addition, self.subtraction)
        MainWindow.setTabOrder(self.subtraction, self.multiplication)
        MainWindow.setTabOrder(self.multiplication, self.division)
        MainWindow.setTabOrder(self.division, self.exponentiation)
        MainWindow.setTabOrder(self.exponentiation, self.root)
        MainWindow.setTabOrder(self.root, self.gdc)
        MainWindow.setTabOrder(self.gdc, self.remainder)
        MainWindow.setTabOrder(self.remainder, self.helpme)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Long arithmetic Calc"))
        self.subtraction.setText(_translate("MainWindow", "-"))
        self.division.setText(_translate("MainWindow", "/"))
        self.root.setText(_translate("MainWindow", "√"))
        self.remainder.setText(_translate("MainWindow", "ОСТ"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Второе число"))
        self.second_num_edit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Hack\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.addition.setText(_translate("MainWindow", "+"))
        self.multiplication.setText(_translate("MainWindow", "*"))
        self.exponentiation.setText(_translate("MainWindow", "^"))
        self.gdc.setText(_translate("MainWindow", "НОД"))
        self.helpme.setText(_translate("MainWindow", "Помощь"))
        self.about.setText(_translate("MainWindow", "About"))
        self.groupBox.setTitle(_translate("MainWindow", "Первое число"))
        self.first_num_edit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Hack\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Результат"))
        self.result.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Hack\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
