import json
#дозапись текста в текстовый файл

path = 'ParsTG.json'
limit_user = 10
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)
f = open('English_text.txt', 'w', encoding='utf-8')
for txt in data:
    f.write(txt['message'])
    print(txt['message'])




    # with open('English_text.txt', 'a', encoding='utf-8') as file:
    #     file.write(txt['message'])
    #     print(txt['message'])

