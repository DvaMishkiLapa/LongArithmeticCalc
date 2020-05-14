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
        # Если self - отрицательный, other - положительный = True
        if self.is_neg and not other.is_neg:
            return True
        # Если self - положительный, other - отрицательный = False
        if not self.is_neg and other.is_neg:
            return False
        # Если оба числа одго знака, сравниваем значение и логически умножаем на значение знака
        # Python правильно сравнивает строки, в которых находятся числа
        if self.is_neg == other.is_neg:
            return (self.value < other.value) and not self.is_neg

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

    # Обработка для выходных данных
    def __str__(self):
        return str('-' if self.is_neg else '') + self.value


if __name__ == '__main__':
    pass
