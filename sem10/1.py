class NonNegative:
    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Не может быть отрицательным")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        # owner - владелец атрибута - <class '__main__.Worker'>
        # my_attr - имя атрибута владельца - hours, rate
        self.my_attr = my_attr
class NonStr:
    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if not isinstance(value,str):
            raise ValueError(f"{self.my_attr} должно быть строкой")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        # owner - владелец атрибута - <class '__main__.Worker'>
        # my_attr - имя атрибута владельца - hours, rate
        self.my_attr = my_attr


class Worker():
    wage = NonNegative()
    bonus = NonNegative()
    name = NonStr()
    surname = NonStr()
    position = NonStr()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self.wage + self.bonus


a = Position('Иван', "Иванов", "Рабочий", 17000, 3200)
print(a.name)
print(a.surname)
print(a.position)
print(a.wage)
print(a.bonus)
print(a.get_full_name())
print(a.get_total_income())
