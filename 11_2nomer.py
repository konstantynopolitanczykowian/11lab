# 11 лабораторная, 3 вариант: является ли матрица симметричной относительно главной диагонали
from random import * # добавление функции рандома
n = int(input()) # считывание размерности матрицы
a = [[randint(1, 21) for j in range(n)] for i in range(n)] # заполнение матрицы рандомными числами, a = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
b = 0 # ввод дополнительной переменной
for i in range(len(a)): # вывод матрицы
    for j in range(len(a[i])):
        print(a[i][j], end=' ') 
    print()
for i in range(len(a)): # цикл проверяет условие для всех чисел матрицы
    for j in range(len(a[i])):
        if a [i][j] != a [j][i]: #проверяется являются ли одинаковыми числа, у которых номер строки одного числа и номер столбца другого одинаковые и наоборот
            b = 1    # если матрица несимметрична переменная меняется

if b == 0: # если переменная не изменяется выводится информация о том, что матрица симметрична
    print('Матрица симметрична')
else: # переменная изменяется, выводится, что матрица несимметрична
    print('Матрица несимметрична') 