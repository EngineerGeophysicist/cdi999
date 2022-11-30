##Напишите программу, которая будет преобразовывать десятичное число в двоичное
my_num = 3


def convert10to2(num):
    q = []
    while num > 0:
        q.append(num % 2)
        num = num // 2
    rez = str(0)
    for i in range(len(q) - 1, -1, -1):
        rez += str(q[i])
    return int(rez)


print(convert10to2(my_num))
