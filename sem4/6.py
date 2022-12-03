from itertools import cycle, count

v_start = int(input('Введите первое число '))
v_stop = 10

print("а) итератор, генерирующий целые числа, начиная с указанного")
for el in count(v_start):
    if el < v_stop:
        print(el)
    else:
        break


print("б) итератор, повторяющий элементы списка, определенного заранее")
my_list = [10, 20, 21]
v_stop = 41
count = 0
for b in cycle(my_list):
    if count < v_stop:
        print(b)
        count += 1
    else:
        break
