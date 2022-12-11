import numpy as np


def func():
    result = [str(el) + " " for el in range(100)]
    sum = 0
    for el in result:
        sum += int(el)
    return ("Сумма чисел в файле", sum)
    try:
        file_input = open("num.txt", "w")

        file_input.writelines(result)
    except IOError:
        return ("Произошла ошибка ввода-вывода!")
    finally:
        file_input.close()


def func2():
    result = np.arange(100)
    sum = 0

    for i in result:
        sum += i
    return (f"Сумма чисел в файле {sum}")
    try:
        file_input = open("num.txt", "w")

        file_input.writelines(result)
    except IOError:
        return "Произошла ошибка ввода-вывода!"
    finally:
        file_input.close()



