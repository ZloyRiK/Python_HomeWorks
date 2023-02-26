import file_func as ff

# Команда /find

def find(value):
    directory = ff.load()
    cs = 0  # Контрольная сумма
    sm = 0  # Сумма несоответствий
    for k, info in directory.items():
        name = info['Имя']
        surname = info['Фамилия']
        phone = info['Телефон']
        if value == name or value == surname:
            print(f'id {k}: \n{name} {surname}')
            for i in phone:
                print(i)
            cs += 1
            # break
        elif value in phone:
            print(f'id {k}: \n{name} {surname}')
            for i in phone:
                print(i)
            cs += 1
        else:
            cs += 1
            sm += 1
    if cs == sm:
        print("Записи с такими данными не найдено. Проверьте корретность ввода")
