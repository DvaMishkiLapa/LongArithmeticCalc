# -*- coding: utf-8 -*-

from sys import argv

from PyQt5 import QtCore, QtGui, QtWidgets

import about
import helpme
import ui
from bigint import GCD, BigInt


# Класс главной формы
class LongArithmeticCalc(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.error_message = 'Ошибка ввода :('

        # Events кнопок меню описания и выбора файла
        self.addition.clicked.connect(self.addition_clicked)                # +
        self.subtraction.clicked.connect(self.subtraction_clicked)          # -
        self.multiplication.clicked.connect(self.multiplication_clicked)    # *
        self.division.clicked.connect(self.division_clicked)                # /
        self.exponentiation.clicked.connect(self.exponentiation_clicked)    # степень
        self.root.clicked.connect(self.root_clicked)                        # корень
        self.gdc.clicked.connect(self.gdc_clicked)                          # НОД
        self.remainder.clicked.connect(self.remainder_clicked)              # ОСТ
        self.about.clicked.connect(self.about_clicked)                      # about
        self.helpme.clicked.connect(self.helpme_clicked)                    # помощь

    def get_nums(self):
        return self.first_num_edit.toPlainText(), self.second_num_edit.toPlainText()

    def data_validation(self, a):
        try:
            int(a)
            return True
        except ValueError:
            return False

    def addition_clicked(self):  # +
        first_num, second_num = self.get_nums()
        if self.data_validation(first_num) and self.data_validation(second_num):
            res = str(BigInt(first_num) + BigInt(second_num))
            self.result.setText(res)
        else:
            self.result.setText(self.error_message)

    def subtraction_clicked(self):  # -
        first_num, second_num = self.get_nums()
        if self.data_validation(first_num) and self.data_validation(second_num):
            res = str(BigInt(first_num) - BigInt(second_num))
            self.result.setText(res)
        else:
            self.result.setText(self.error_message)

    def multiplication_clicked(self):  # *
        first_num, second_num = self.get_nums()
        if self.data_validation(first_num) and self.data_validation(second_num):
            res = str(BigInt(first_num) * BigInt(second_num))
            self.result.setText(res)
        else:
            self.result.setText(self.error_message)

    def division_clicked(self):  # /
        first_num, second_num = self.get_nums()
        if self.data_validation(first_num) and self.data_validation(second_num):
            res = str(BigInt(first_num) / BigInt(second_num))
            self.result.setText(res)
        else:
            self.result.setText(self.error_message)

    def exponentiation_clicked(self):  # степень
        first_num, second_num = self.get_nums()
        if self.data_validation(first_num) and self.data_validation(second_num):
            res = str(BigInt(first_num).bipow(int(second_num)))
            self.result.setText(res)
        else:
            self.result.setText(self.error_message)

    def root_clicked(self):  # корень
        first_num, second_num = self.get_nums()
        if self.data_validation(first_num) and self.data_validation(second_num):
            res = str(BigInt(first_num).birt(int(second_num)))
            self.result.setText(res)
        else:
            self.result.setText(self.error_message)

    def gdc_clicked(self):  # НОД
        first_num, second_num = self.get_nums()
        if self.data_validation(first_num) and self.data_validation(second_num):
            res = str(GCD(BigInt(first_num), BigInt(second_num)))
            self.result.setText(res)
        else:
            self.result.setText(self.error_message)

    def remainder_clicked(self):  # ОСТ
        first_num, second_num = self.get_nums()
        if self.data_validation(first_num) and self.data_validation(second_num):
            res = str(BigInt(first_num) % BigInt(second_num))
            self.result.setText(res)
        else:
            self.result.setText(self.error_message)

    def about_clicked(self):  # About
        about_dialog = about()
        about_dialog.exec_()

    def helpme_clicked(self):  # Помощь
        helpme_dialog = helpme()
        helpme_dialog.exec_()


class about(QtWidgets.QDialog, about.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        pixmap = QtGui.QPixmap('./img/math_logo.png')
        self.ejik.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())


class helpme(QtWidgets.QDialog, helpme.Ui_helpme):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(argv)
    main_window = LongArithmeticCalc()
    main_window.show()
    app.exec_()


if __name__ == "__main__":
    main()
