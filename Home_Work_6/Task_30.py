# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input('\nУкажите начало прогрессии '))
b = int(input('Укажите шаг прогрессии '))
n = int(input('Сколько нужно элементов '))

array = list()

for i in range(n):
    array.append(a)
    a=a+b
    
    
print(f'\nВаш массив {array}\n')