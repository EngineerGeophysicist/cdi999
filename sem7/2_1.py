from memory_profiler import profile


@profile
def sumList():
    my_list = list(range(100000))  ## берем массив побольше
    s = 0
    for i in my_list:
        if i % 2 != 0:
            s += my_list[i]
    my_list = None  ## переобределяем на None , чтоб высвободить память
    return s


sumList()

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     20.2 MiB     20.2 MiB           1   @profile
     5                                         def sumList():
     6     24.0 MiB      3.8 MiB           1       my_list = list(range(100000))  ## берем массив побольше
     7     24.0 MiB      0.0 MiB           1       s = 0
     8     24.0 MiB      0.0 MiB      100001       for i in my_list:
     9     24.0 MiB      0.0 MiB      100000           if i % 2 != 0:
    10     24.0 MiB      0.0 MiB       50000               s += my_list[i]
    11     22.2 MiB     -1.8 MiB           1       my_list = None  ## переобределяем на None , чтоб высвободить память
    12     22.2 MiB      0.0 MiB           1       return s
"""