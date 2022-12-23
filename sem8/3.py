class DivNullEror(Exception):
    def __init__(self, txt):
        self.txt = txt
div = input("Введите делимое: ")
den = input("Введите делитель: ")
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
