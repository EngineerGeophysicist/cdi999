##1) Реализовать функцию, принимающую два числа (позиционные аргументы) и
##выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
##обработку ситуации деления на ноль.


a = int(input("Введите первое число "))
b = int(input("Введите второе число "))


def divide(var1, var2):
    try:
        return (var1 / var2)

    except:
        return ("Старайтесь лучше")


print(divide(a, b))
