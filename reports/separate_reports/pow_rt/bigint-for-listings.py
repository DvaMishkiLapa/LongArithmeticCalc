# -*- coding: utf-8 -*-

import time
from sys import setrecursionlimit

setrecursionlimit(1500)  # Максимальный стек рекурсии


class BigInt(object):
    """Класс работы с большими целыми числами"""
    is_neg = False  # Флаг отрицательности числа
    value = ''      # Число в виде стоки

    def __init__(self, x=0):
        """Без аргументов конструктор задает значение равное нулю.
        Если `x` - число, конструктор заполняет экземпляр этим числом.
        Если `x` - строка, которая могла бы быть числом, конструктор заполняет экземпляр этим числом.
        Если `x` - экземпляр того же класса, конструктор копирует его содержимое в новый экземпляр."""
        self.value = '0'
        # Если в конструктор передано целое число
        if isinstance(x, int):
            self.is_neg = x < 0
            self.value = str(x if x >= 0 else -x)
        # Если в конструктор передана строка
        elif isinstance(x, str):
            # Если вдруг пришла пустая строка, пропускаем, оставляем value = 0
            if len(x):
                self.is_neg = x[0] == '-'
                # Значением будет все, после минуса, если он был. И убираем ведущие нули, если они были
                self.value = x[self.is_neg:].lstrip('0')
                # Проверяем, является ли строка числом, если нет, value = 0
                if not self.value.isdigit():
                    self.value = '0'
                if self.value == '0':
                    self.is_neg = False
        # Если в конструктор передан экземпляр того же класса, копируем его содержимое
        elif isinstance(x, BigInt):
            self.value = x.value
            self.is_neg = x.is_neg

    # Является ли число четным
    def is_even(self):
        """Является ли число четным"""
        return not (int(self.value[-1]) \& 1)

    # Перегрузка числа по модулю
    def __abs__(self):
        return BigInt(self.value)

    def bipow(self, n):
        """Возведение числа в степень `n`"""
        # Любое число в степени 0 = 1
        if n < 0:
            return None
        if not n:
            return BigInt(1)
        # if n \& 1:
        #     return BigInt(self.bipow(n - 1)) * self
        # tmp = BigInt(self.bipow(n // 2))
        # return BigInt(tmp * tmp)
        res = self
        for _ in range(n - 1):
            res *= self
        return res

    def birt(self, n):
        """Вычисление корня степени `n` из числа"""
        # Корень извлекать можем только из положительного числа
        if (n < 0) or self.is_neg:
            return None
        if n == 1:
            return self
        length = (len(self.value) + 1) // 2
        index = 0
        v = [0] * length
        while index < length:
            v[index] = 9
            while BigInt(''.join(str(x) for x in v)).bipow(n) > self and v[index]:
                v[index] -= 1
            index += 1
        v = ''.join(str(x) for x in v).lstrip('0')
        return BigInt('-' + v) if self.is_neg else BigInt(v)

    # Перегрузка перевода в bool
    def __bool__(self):
        return self.value != '0'

    # Перегрузка x < y
    def __lt__(self, other):
        if isinstance(other, int):
            other = BigInt(other)
        self_len = len(self.value)  # Запоминаем длину первого числа
        self_other = len(other.value)  # Запоминаем длину второго числа
        # Если знаки одинаковые, то проверяем значения
        if self.is_neg == other.is_neg:
            # Если длины не равны
            if self_len != self_other:
                # Меньше число с меньшей длинной для положительных и с большей длиной для отрицательных
                return (self_len < self_other) ^ self.is_neg
            i = 0
            # Ищем разряд, в котором значения отличаются
            while (i < self_len and self.value[i] == other.value[i]):
                i += 1
            # Если разряд найден, то меньше число с меньшей цифрой для положительных и с большей цифрой для отрицательных, иначе числа равны
            return (i < self_len) and ((self.value[i] < other.value[i]) ^ self.is_neg)
        return self.is_neg  # Знаки разные, если число отрицательное, то оно меньше, если положительное, то больше

    # Перегрузка x <= y
    def __le__(self, other):
        return self < other or self == other

    # Перегрузка x == y
    def __eq__(self, other):
        if isinstance(other, int):
            other = BigInt(other)
        return (self.value == other.value) and (self.is_neg == other.is_neg)

    # Перегрузка x != y
    def __ne__(self, other):
        return not self == other

    # Перегрузка x > y
    def __gt__(self, other):
        return not (self < other or self == other)

    # Перегрузка x >= y
    def __ge__(self, other):
        return self > other or self == other

    # Унарный плюс (просто копируем значение числа)
    def __pos__(self):
        return self

    # Унарный минус
    def __neg__(self):
        return BigInt(self.value if self.is_neg else '-' + self.value)

    # Число в бинарный вид (ТОЛЬКО ПОЛОЖИТЕЛЬНЫЕ)
    def to_bin(self):
        return bin(int(self.value))

    # Битовый сдвиг вправо (x >> y) (ТОЛЬКО ПОЛОЖИТЕЛЬНЫЕ)
    def __rshift__(self, n):
        if n < 0:
            raise ValueError
        self_bin = self.to_bin()
        if n >= len(self_bin) - 2 or (self == 0):
            return BigInt(0)
        return BigInt(int(self_bin[:len(self_bin) - n], 2))

    # Битовый сдвиг вслево (x << y) (ТОЛЬКО ПОЛОЖИТЕЛЬНЫЕ)
    def __lshift__(self, n):
        if n < 0:
            raise ValueError
        if self == 0:
            return BigInt(0)
        self_bin = self.to_bin()
        return BigInt(int(self_bin + ('0' * n), 2))

    # Побитовое И (x \& y) (ТОЛЬКО ПОЛОЖИТЕЛЬНЫЕ)
    def __and__(self, other):
        if isinstance(other, int):
            other = BigInt(other)
        self_bin = self.to_bin()[2:]
        other_bin = other.to_bin()[2:]
        self_len = len(self_bin)
        other_len = len(other_bin)
        if self_len > other_len:
            other_bin = other_bin.zfill(self_len)
        elif self_len < other_len:
            self_bin = self_bin.zfill(other_len)
        res = int('0b' + ''.join(['1' if (x, y) == ('1', '1') else '0' for x, y in zip(self_bin, other_bin)]), 2)
        return BigInt(res)

    # Побитовое ИЛИ (x | y) (ТОЛЬКО ПОЛОЖИТЕЛЬНЫЕ)
    def __or__(self, other):
        if isinstance(other, int):
            other = BigInt(other)
        self_bin = self.to_bin()[2:]
        other_bin = other.to_bin()[2:]
        self_len = len(self_bin)
        other_len = len(other_bin)
        if self_len > other_len:
            other_bin = other_bin.zfill(self_len)
        elif self_len < other_len:
            self_bin = self_bin.zfill(other_len)
        res = int('0b' + ''.join(['0' if (x, y) == ('0', '0') else '1' for x, y in zip(self_bin, other_bin)]), 2)
        return BigInt(res)

    # Возврат копии
    def copy(self):
        """Возврат копии"""
        return BigInt(('-' if self.is_neg else '') + self.value)

    # Сложение двух чисел
    def __add__(self, other):
        if isinstance(other, int):
            other = BigInt(other)
        # Если знаки одинаковые, то выполняем сложение
        if other.is_neg == self.is_neg:
            num2 = other.value  # Запоминаем значение второго операнда
            self_len = len(self.value)  # Длинна первого операнда
            other_len = len(num2)  # Длинна второго операнда
            # Длина суммы равна максимуму из двух длин + 1 из-за возможного переноса разряда
            length = max(self_len, other_len)
            res = [0] * (length + 1)
            for i in range(length):
                j = length - i
                # Выполняем сложение разрядов
                res[j] += int((num2[other_len - 1 - i] if i < other_len else '0')) + int((self.value[self_len - 1 - i] if i < self_len else '0'))
                res[j - 1] = res[j] // 10  # Выполняем перенос в следующий разряд, если он был
                res[j] = res[j] % 10  # Оставляем только единицы от возможного переноса и превращаем символ в цифру
                # Возвращаем результат, учитывая его знак
            return BigInt(('-' if self.is_neg else '') + ''.join(str(x) for x in res))
        # Если одно из чисел отрицательное, а другое положительное, отправляем на вычитание, меняя знак
        return (self - (-BigInt(other))) if self.is_neg else (other - (-BigInt(self)))

    # Вычитание одного числа из другого
    def __sub__(self, other):
        if isinstance(other, int):
            other = BigInt(other)
        # Если числа равны, считать не нужно
        if self == other:
            return BigInt(0)
        # Если оба числа положительные, выполняем вычитание
        if not self.is_neg and not other.is_neg:
            self_len = len(self.value)  # Запоминаем длину первого числа
            self_other = len(other.value)  # Запоминаем длину второго числа
            length = max(self_len, self_other) - 1  # Длина результата не превысит максимума длин чисел
            is_neg_res = other > self  # Определяем знак результата
            # Массивы аргументов
            new_length = length + 1
            a = [0] * new_length
            b = [0] * new_length
            res = [0] * new_length
            sign = 2 * is_neg_res - 1  # Получаем числовое значение знака результата
            for i in range(length):
                a[i] += int(self.value[self_len - 1 - i]) if i < self_len else 0  # Формируем разряды
                b[i] += int(other.value[self_other - 1 - i]) if i < self_other else 0  # Из строк аргументов
                b[i + 1] = -is_neg_res  # В зависимости от знака занимаем или не занимаем
                a[i + 1] = is_neg_res - 1  # 10 у следующего разряда
                res[length - i] += 10 + sign * (b[i] - a[i])
                res[length - 1 - i] = res[length - i] // 10
                res[length - i] = res[length - i] % 10
            # Выполняем операцию с последним разрядом
            a[length] += (length < self_len) * int(self.value[0])
            b[length] += (length < self_other) * int(other.value[0])
            # Записываем в строку последний разряд
            res[0] += sign * (b[length] - a[length])
            # Возвращаем результат, учитывая его знак
            return BigInt(('-' if is_neg_res else '') + ''.join(str(x) for x in res))
        return -BigInt(other) - (-BigInt(self)) if self.is_neg and other.is_neg else self + -BigInt(other)

    # Умножение двух чисел
    def __mul__(self, other):
        if isinstance(other, int):
            other = BigInt(other)
        # Если один из множителей равен нулю, то результат равен нулю
        if self.value == '0' or other.value == '0':
            return BigInt(0)
        self_len = len(self.value)  # Запоминаем длину первого числа
        other_len = len(other.value)  # Запоминаем длину второго числа
        length = self_len + other_len  # Результат влезет в сумму длин + 1 из-за возможного переноса
        # Флаг отрицательности результата - отрицательный, если числа разных знаков
        is_neg_res = self.is_neg ^ other.is_neg
        if length < 10:  # Число небольшое, можно по нормальному
            res = int(self.value) * int(other.value)
            return BigInt(-res if is_neg_res else res)
        else:  # Умножаем в столбик
            # Массивы аргументов
            new_length = length + 1
            a = [0] * new_length
            b = [0] * new_length
            res = [0] * new_length
            # Заполняем массивы инверсной записью чисел (с ведущими нулями)
            for i in range(new_length):
                a[i] = int(self.value[self_len - 1 - i]) if i < self_len else 0
                b[i] = int(other.value[other_len - 1 - i]) if i < other_len else 0
            # Выполняем умножение "в столбик"
            for i in range(self_len):
                for j in range(other_len):
                    res[length - (i + j)] += a[i] * b[j]
                    res[length - (i + j + 1)] += res[length - (i + j)] // 10
                    res[length - (i + j)] %= 10
            # Возвращаем результат, учитывая его знак
            return BigInt(('-' if is_neg_res else '') + ''.join(str(x) for x in res))

    # Деление одного числа на другое
    def __truediv__(self, other):
        if isinstance(other, int):
            other = BigInt(other)
        value1 = self.value  # Запоминаем значение первого числа
        value2 = other.value  # Запоминаем значение второго числа
        if value2 == '0':
            raise ZeroDivisionError  # Нельзя делить на ноль
        if value1 == '0':
            return BigInt(0)  # А вот ноль делить можно на всё, кроме нуля, но смысл
        if value2 == '1':
            return -BigInt(self) if other.is_neg else BigInt(self)  # Делить на 1 можно, но смысл?
        zeroes = 0
        while value2[len(value2) - 1 - zeroes] == '0':
            zeroes += 1
        if zeroes >= len(value1):
            return BigInt(0)
        # если у нас 13698 / 1000, то мы можем делить 13 / 1
        if zeroes:
            value1 = value1[:len(value1) - zeroes]
            value2 = value2[:len(value2) - zeroes]
        is_neg_res = self.is_neg ^ other.is_neg  # Cчитаем знак числа
        tmp = BigInt(value2)
        divider_length = len(value2)  # Запоминаем длину делителя
        # Если длина больше 8, то обнуляем делитель, иначе переводим строку в long
        # Можно не обнулять, но мы думаем, что Python не умеет в большие числа
        divider_v = 0 if divider_length > 8 else int(value2)
        length = len(value1)  # Получаем длину делимого
        index = 0  # Стартуем с нулевого индекса
        div = ''  # Строка результата деления
        v = ''  # Строка подчисла (которое делится на делитель в столбик)
        index = len(value2)
        v = value1[:index]
        mod = None
        while True:
            count = 0  # Результат деления подчисла на делитель
            # Если можем разделить, то делим
            if BigInt(v) >= tmp:
                # Если не входит в long, то делим с помощью вычитания
                if divider_length > 8:
                    mod = BigInt(v)
                    while mod >= tmp:
                        mod = (mod - tmp).copy()
                        count += 1
                    v = mod.value
                else:
                    mod = int(v)
                    count = mod // divider_v
                    v = str(mod % divider_v)
            # Если не делили, то добавили ноль к результату, иначе добавили результат деления
            div = div + (str(count) if count else '0')
            if index <= length:
                try:  # Тот самый ноль, лучше не спрашивать
                    v = v + value1[index]
                except IndexError:
                    v = v + '0'
                index += 1  # Формируем новое значение для подчисла
            if not (index <= length):
                break
        # Возвращаем результат учитывая знак и возможное равенство нулю
        return BigInt('-' + div if is_neg_res and div != '0' else div)

    # Обработка для выходных данных
    def __str__(self):
        return str('-' if self.is_neg else '') + self.value

    # Остаток от деления
    def __mod__(self, other):
        if isinstance(other, int):
            other = BigInt(other)
        if other.value == '0':
            return None
        if self.value == '0' or other.value == "1":
            return BigInt(0)
        # Если числа меньше 9, можно посчитать по нормальному
        if len(self.value) < 9 and len(other.value) < 9:
            return BigInt(int(str('-' if self.is_neg else '') + self.value) % int(str('-' if other.is_neg else '') + other.value))
        tmp = BigInt(other.value)
        divider_length = len(other.value)  # запоминаем длину делителя
        # Если длина больше 8, то обнуляем long'овый делитель, иначе переводим строку в long
        divider_v = 0 if divider_length > 8 else int(other.value)
        length = len(self.value)
        index = 0
        mod2 = self.copy()
        v = ''
        mod = None
        while BigInt(v) < tmp and index < length:
            v = v + self.value[index]
            index += 1
        while True:
            if BigInt(v) >= tmp:
                if divider_v:
                    v = str(int(v) % divider_v)
                else:
                    mod = BigInt(v)
                    while mod >= tmp:
                        mod = (mod - tmp).copy()
                    v = mod.value
            if index <= length:
                mod2 = v
                try:
                    v = v + self.value[index]
                except IndexError:
                    break
                index += 1
            if not (index <= length):
                break
        if isinstance(mod2, BigInt):
            if mod2.value == '0':
                return BigInt(0)
        res = -BigInt(mod2) if self.is_neg else BigInt(mod2)
        if self.is_neg ^ other.is_neg and res != 0:
            return other + res
        return res


