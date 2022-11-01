#https://proglib.io/p/pishem-prostoy-grabber-dlya-telegram-chatov-na-python-2019-11-06 - cod from
#https://t.me/joinchat/AAAAAEF89LGv7F_CuAnoTQ - for check


import time
import telebot
#from translate import Translator
import keys


from telethon.sync import TelegramClient
from telethon import connection



# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest

api_id   = '1911521'
api_hash ='8a552b27e4486e58aba3166ccda35e1b'
username ='debocherry'
bot_token = '1356430120:AAENZ3Hgd1-8h76u8ldnD5cOgu6WxbY0fjM'


client = TelegramClient(username, api_id, api_hash)
client.start()



async def dump_all_messages(channel):
	"""Записывает json-файл с информацией о всех сообщениях канала/чата"""
	offset_msg = 0   # номер записи, с которой начинается считывание

	limit_msg = 1   # максимальное число записей, передаваемых за один раз, НУЖНО МЕНЯТЬ ЭТО

	all_messages = []   # список всех сообщений
	total_messages = 0
	total_count_limit = 3  # поменяйте это значение, если вам нужны не все сообщения



	while True:
		history = await client(GetHistoryRequest(
			peer=channel,
			offset_id=offset_msg,
			offset_date=None, add_offset=0,
			limit=limit_msg, max_id=0, min_id=0,
			hash=0))
		if not history.messages:
			break

		messages = history.messages

		for message in messages:
			#all_messages.append(message.to_dict())
			print(message.id)



			bot = telebot.TeleBot(bot_token)
			text_id = message.id
			bot.forward_message(chat_id='@pandaas_music', from_chat_id = '@musiclullaby', message_id= text_id)



			# Время между постами
			time.sleep(1)




		# offset_msg = messages[len(messages) - 1].id
		# total_messages = len(all_messages)
		# if total_count_limit != 0 and total_messages >= total_count_limit:
		# 	break


async def main():
	#url = input("Введите ссылку на канал или чат: ")
	url = "https://t.me/musiclullaby"
	channel = await client.get_entity(url)
	await dump_all_messages(channel)






with client:
	client.loop.run_until_complete(main())


#https://t.me/mmmwwwi
#https://t.me/corleone666
#https://t.me/boilingmephi
#что-то на английском https://t.me/wannabeyourfavorite
#цитаты на английском https://t.me/englishscitat

#https://t.me/lizardofthestreet - полностью на английском!
#https://t.me/musiclullaby
