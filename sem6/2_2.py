from memory_profiler import profile


@profile
def pair():
    my_list = list(range(100000))  ## берем массив побольше
    out_list = []
    for i in range(int(len(my_list) / 2)):
        out_list.append(my_list[i] * my_list[len(my_list) - 1 - i])
    del my_list  ##удаляем ненужный массив
    return out_list


pair()

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     20.2 MiB     20.2 MiB           1   @profile
     5                                         def pair():
     6     24.0 MiB      3.8 MiB           1       my_list = list(range(100000))  ## берем массив побольше
     7     24.0 MiB      0.0 MiB           1       out_list = []
     8     26.3 MiB      1.6 MiB       50001       for i in range(int(len(my_list) / 2)):
     9     26.3 MiB      0.8 MiB       50000           out_list.append(my_list[i] * my_list[len(my_list) - 1 - i])
    10     24.1 MiB     -2.3 MiB           1       del my_list  ##удаляем ненужный массив
    11     24.1 MiB      0.0 MiB           1       return out_list
"""
## После того как массив my_list стал не нужен для вычисления я его удалил, чтоб высвободить память
