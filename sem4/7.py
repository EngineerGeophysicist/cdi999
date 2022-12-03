from math import factorial

n = int(input("Введите количество факториалов "))


def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)


for el in fact(n):
    print(el)
