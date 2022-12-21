import unittest


class Car:
    def __init__(
            self,
            color: str,
            name: str,
            is_police: bool = False):
        self.color = color
        self.name = name
        self.is_police = False

        self.speed = 0
        self._direction = ''

    def go(self, speed: float):
        try:
            self.speed = float(speed)
        except ValueError:
            pass

    def stop(self):
        self.speed = 0

    def turn(self, direction: str):
        if direction not in ('влево', 'вправо'):
            print(f"'{direction}', так мы никуда не уедем ")
            return

        if not self.speed:
            print(f"В данный момент, машина стоит, поворот невозможен")
            return

        self._direction = direction

    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч')
        if self.speed > self._max_granted_speed:
            print(
                f'Вы превысили скорость на {self.speed - self._max_granted_speed} км/ч')

    @property  ## обращаемся к direction как к обычной переменной
    def direction(self):
        return self._direction


class TownCar(Car):
    _max_granted_speed = 60  # максимальная скорость движения


class SportCar(Car):
    _max_granted_speed = 666


class WorkCar(Car):
    _max_granted_speed = 40


class PoliceCar(Car):
    _max_granted_speed = 240

    def __init__(
            self,
            color: str,
            name: str,
            is_police: bool = True):
        self.color = color
        self.name = name
        self.is_police = True

        self.speed = 0
        self._direction = ''


if __name__ == '__main__':
    cars_data = {
        ('Желтый', 'Aston Martin Cygnet'): TownCar,
        ('Синий', 'BMW M3'): SportCar,
        ('Малиновый', 'VAZ 2106'): WorkCar,
        ('Чёрный', 'Ford Crown Victoria'): PoliceCar,
    }

    for car_descr, car_cls in cars_data.items():
        car = car_cls(*car_descr)

        print(f"Название машины '{car.name}'")
        print(f"Цвет машины '{car.color}'")
        print(f"Полицейская машина '{car.is_police}'")
        print(f"Скорость машины '{car.speed}'")

        car.turn('вправо')
        car.go("brrr")
        car.go(30)
        car.turn('brrr')
        car.show_speed()
        car.go(45)
        car.show_speed()
        car.go(75)
        car.show_speed()
        car.turn('влево')
        print(f"Машина повернула '{car.direction}'")
        car.turn('вправо')
        print(f"Машина повернула '{car.direction}'")
        car.stop()
        car.show_speed()
        print('Приехали\n\n')


## Тесты

class TestCar(unittest.TestCase):
    """создаем тестовый случай"""

    def testraises(self):
        """используем функцию assertRaises"""
        with self.assertRaises(Exception):
            Car()  ## не переданы аргументы

    def testnotequal(self):
        a = PoliceCar(" ", " ")
        b = TownCar(" ", " ")
        """используем функцию assertNotEqual"""
        self.assertNotEqual(a, b)

    def testtrue(self):
        p = PoliceCar("", "")
        """используем функцию assertTrue"""
        self.assertTrue(p.is_police)

    def testfalse(self):
        s = SportCar("", "")
        """используем функцию assertFalse"""
        self.assertFalse(s.is_police)

    def testisnot(self):
        a = Car("", "")
        b = Car("", "")

        """используем функцию assertIsNot"""
        self.assertIsNot(a, b)

    def testisinstance(self):
        a = Car("", "")
        b = Car
        """используем функцию assertIs"""
        self.assertIsInstance(a, b)

    def testraises(self):
        """используем функцию assertRaises"""
        with self.assertRaises(Exception):
            Car.go()  ## не переданы аргументы

    def testin(self):
        a = 'а'
        b = 'Малиновый'

        self.assertIn(a,b)
