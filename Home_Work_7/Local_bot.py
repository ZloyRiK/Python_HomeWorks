from random import *
import json

films = []
bot_commands = ['/start', '/stop', '/add',
                '/show', '/delete', '/random', '/help']


def save():
    with open("films.json", 'w', encoding='utf-8') as ts:
        ts.write(json.dumps(films, ensure_ascii=False))
        # print('Список фильмов сохранен в файл')


# def load():
#     with open("films.json", 'r', encoding='utf-8') as tr:
#         films=json.load(tr)
#     print('Фильмы из файла загружены')

# Пока не придумал как наладить эту функцию
    
try:
    with open("films.json", 'r', encoding='utf-8') as tr:
        films=json.load(tr)
        print('Список фильмов успешно загружен')
except:
    print('Нет сохраненного файла')


while True:
    command = input('Введите команду ')
    if command == '/start':
        print('Бот запущен')
    elif command == '/stop':
        if not films:
            print('Бот остановлен \nСписок фильмов для сохранения пуст')
        else:
            save()
            print ('Бот остановлен \nСписок фильмов сохранен')
        break
    elif command == '/show':
        with open("films.json", 'r', encoding='utf-8') as tr:
            films=json.load(tr)
        print('Сейчас в списке следующие фильмы: ')
        for i in films:
            print(i)
    elif command == '/add':
        af= input('Введите название фильма, который будете смотреть: ')
        if af in films:
            print('Этот фильм уже в списке')
        else:
            films.append(af)
            save()
            print('Фильм добавлен')
    elif command == '/delete':
        d = input('Введите название фильма, чтобы убрать из списка ')
        try:
            films.remove(d)
            print('Фильм удален.\nСписок оставшихся фильмов: ')
            for i in films:
                print(i)
        except:
            print(
                'Такого фильма нет или допущена ошибка при вводе. \nПроверьте ввод и повторите команду')
        save()
    elif command == '/random':
        print(f'Попробуйте посмотреть: {choice(films)}')
    elif command == '/help':
        print('Список доступных команд: ')
        for i in bot_commands:
            print(i)
    else:
        print('Неизвестная комманда. Напишите /help для справки')
