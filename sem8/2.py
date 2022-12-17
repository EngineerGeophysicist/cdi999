class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return self.quantity * "[]"

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if int(self.quantity - other.quantity) > 0:
            return Cell((self.quantity - other.quantity))
        else:
            return f'Так не пойдёт'

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        if int(self.quantity) > int(other.quantity):
            return "Меньше одной ячейки"
        else:
            return Cell(int(other.quantity // self.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += "[]" * cells_in_row + '\n'
        row += "[]" * (self.quantity % cells_in_row)
        return row


cells1 = Cell(3)
cells2 = Cell(6)
print(f'Первая клетка {cells1}')
print(f'Вторая клетка {cells2}')
print(f'Сложение {cells1 + cells2}')
print(f'Вычитание {cells2 - cells1}')
print(f'Деление {cells1 / cells2}')
print(f'Умножение {cells1 * cells2}')
"""
Не уверен, что правильно понял задание
print ("По два в ряд")
print(cells1.make_order(2))
print ("По три в ряд")
print(cells2.make_order(3))
"""
