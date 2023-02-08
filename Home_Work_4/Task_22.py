# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

print()
m = int(input("Введите размер первого набора чисел "))
n = int(input("Введите размер второго набора чисел "))
print()

start_arr_m = list()
start_arr_n = list()


print("Ввод элементов множества m:")  
for i in range(m):
    # start_arr_m.append(randint(0,9))
    start_arr_m.append(int(input()))

print()
print("Ввод элементов множества n:")  
for i in range(n):
    # start_arr_n.append(randint(0,9))
    start_arr_n.append(int(input()))
    

    
m_set = set(start_arr_m)
n_set = set(start_arr_n)

# print()
# print(f'Получены 2 множества: \n{m_set} \n{n_set}')

final_set = set(m_set.intersection(n_set))

final_set=list(final_set)
temp = 0

for i in range(len(final_set)-1):
    for j in range(len(final_set)-i-1):
        if final_set[j]>final_set[j+1]:
            temp=final_set[j]            #Bubble_sort
            final_set[j]=final_set[j+1]  # final_set[j], final_set[j+1] = final_set[j+1], final_set[j]
            final_set[j+1]=temp
            

print()
print(final_set)
print()