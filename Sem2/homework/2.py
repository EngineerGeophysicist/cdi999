##2) Для списка реализовать обмен значений соседних элементов, т.е. значениями
# обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
# элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

el_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0

while i < el_count:
    my_list.append(input(f"Введите {i+1} значение списка "))
    i += 1
el = 0
print(f"Исходный{my_list}")
for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)