def GCD(a, b):
    """Нахождение наибольшего общего делителя у чисел `a` и `b`"""
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    while b:
        a, b = b, a % b
    return a


def binary_GCD(num1, num2):
    """Нахождение наибольшего общего делителя у чисел `a` и `b` (Бинарный алгоритм)"""
    if num1 < 0:
        num1 = -num1
    if num2 < 0:
        num2 = -num2
    shift = 0
    # Если одно из чисел равно нулю, делитель - другое число
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    # Если num1 = 1010, а num2 = 0100, то num1 | num2 = 1110
    # 1110 \& 0001 == 0, тогда происходит сдвиг, который фиксируется в shift
    while (num1 | num2) \& 1 == 0:
        shift += 1
        num1 = num1 >> 1
        num2 = num2 >> 1
    # Если True, значит num1 - четное, иначе - нечетное
    while num1 \& 1 == 0:
        # если нечетное, сдвигаем на один бит
        num1 = num1 >> 1
    while num2 != 0:
        # пока число нечётное, сдвигаем на один бит
        while num2 \& 1 == 0:
            num2 = num2 >> 1
        # если первое число больше второго
        if num1 > num2:
            # меняем их местами
            num1, num2 = num2, num1
        # теперь первое число меньше второго, вычитаем
        num2 = num2 - num1
    # возвращаем число, перед этим сдвинув его биты на shift
    return num1 << shift


