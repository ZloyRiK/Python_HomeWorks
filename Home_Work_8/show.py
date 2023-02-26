import file_func as ff  

def show():
    directory = ff.load()
    for k, v in directory.items():
            name=v['Имя']
            surname = v['Фамилия']
            phone = v['Телефон']
            print (f'ID {k} \nИмя: {name} \nФамилия: {surname} \nТелефоны: {phone}')