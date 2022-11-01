from translate import Translator
translators = Translator(from_lang="en", to_lang="russian")
en_message = open('ParsTG_Text.txt', 'r', encoding='utf-8')
en_message_pice = en_message.read()
ru_message = translators.translate(en_message_pice[0:500])


with open('Russian_text.txt', 'a', encoding='utf-8') as file:
    file.write(ru_message)
#print(ru_message)

# en_messages = en_message.read()
# print(en_message.read())

