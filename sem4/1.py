from sys import argv

script_name, rezult_per_hour, wage_rate, premium = argv

print("Выработка в час: ", rezult_per_hour)
print("Ставка: ", wage_rate)
print("Премия: ", premium)

zp = (8 * int(rezult_per_hour) * int(wage_rate)) + int(premium)

print("Заработная плата за восьмичасовую смену: ", zp)
