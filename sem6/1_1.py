from timeit import Timer
from sem5_5 import *

t = Timer("file_sum()", "from sem5_5 import file_sum")
print("file_sum", t.timeit(number=1000), "секунд")

t2 = Timer("file_sum2()", "from sem5_5 import file_sum2")
print("file_sum2", t2.timeit(number=1000), "секунд")

print("Быстрее в ", t.timeit(number=1000) / t2.timeit(number=1000), "раз")
## Аналитика
## Для оптимизации воспользовался модулем numpy
## file_sum 0.04779239999970741 секунд
## file_sum2 0.015770699999848148 секунд
## Быстрее в  2.979877451280361 раз

