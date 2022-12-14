class Road():
    _weight = 25
    _thickness = 5

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def weight_line(self):
        w = (self.__length *
             self.__width *
             self._weight *
             self._thickness) / 1000
        return (str(w) + " тонн")


a = Road(5000, 20)
print(a.weight_line())
