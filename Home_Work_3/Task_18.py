# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел A i
# . Последняя строка
# содержит число X

from random import randint

print()
n = int(input("Введите колличество элементов массива "))
k = int(input("Возле какого значения ищем элемент? "))

mass = [randint(0, 9) for i in range(n)]

print(mass)
print()

res = mass[0]

for i in mass:
    if ((abs(i-k)) < (abs(res-k))) and i != k:
        res = i


print(f"Ближайшее по значению число в массиве {res}")
print()