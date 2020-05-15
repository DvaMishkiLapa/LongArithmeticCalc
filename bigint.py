class BigInt(object):
    """Класс работы с большими целыми числами"""
    MAX_SIZE_STEP = 2000
    is_neg = False  # Флаг отрицательности числа
    value = ''      # Число в виде стоки

    def __init__(self, x=0):
        """Без аргументов конструктор задает значение равное нулю.
        Если x - число, конструктор заполняет экземпляр этим числом.
        Если x - строка, которая могла бы быть числом, конструктор заполняет экземпляр этим числом.
        Если x - экземпляр того же класса, конструктор копирует его содержимое в новый экземпляр."""
        self.value = '0'
        # Если в конструктор передано целое число
        if isinstance(x, int):
            self.is_neg = x < 0
            self.value = str(x if x > 0 else -x)
        # Если в конструктор передана строка
        elif isinstance(x, str):
            # Если вдруг пришла пустая строка, пропускаем, оставляем value = 0
            if not len(x):
                pass
            else:
                self.is_neg = x[0] == '-'
                # Значением будет все, после минуса, если он был. И убираем ведущие нули, если они были
                self.value = x[self.is_neg:].lstrip('0')
                # Проверяем, является ли строка числом, если нет, value = 0
                if not self.value.isdigit():
                    self.value = '0'
        # Если в конструктор передан экземпляр того же класса, копируем его содержимое
        elif isinstance(x, BigInt):
            self.value = x.value
            self.is_neg = x.is_neg

    # Является ли число четным
    def is_iven(self):
        return int(self.value[len(self.value) - 1]) % 2 == 0

    # Перегрузка числа по модулю
    def __abs__(self):
        return self.value

    # Перегрузка x < y
    def __lt__(self, other):
        self_len = len(self.value)  # Запоминаем длину первого числа
        self_other = len(other.value)  # Запоминаем длину второго числа
        # Если знаки одинаковые, то проверяем значения
        if self.is_neg == other.is_neg:
            # Если длины не равны
            if (self_len != self_other):
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
        return (self.value == other.value) and (self.is_neg == other.is_neg)

    # Перегрузка x != y
    def __ne__(self, other):
        return (self.value != other.value) or (self.is_neg != other.is_neg)

    # Перегрузка x > y
    def __gt__(self, other):
        return not (self < other or self == other)

    # Перегрузка x >= y
    def __ge__(self, other):
        return self > other or self == other

    # Унарный плюс (просто копируем значение числа)
    def __pos__(self):
        return BigInt(self)

    # Унарный минус
    def __neg__(self):
        return BigInt(self.value if self.is_neg else '-' + self.value)

    # Возврат копии
    def copy(self):
        return BigInt(('-' if self.is_neg else '') + self.value)

    # Сложение двух чисел
    def __add__(self, other):
        new_int = BigInt()
        # Если знаки одинаковые, то выполняем сложение
        if not (other.is_neg ^ self.is_neg):
            num2 = other.value  # Запоминаем значение второго операнда
            self_len = len(self.value)  # Длинна первого операнда
            other_len = len(num2)  # Длинна второго операнда
            # Длина суммы равна максимуму из двух длин + 1 из-за возможного переноса разряда
            length = max(self_len, other_len) + 1
            res = [0 for _ in range(length)]
            for i in range(length - 1):
                j = length - 1 - i
                # Выполняем сложение разрядов
                res[j] += int((num2[other_len - 1 - i] if i < other_len else '0')) + int((self.value[self_len - 1 - i] if i < self_len else '0'))
                res[j - 1] = res[j] // 10  # Выполняем перенос в следущий разряд, если он был
                res[j] = res[j] % 10  # Оставляем только единицы от возможного переноса и превращаем символ в цифру
                # Возвращаем результат, учитывая его знак
            return BigInt(('-' if self.is_neg else '') + ''.join(str(x) for x in res))
        else:
            # Если одно из чисел отрицательное, а другое положительное, отправляем на вычитание, меняя знак
            return (self - (-BigInt(other))) if self.is_neg else (other - (-BigInt(self)))

    # Вычитание одного числа из другого
    def __sub__(self, other):
        # Если числа равны, считать не нужно
        if self == other:
            return 0
        # Если оба числа положительные, выполняем вычитание
        if not self.is_neg and not other.is_neg:
            self_len = len(self.value)  # Запоминаем длину первого числа
            self_other = len(other.value)  # Запоминаем длину второго числа
            length = max(self_len, self_other)  # Длина результата не превысит максимума длин чисел
            is_neg_res = other > self  # Определяем знак результата
            # Массивы аргументов
            a = [0 for _ in range(length)]
            b = [0 for _ in range(length)]
            res = [0 for _ in range(length)]
            sign = 2 * is_neg_res - 1  # Получаем числовое значение знака результата
            for i in range(length - 1):
                a[i] += int(self.value[self_len - 1 - i]) if i < self_len else 0  # Формируем разряды
                b[i] += int(other.value[self_other - 1 - i]) if i < self_other else 0  # Из строк аргументов
                b[i + 1] = -is_neg_res  # В зависимости от знака занимаем или не занимаем
                a[i + 1] = is_neg_res - 1  # 10 у следующего разряда
                res[length - 1 - i] += 10 + sign * (b[i] - a[i])
                res[length - 2 - i] = res[length - 1 - i] // 10
                res[length - 1 - i] = res[length - 1 - i] % 10
            # Выполняем операцию с последним разрядом
            a[length - 1] += (length - 1 < self_len) * int(self.value[0])
            b[length - 1] += (length - 1 < self_other) * int(other.value[0])
            # Записываем в строку последний разряд
            res[0] += sign * (b[length - 1] - a[length - 1])
            # Возвращаем результат, учитывая его знак
            return BigInt(('-' if self.is_neg else '') + ''.join(str(x) for x in res))
        else:
            return -BigInt(other) - (-BigInt(self)) if self.is_neg and other.is_neg else self + -BigInt(other)

    # Умножение двух чисел
    def __mul__(self, other):
        # Если один из множителей равен нулю, то результат равен нулю
        if self.value == '0' and other.value == '0':
            return 0
        self_len = len(self.value)  # Запоминаем длину первого числа
        other_len = len(other.value)  # Запоминаем длину второго числа
        length = self_len + other_len + 1  # Резульат влезет в сумму длин + 1 из-за возможного переноса
        # Флаг отрицательности результата - отрицательный, если числа разных знаков
        is_neg_res = self.is_neg ^ other.is_neg
        if length < 10:  # Число небольшое, можно по нормальному
            res = int(self.value) * int(other.value)
            return BigInt(-res if is_neg_res else res)
        else:  # Умножаем в столбик
            # Массивы аргументов
            a = [0 for _ in range(length)]
            b = [0 for _ in range(length)]
            res = [0 for _ in range(length)]
            # Заполняем массивы инверсной записью чисел (с ведущими нулями)
            for i in range(length):
                a[i] = int(self.value[self_len - 1 - i]) if i < self_len else 0
                b[i] = int(other.value[other_len - 1 - i]) if i < other_len else 0
                res[i] = 0
            # Выполняем умножение "в столбик"
            for i in range(self_len):
                for j in range(other_len):
                    res[length - 1 - (i + j)] += a[i] * b[j]
                    res[length - 1 - (i + j + 1)] += res[length - 1 - (i + j)] // 10
                    res[length - 1 - (i + j)] %= 10
            # Возвращаем результат, учитывая его знак
            return BigInt(('-' if self.is_neg else '') + ''.join(str(x) for x in res))

    # Деление одного числа на другое
    def __truediv__(self, other):
        value1 = self.value  # Запоминаем значение первого числа
        value2 = other.value  # Запоминаем значение второго числа
        if value2[0] == '0':
            return None  # Нельзя делить на ноль
        if value1[0] == '0':
            return 0  # А вот ноль делить можно на всё, кроме нуля, но смысл
        if value2 == '1':
            return BigInt(-BigInt(self) if other.is_neg else BigInt(self))  # Делить на 1 можно, но смысл?
        zeroes = 0
        while value2[len(value2) - 1 - zeroes] == '0':
            zeroes += 1
        if zeroes >= len(value1):
            return 0
        # Избавляемся от общих нулей в конце чисел
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
        # Формируем начальное число для деления
        while BigInt(v) < tmp and index < length:
            v = v + value1[index]
            index += 1
        mod = None
        while True:
            count = 0  # Результат деления подчисла на делитель
            # Если можем разделить, то делим
            if BigInt(v) >= tmp:
                # Если не входит в long, то делим с помощью вычитания
                if (divider_length > 8):
                    mod = BigInt(v)
                    while mod >= tmp:
                        mod = (mod - tmp).copy()
                        count += 1
                    v = mod.value
                else:
                    mod = int(v)
                    count = mod // divider_v
                    v = str(mod % divider_v)
            # Если не делили, то добавили ноль к результату, иначе добавили результат дедения
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

    def __mod__(self, other):
        if other.value[0] == '0':
            return None
        if self.value[0] == '0' or other.value == "1":
            return 0
        # Если числа меньше 9, можно посчитать по нормальному
        if len(self.value) < 9 and len(other.value) < 9:
            res = int(self.value) % int(other.value)
            return BigInt(-res if self.is_neg else res)
        tmp = BigInt(other.value)
        divider_length = len(other.value)  # запоминаем длину делителя
        # Если длина больше 9, то обнуляем long'овый делитель, иначе переводим строку в long
        divider_v = 0 if divider_length >= 9 else int(other.value)
        length = len(self.value)
        index = 0
        mod2 = self.copy()
        v = ''
        mod = None
        while BigInt(v) < tmp and index < length:
            v += value[index]
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
                v = v + value[index]
                index += 1
            if not (index <= length):
                break
        if (mod2.value == "0"):
            return 0
        return -BigInt(mod2) if self.is_neg else mod2


if __name__ == '__main__':
    pass
