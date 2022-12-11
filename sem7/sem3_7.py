def sumList():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    s = 0
    for i in range(len(list)):
        if i % 2 != 0:
            s += list[i]
    return s


##print("Сумма элементов на нечетных позициях", sumList())

def sumList2():
    list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    s = 0
    for i in range(len(list)):
        if i % 2 != 0:
            s += list[i]
    return s

##print("Сумма элементов на нечетных позициях", sumList2())
