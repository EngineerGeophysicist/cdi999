result = [str(el) + " " for el in range(100)]
sum = 0
for el in result:
    sum += int(el)
print("Сумма чисел в файле", sum)
try:
    file_input = open("num.txt", "w")

    file_input.writelines(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_input.close()
