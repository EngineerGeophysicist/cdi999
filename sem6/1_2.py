from timeit import Timer
from sem3_7 import *

t = Timer("sum_list()", "from sem3_7 import sum_list")
print("sum_list", t.timeit(number=1000), "секунд")

t2 = Timer("sum_list2()", "from sem3_7 import sum_list2")
print("sum_list2", t2.timeit(number=1000), "секунд")

print("Быстрее в ", t.timeit(number=1000) / t2.timeit(number=1000), "раз")
## Аналитика
## Использование кортежей позволило существенно повысить скорость исполнения кода
## sumList 0.001756300000124611 секунд
## sumList2 0.0015318999994633486 секунд
## Быстрее в  1.0438460452426683 раз
