# 1. Создать класс-исключение от класса Exception
# 2. Сгенерировать исключение в нужной точке программы
# 3. Отловить и обработать
import unittest


class DivNullEror(Exception):
    def __init__(self, txt):
        self.txt = txt


##div = input("Введите делимое: ")
##den = input("Введите делитель: ")

try:
    div = int(div)
    den = int(den)
    if den == 0:
        raise DivNullEror("Попытка деления на ноль")

except ValueError:
    print("Вы ввели не число")
except DivNullEror as err:
    print(err)

else:
    print(f"Все хорошо. Ваше число: {int(div) / int(den)}")


#####тесты
class TestDiv(unittest.TestCase):
    def setUp(self):
        den = 10
        div = 0

    def test_text(self):
        pass

    def testraises(self):
        with self.assertRaises(Exception):
            1 / 0

unittest.main()