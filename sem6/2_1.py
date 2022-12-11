from memory_profiler import profile


@profile
def sum_list():
    my_list = list(range(100000))  ## берем массив побольше
    s = 0
    for i in my_list:
        if i % 2 != 0:
            s += my_list[i]
    my_list = None  ## переопределяем на None , чтоб высвободить память
    return s


sum_list()

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     20.1 MiB     20.1 MiB           1   @profile
     5                                         def sum_list():
     6     23.9 MiB      3.8 MiB           1       my_list = list(range(100000))  ## берем массив побольше
     7     23.9 MiB      0.0 MiB           1       s = 0
     8     23.9 MiB      0.0 MiB      100001       for i in my_list:
     9     23.9 MiB      0.0 MiB      100000           if i % 2 != 0:
    10     23.9 MiB      0.0 MiB       50000               s += my_list[i]
    11     22.1 MiB     -1.8 MiB           1       my_list = None  ## переопределяем на None , чтоб высвободить память
    12     22.1 MiB      0.0 MiB           1       return s
"""
## после того как массив my_list стал не нужен я переопределил его в None,
## чтоб-бы не расходовать память