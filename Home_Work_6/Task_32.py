# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)


from random import randint

min = int(input('\nВведите нижний диапазон поиска '))
max = int(input('Введите верхний диапазон поиска '))
n = int(input('Введите размер массива '))

a = list()


for i in range(n):
    a.append(randint(-20, 20))

print('\n', a)

res = list()

for i in range(len(a)):
    if a[i] >= min and a[i] <= max:
        res.append(i)

print(f'\nВаш массив с результатами {res}\n')
