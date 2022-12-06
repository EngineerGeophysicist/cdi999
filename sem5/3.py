summa = 0
count = 0
persons = []
with open("costs.txt", "r") as file:
    for line in file:
        ##print(line)
        tokens = line.split(' ')
        if int(tokens[1]) >= 21000:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"Зарабатывают больше 21000: {persons}")
print(f"А в среднем: {result}")
