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

    # Обработка для выходных данных
    def __str__(self):
        return str('-' if self.is_neg else '') + self.value


if __name__ == '__main__':
    pass
