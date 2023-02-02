# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

from random import randint

print()
n = int (input("Введите количество моенток "))
count_0 = 0
count_1 = 0

coins = [randint(0,1) for i in range(n)]
    
print (coins)

for i in coins:
    if i==0:
        count_0+=1
    else:
        count_1+=1
print()
if count_0<count_1:
    print(count_0)
else:
    print(count_1)

print()