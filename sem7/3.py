class Worker():
    def __init__(
            self,
            name: str,
            surname: str,
            position: str,
            wage: float = 0,
            bonus: float = 0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"Зарплата": wage, "Премия": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return sum(self._income.values())


a = Position("Иван", "Иванов", "Рабочий", 17000, 3200)
print(a.name)
print(a.surname)
print(a.position)
print(a._income)
print(a.get_full_name())
print(a.get_total_income())
