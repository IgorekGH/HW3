# Задача 2.
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5 - n
# 1 2 3 4 5 - a
# 6 - x
# -> 5


array = []
n = int(input('Введите количество элементов в массиве: '))
for i in range(1,n+1):
    a = int(input('Введите число: '))
x = int(input('Введите число x: '))
if(x) < array[i]:
    (x-1)
    if(x) > array[i]:
        (x+1)
print((x+1) & (x-1))

