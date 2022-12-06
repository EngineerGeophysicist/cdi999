translater = {'One': 'Первый', 'Two': 'Второй', 'Three': 'Третий', 'Four': 'Четвертый'}
my_list = []
result = []
try:
    file_obj = open("eng.txt", 'r')
    for line in file_obj:
        tokens = line.split(" — ")
        ##print(tokens[0])
        if tokens[0] in translater:
            word = translater[tokens[0]]
            result.append(word +' — '+ tokens[1])
    ##print(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()

try:
    file_input = open("rus.txt", "w")
    file_input.writelines(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_input.close()