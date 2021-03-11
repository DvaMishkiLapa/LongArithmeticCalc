import unittest
from random import randint

from bigint import GCD, BigInt


class TestBigInt(unittest.TestCase):

    MIN = -10 ** 30
    MAX = 10 ** 30
    SIMPLE_MIN = -10 ** 10
    SIMPLE_MAX = 10 ** 10
    TESTS_COUNT = 10 ** 5

    def test_add(self):
        for _ in range(self.TESTS_COUNT):
            x = randint(self.MIN, self.MAX)
            y = randint(self.MIN, self.MAX)
            big_x = BigInt(str(x))
            big_y = BigInt(str(y))
            self.assertEqual(x + y, big_x + big_y)

    def test_sub(self):
        for _ in range(self.TESTS_COUNT):
            x = randint(self.MIN, self.MAX)
            y = randint(self.MIN, self.MAX)
            big_x = BigInt(str(x))
            big_y = BigInt(str(y))
            self.assertEqual(x - y, big_x - big_y)

    def test_mul(self):
        for _ in range(self.TESTS_COUNT):
            x = randint(self.MIN, self.MAX)
            y = randint(self.MIN, self.MAX)
            big_x = BigInt(str(x))
            big_y = BigInt(str(y))
            self.assertEqual(x * y, big_x * big_y)

    def test_div(self):
        for _ in range(self.TESTS_COUNT):
            x = randint(self.MIN, self.MAX)
            y = randint(self.MIN, self.MAX)
            big_x = BigInt(str(x))
            big_y = BigInt(str(y))
            self.assertEqual(int(x / y), big_x / big_y)

    def test_mod(self):
        for _ in range(self.TESTS_COUNT):
            x = randint(self.MIN, self.MAX)
            y = randint(self.MIN, self.MAX)
            big_x = BigInt(str(x))
            big_y = BigInt(str(y))
            self.assertEqual(x % y, big_x % big_y)

    def test_pow(self):
        for _ in range(self.TESTS_COUNT):
            x = randint(self.SIMPLE_MIN, self.SIMPLE_MAX)
            y = randint(1, 10)
            big_x = BigInt(str(x))
            self.assertEqual(x**y, big_x.bipow(y))

    # def test_rt(self):
    #     for _ in range(self.TESTS_COUNT):
    #         x = randint(self.MIN, self.MAX)
    #         y = randint(1, 10)
    #         big_x = BigInt(str(x))
    #         self.assertEqual(int(x**(1 / y)), big_x.birt(y))


if __name__ == '__main__':
    unittest.main()
