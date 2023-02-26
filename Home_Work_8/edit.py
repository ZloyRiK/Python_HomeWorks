import file_func as ff

# directory = ff.load()

# id = input('Введите ID записи для изменения: ')

# print(f'\n {directory[id]}')

def change(id):
    directory = ff.load()
    value = input('Ваша команда: ')
    if value == 'Имя':
        new_value = input('Введите новое значение: ')
        directory[id]['Имя']=new_value
        print(directory[id]['Имя'])
    elif value == 'Фамилия':
        new_value = input('Введите новое значение: ')
        directory[id]['Фамилия']=new_value
        print (directory[id]['Фамилия'])
    elif value=='Телефон':
        n=0
        for i in directory[id]['Телефон']:
            n+=1
            print(f'Номер {n}: {i}')
        phone_id=int(input('Выберите id номера телефона для изменения: '))
        new_value = input('Введите новое значение: ')
        directory[id]['Телефон'].pop(phone_id-1)
        directory[id]['Телефон'].insert(phone_id-1, new_value)
    elif value == 'Добавить':
        new_value = input('Введите номер для добавления: ')
        directory[id]['Телефон'].append(new_value)
    elif value == 'Удалить':
        del directory[id]
    else:
        print ("Неизвестная команда")
    ff.save()

# print(change(id))

# print(f'\n {directory[id]}')
