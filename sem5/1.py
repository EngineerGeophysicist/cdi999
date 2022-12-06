text_file = open("text.txt", "w", encoding='utf-8')

line = input("Введите строку ")
while line != "":
    text_file.write(line + "\n")
    line = input("Введите строку ")
