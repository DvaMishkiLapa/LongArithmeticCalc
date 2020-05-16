from sys import argv
from PyQt5 import QtCore, QtGui, QtWidgets

import ui
from bigint import GCD, BigInt


# Класс главной формы
class LongArithmeticCalc(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Events кнопок меню описания и выбора файла
        self.addition.clicked.connect(self.addition_clicked)                # +
        self.subtraction.clicked.connect(self.subtraction_clicked)          # -
        self.multiplication.clicked.connect(self.multiplication_clicked)    # *
        self.division.clicked.connect(self.division_clicked)                # /
        self.exponentiation.clicked.connect(self.exponentiation_clicked)    # ^
        self.root.clicked.connect(self.root_clicked)                        # √
        self.gdc.clicked.connect(self.gdc_clicked)                          # НОД
        self.remainder.clicked.connect(self.remainder_clicked)              # ОСТ

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
        valid = self.data_validation(first_num) and self.data_validation(second_num)
        if self.data_validation(first_num) and self.data_validation(second_num):
            res = str(BigInt(first_num) + BigInt(second_num))
            self.result.setText(res)
        else:
            self.result.setText('Ошибка ввода :(')

    def subtraction_clicked(self):  # -
        first_num, second_num = self.get_nums()
        valid = self.data_validation(first_num) and self.data_validation(second_num)
        if self.data_validation(first_num) and self.data_validation(second_num):
            res = str(BigInt(first_num) - BigInt(second_num))
            self.result.setText(res)
        else:
            self.result.setText('Ошибка ввода :(')

    def multiplication_clicked(self):  # *
        first_num, second_num = self.get_nums()
        valid = self.data_validation(first_num) and self.data_validation(second_num)
        if self.data_validation(first_num) and self.data_validation(second_num):
            res = str(BigInt(first_num) * BigInt(second_num))
            self.result.setText(res)
        else:
            self.result.setText('Ошибка ввода :(')

    def division_clicked(self):  # /
        first_num, second_num = self.get_nums()
        valid = self.data_validation(first_num) and self.data_validation(second_num)
        if self.data_validation(first_num) and self.data_validation(second_num):
            res = str(BigInt(first_num) / BigInt(second_num))
            self.result.setText(res)
        else:
            self.result.setText('Ошибка ввода :(')

    def exponentiation_clicked(self):  # ^
        first_num, second_num = self.get_nums()
        valid = self.data_validation(first_num) and self.data_validation(second_num)
        if self.data_validation(first_num) and self.data_validation(second_num):
            res = str(BigInt(first_num).bipow(int(second_num)))
            self.result.setText(res)
        else:
            self.result.setText('Ошибка ввода :(')

    def root_clicked(self):  # √
        first_num, second_num = self.get_nums()
        valid = self.data_validation(first_num) and self.data_validation(second_num)
        if self.data_validation(first_num) and self.data_validation(second_num):
            res = str(BigInt(first_num).birt(int(second_num)))
            self.result.setText(res)
        else:
            self.result.setText('Ошибка ввода :(')

    def gdc_clicked(self):  # НОД
        first_num, second_num = self.get_nums()
        valid = self.data_validation(first_num) and self.data_validation(second_num)
        if self.data_validation(first_num) and self.data_validation(second_num):
            res = str(GCD(BigInt(first_num), BigInt(second_num)))
            self.result.setText(res)
        else:
            self.result.setText('Ошибка ввода :(')

    def remainder_clicked(self):  # ОСТ
        first_num, second_num = self.get_nums()
        valid = self.data_validation(first_num) and self.data_validation(second_num)
        if self.data_validation(first_num) and self.data_validation(second_num):
            res = str(BigInt(first_num) % BigInt(second_num))
            self.result.setText(res)
        else:
            self.result.setText('Ошибка ввода :(')


def main():
    app = QtWidgets.QApplication(argv)
    main_window = LongArithmeticCalc()
    main_window.show()
    app.exec_()


if __name__ == "__main__":
    main()
