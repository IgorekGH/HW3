# Задача 1.
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример
# 5
# 1 2 3 4 5
# 3
# -> 1

array = []
n = int(input('Введите количество элементов в массиве: '))
for i in range(1,n+1):
    a = int(input('Введите число: '))
    array.append(a)
x = int(input('Введите число x: '))
print("Число x встречается в массиве: ", array.count(x))
