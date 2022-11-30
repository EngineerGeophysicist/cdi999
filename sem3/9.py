##Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

my_list = [1.1, 1.2, 3.1, 5, 10.01]
fractionalList = []


def abc(list):
    for i in range(len(list)):
        if round((list[i] % 1), 3) != 0:
            fractionalList.append(round((list[i] % 1), 5))
    rez = max(fractionalList) - min(fractionalList)
    return rez


print(abc(my_list))
