class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return (f"Запуск отрисовки, {self.title}")


class Pen(Stationery):
    def draw(self):
        return ("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def draw(self):
        return ("Запуск отрисовки карандашом")


class Handle(Stationery):
    def draw(self):
        return ("Запуск отрисовки маркером")


data = {"ручка": Pen,
        "карандаш": Pencil,
        "маркер": Handle,
        "канцелярская принадлежность": Stationery}
for el, type in data.items():
    p = type(el)
    print(p.draw())
