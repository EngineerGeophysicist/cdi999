from math import factorial
import unittest


##3) Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    m = sorted((a, b, c))[1:]
    return sum(m)


##Тесты


class TestCar(unittest.TestCase):
    """создаем тестовый случай"""

    def testfunc(self):
        """test1"""
        res = my_func(1, 2, 3)
        self.assertEqual(res, 5)

    def testraises(self):
        """используем функцию assertRaises"""
        with self.assertRaises(Exception):
            my_func("")
