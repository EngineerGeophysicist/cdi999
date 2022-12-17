class DivNullEror(Exception):
    def __init__(self, div, den):
        self.div = div
        self.den = den

    def div(div, den):
        try:
            den = int(den)
            div = int(div)
            if den == 0:
                raise ZeroDivisionError(f'Деление на ноль недопустимо')
        except ValueError:
            return ("Вы ввели не число")
        except ZeroDivisionError:
            return (f"Деление на ноль")
        else:
            return (f'Всё хорошо {div}/{den} = {div / den}')


d = DivNullEror(100, 0)
print(DivNullEror.div(10, 0))
print(DivNullEror.div(10, 2))
print(DivNullEror.div(10, "f"))
