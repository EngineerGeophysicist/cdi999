class Singleton:
    a = None

    def __new__(cls):
        if cls.a is None:
            cls.a = object.__new__(cls)
        return cls.a


class Test(Singleton):
    pass


T_OBJ = Test()
T_OBJ_1 = Test()
print(T_OBJ)
print(T_OBJ_1)
print(T_OBJ is T_OBJ_1)
