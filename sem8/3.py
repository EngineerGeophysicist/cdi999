class DivNullEror:
    def __init__(self, div, den):
        self.div = div
        self.den = den


    def divide_by_null(div, den):
        try:
            return (div / den)
        except:
            return (f"∞")



print(DivNullEror.divide_by_null(10, 0))
print(DivNullEror.divide_by_null(10, 0.1))
print(DivNullEror.divide_by_null(100, 0))