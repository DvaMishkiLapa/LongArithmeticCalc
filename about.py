# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(500, 400))
        Dialog.setMaximumSize(QtCore.QSize(500, 400))
        font = QtGui.QFont()
        font.setFamily("Hack")
        font.setPointSize(12)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ejik = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Hack")
        self.ejik.setFont(font)
        self.ejik.setAlignment(QtCore.Qt.AlignCenter)
        self.ejik.setWordWrap(True)
        self.ejik.setObjectName("ejik")
        self.verticalLayout.addWidget(self.ejik)
        self.about_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Hack")
        self.about_label.setFont(font)
        self.about_label.setAlignment(QtCore.Qt.AlignCenter)
        self.about_label.setWordWrap(True)
        self.about_label.setObjectName("about_label")
        self.verticalLayout.addWidget(self.about_label)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About"))
        self.ejik.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.about_label.setText(_translate("Dialog", "<html><head/><body><p>Создатель: Уткин Артем Александрович<br/>Студент математического факультета ВГУ каферы КФА</p></body></html>"))
