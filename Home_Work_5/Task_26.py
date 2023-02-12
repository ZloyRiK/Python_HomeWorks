# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

n = int(input("\nВведите число "))
m= int (input("Введите степень числа "))

def to_the_power (n, m):
    if m ==0:
        return 1
    else:
        return n*to_the_power(n,m-1)
    
print (f"\n{n}**{m} = {to_the_power(n,m)} \n")