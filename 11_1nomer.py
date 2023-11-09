# 11 лабораторная, 4 вариант: транспонировать матрицу
from random import * # добавление функции рандома
n = int(input()) # считывание размерности матрицы
a = [[randint(1, 21) for j in range(n)] for i in range(n)] # заполнение матрицы рандомными числами, a = [[1, 2, 3], [2, 4, 5], [3, 5, 6]] 
for i in range(len(a)): # вывод матрицы без изменений
    for j in range(len(a[i])):
        print(a[i][j], end=' ') 
    print()

print( ) 
for i in range(len(a)): # вывод матрицы, но номер строки меняется на номер столбца 
    for j in range(len(a[i])):
        print(a[j][i], end=' ')
    print()