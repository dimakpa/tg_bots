import json
#дозапись текста в текстовый файл

path = 'ParsTG.json'
limit_user = 10
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)


    datas = data[1]
    print(int(datas['media']['photo']['id']))

