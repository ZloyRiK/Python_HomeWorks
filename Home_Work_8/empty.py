import json


directory={}

def save():
    with open('directory.json', 'w', encoding='utf-8') as ds:
        ds.write(json.dumps(directory, ensure_ascii=False, sort_keys=True))

# save()
