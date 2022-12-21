import unittest


##1) Реализовать функцию, принимающую два числа (позиционные аргументы) и
##выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
##обработку ситуации деления на ноль.


##a = int(input("Введите первое число "))
##b = int(input("Введите второе число "))


def divide(var1, var2):
    try:
        return (var1 / var2)

    except:
        return ("Старайтесь лучше")


##Тесты
class TestDivide(unittest.TestCase):
    """создаем тестовый случай"""

    def testequal(self):
        """создаем сам тест"""

        # используем функцию assertEqual
        self.assertEqual(divide(3, 2), 1.5)
        self.assertEqual(divide(3, 0), "Старайтесь лучше")

    def testraises(self):
        """используем функцию assertRaises"""
        with self.assertRaises(Exception):
            divide()  ##всё можно сломать
