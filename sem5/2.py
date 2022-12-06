with open(r"file.txt", "r") as file:
    l = 0
    for line in file:
        l += 1
        if line == " ":
            pass
        w = 0
        for word in line:
            if word == " " or word == "\n":
                w += 1

        print("Строка", l, "содержит слов в количестве", w)
