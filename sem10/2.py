class NonColor:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value not in ('Желтый', 'Синий', 'Чёрный', 'Малиновый'):
            raise ValueError("Не может быть")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        # owner - владелец атрибута - <class '__main__.Worker'>
        # my_attr - имя атрибута владельца - hours, rate
        self.my_attr = my_attr


class Car:
    color = NonColor()

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
