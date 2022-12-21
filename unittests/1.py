import unittest


class Road():
    _weight = 25
    _thickness = 5

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    r = ""

    def weight_line(self):
        w = (self.__length *
             self.__width *
             self._weight *
             self._thickness) / 1000
        r = str(w) + " тонн"
        return r


a = Road(5000, 20)
print(a.weight_line())
"""
Тесты
"""


class TestDiv(unittest.TestCase):
    """создаем тестовый случай"""

    def testequal(self):
        """создаем сам тест"""
        a = Road(5000, 20)
        # используем функцию assertEqual
        self.assertEqual(a.weight_line(), "12500.0 тонн")

    def testraises(self):
        """используем функцию assertRaises"""
        with self.assertRaises(Exception):
            a.weight_line("")

    def testisnone(self):
        """используем функцию assertIsNone"""
        self.assertIsNone(a.__init__(5000, 20))  ## NONE __init__
        self.assertIsNotNone(a.weight_line())  ## weight_line not None
