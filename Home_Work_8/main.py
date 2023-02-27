import json
from search import find
import file_func as ff
import add, edit, show, empty, dict_sort

 
try:
    directory = ff.load()
    print ("Список контактов успешно загружен")
except:
    print('Не удалось загрузить файл или файл отсутствует \nСоздайте первую запись')
    empty.save()
    
help = 'Список команд: \n/start - Запуск программы  \n/stop - Остановка программы \n/show - Показать все записи в телефонной книге \n/add - добавить новую запись \n/find - поиск контакта \n/edit - изменение и удаление данных \n/help - список команд'

print(help)

while True:
    comand=input('Введите команду ')
    if comand == '/start':
        print ("Справочник готов к работе")
    elif comand == "/stop":
        if not directory:
            print("Программа остановлена")
        else:
            try:
                dict_sort.sorting()
            except:
                ff.save()
            print("Программа остановлена. Все изменения сохранены")
        break
    elif comand== '/add':
        add.add()
    elif comand=='/show':
        show.show() 
    elif comand == '/find':
        f = input("Введите фамилию, имя или номер телефона: ")
        find(f)
    elif comand == '/edit':
        id = input('Введите ID записи для изменения: ')
        print('Доступные команды:'
          +'\nИмя - изменить имя контакта'
          +'\nФамилия - изменить фамилию контакта'
          +'\nТелефон - изменить или удалить один из номеров контакта'
          +'\nДобавить - добавить еще один номер контакту'
          +'\nУдалить - удалить выбранный контакт')
        edit.change(id)
        print ('Запись изменена')
    # elif comand == "/sort":
    #     dict_sort.sorting()
    elif comand == '/help':
        print(help)
    else:
        print ('Неизвестная команда \nДля открытия меню команд напишите /help')