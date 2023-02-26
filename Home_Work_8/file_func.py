import json

def load():
    global directory
    with open('directory.json', 'r', encoding='utf-8') as dl:
        directory = json.load(dl)
    return directory

def save():
    with open('directory.json', 'w', encoding='utf-8') as dl:
        dl.write(json.dumps(directory, ensure_ascii=False))

def save_sort():
    with open('directory.json', 'w', encoding='utf-8') as dl:
        dl.write(json.dumps(directory, ensure_ascii=False, sort_keys=True))
