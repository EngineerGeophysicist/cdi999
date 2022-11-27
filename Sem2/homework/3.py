##3) Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
# времени года относится месяц (зима, весна, лето, осень). Напишите решения
# через list и через dict.

season_list = ["лето", "осень", "зима", "весна"]
season_dict = {1: "лето", 2: "осень", 3: "зима", 4: "весна"}
month = int(input("Введите номер месяца"))

if month == 1 or month == 2 or month == 12:
    print(season_list[2])
    print(season_dict.get(3))
elif month == 3 or month == 4 or month == 5:
    print(season_list[3])
    print(season_dict.get[4])
elif month == 6 or month == 7 or month == 8:
    print(season_list[0])
    print(season_dict[1])
elif month == 9 or month == 10 or month == 11:
    print(season_list[1])
    print(season_dict[2])
else:
    print("Попробуйте ещё раз")
