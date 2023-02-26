import json
import file_func as ff


# Структура словаря:
# id - int
#     Вложенный словарь:
#         Имя - строка
#         Фамилия - строка
#         Телефон - список

def add():
    directory = ff.load()
    
    keys=[]
    for i in directory.keys():
        keys.append(i)
        
    keys.sort()

    def next_key():
        count = 1
        for i in keys:
            i = int(i)
            if count == i:
                count += 1
            else:
                break
        return count

    print(f'ID новой записи {next_key()}')
    name = ''
    surname = ''
    phone = []

    for i in range(4):
        if i == 1:
            name = input('Введите имя: ')
        elif i == 2:
            surname = input('Введите фамилию: ')
        elif i == 3:
            phone.append(input('Введите номер телефона: '))
            again = input('Хотите добавить еще номер? Да/Нет  ')
            if again == 'Да':
                phone.append(input('Введите номер телефона: '))
            else:
                print('Добавление закончено')

    directory[next_key()] = {
        'Имя': name,
        'Фамилия': surname,
        'Телефон': phone
    }
    ff.save()


# add() #for test
