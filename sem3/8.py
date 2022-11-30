##Напишите программу, которая найдёт произведение пар чисел списка. Парой
# считаем первый и последний элемент, второй и предпоследний и т.д.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def pair(list):
    out_list = []
    for i in range(int(len(list) / 2)):
        ##print(i, len(list))
        ##print(list[i], "  ", list[len(list) - 1 - i])
        out_list.append(list[i] * list[len(list) - 1 - i])
    return out_list

print(pair((my_list)))