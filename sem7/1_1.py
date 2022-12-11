from timeit import Timer
from sem5_5 import *

t = Timer("func()", "from sem5_5 import func")
print("func", t.timeit(number=1000), "секунд")

t2 = Timer("func2()", "from sem5_5 import func2")
print("func2", t2.timeit(number=1000), "секунд")

print ("Быстрее в ", t.timeit(number=1000)/t2.timeit(number=1000), "раз")
## Аналитика
## Для оптимизации воспользовался модулем numpy
## func 0.04779239999970741 секунд
## func2 0.015770699999848148 секунд
## Быстрее в  2.979877451280361 раз