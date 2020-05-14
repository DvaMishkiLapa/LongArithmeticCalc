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
            return BigInt(('-' if self.is_neg else '') + ''.join(str(x) for x in res))
        else:
            return -BigInt(other) - (-BigInt(self)) if self.is_neg and other.is_neg else self + -BigInt(other)

    # Обработка для выходных данных
    def __str__(self):
        return str('-' if self.is_neg else '') + self.value


if __name__ == '__main__':
    pass
