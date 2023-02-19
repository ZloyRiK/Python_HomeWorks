# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке

is_song = lambda song: True if ' ' in song else False

phrases = lambda song: song.split(' ')

check_res = lambda syllable: print('\nПам парам\nОпилки же в голове') if len(syllable) > 1 else print('\nПарам пам-пам\nА это звучит')

def count_syllable(phrases):
    vowels = 'аеёиоуыэюя' # гласные
    syllables = set()
    for phrase in phrases:
        count_syllable = int() # счетчик слогов
        for char in phrase:
            if char in vowels:
                count_syllable += 1
        syllables.add(count_syllable)
    return syllables

def input_song(): # main function
    song = input('\nВведи сюда свой стих: ')
    if is_song(song):
        check_res(count_syllable(song.split(' ')))
    else:
        print('Это не стихотворение\n')
        input_song()


input_song()