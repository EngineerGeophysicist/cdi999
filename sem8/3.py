class DivNullEror:
    def __init__(self, div, den):
        self.div = div
        self.den = den

    def divide_by_null(div=int, den=int):
        try:
            if den == 0:
                raise ZeroDivisionError(f'Деление на ноль недопустимо')
        except ZeroDivisionError:
            return (f"Деление на ноль")
        except OwnError as err:
            print(err)
        else:
            return f'Всё хорошо {div}/{den} = {div / den}'


div = DivNullEror(100, 0)
print(DivNullEror.divide_by_null(10, 0))
print(DivNullEror.divide_by_null(10, 0.1))
print(DivNullEror.divide_by_null(100, 0))