if __name__ == '__main__':
    while True:
        menu_text = '\n'.join([
            'Выберите действие:',
            '1) x + y',
            '2) x - y',
            '3) x * y',
            '4) x / y',
            '5) Возведение числа x в степень y',
            '6) Извлечение корня из числа x степени y',
            'q) Выход'
        ])
        print(menu_text)
        choice = input()
        if choice == '1':
            x = BigInt(input('Введите первое число (x): '))
            y = BigInt(input('Введите второе число (y): '))
            t = time.time()
            res = x + y
            print(f'\nВремя расчета: {time.time() - t} сек.')
            print('x + y =', res, '\n\n')
        elif choice == '2':
            x = BigInt(input('Введите первое число (x): '))
            y = BigInt(input('Введите второе число (y): '))
            t = time.time()
            res = x - y
            print(f'\nВремя расчета: {time.time() - t} сек.')
            print('x - y =', res, '\n\n')
        elif choice == '3':
            x = BigInt(input('Введите первое число (x): '))
            y = BigInt(input('Введите второе число (y): '))
            t = time.time()
            res = x * y
            print(f'\nВремя расчета: {time.time() - t} сек.')
            print('x * y =', res, '\n\n')
        elif choice == '4':
            x = BigInt(input('Введите первое число (x): '))
            y = BigInt(input('Введите второе число (y): '))
            t = time.time()
            res = x / y
            print(f'\nВремя расчета: {time.time() - t} сек.')
            print('x / y =', res, '\n\n')
        elif choice == '5':
            x = BigInt(input('Введите первое число (x): '))
            y = int(input('Введите второе число (y): '))
            t = time.time()
            res = x.bipow(y)
            print(f'\nВремя расчета: {time.time() - t} сек.')
            print('x**y =', res, '\n\n')
        elif choice == '6':
            x = BigInt(input('Введите первое число (x): '))
            y = int(input('Введите второе число (y): '))
            t = time.time()
            res = x.birt(y)
            print(f'\nВремя расчета: {time.time() - t} сек.')
            print('x**(1/y) =', res, '\n\n')
        else:
            exit()
