# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника)

print()
n = int (input("Сколько долек на первой стороне? "))
m = int (input("Сколько долек на второй стороне? "))
k = int (input("Сколько долек хотите отломить? "))

print()
if k%m==0 or k%n==0 and k<m*n:
    print ('Ломай смело, у тебя все получится')
else:
    print ('Эта шоколадка так не делится, отдай ее мне, а себе купи другую')
    
print()