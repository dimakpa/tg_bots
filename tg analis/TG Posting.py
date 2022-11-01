#https://proglib.io/p/pishem-prostoy-grabber-dlya-telegram-chatov-na-python-2019-11-06 - cod from
#https://t.me/joinchat/AAAAAEF89LGv7F_CuAnoTQ - for check


import time
import telebot
#from translate import Translator
import keys
import configparser
import json

from telethon.sync import TelegramClient
from telethon import connection

# для корректного переноса времени сообщений в json
from datetime import date, datetime

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest




client = TelegramClient(keys.username, keys.api_id, keys.api_hash)
client.start()

async def dump_all_participants(channel):
	"""Записывает json-файл с информацией о всех участниках канала/чата"""
	offset_user = 0    # номер участника, с которого начинается считывание
	limit_user = 10   # максимальное число записей, передаваемых за один раз

	all_participants = []   # список всех участников канала
	filter_user = ChannelParticipantsSearch('')

	while True:
		participants = await client(GetParticipantsRequest(channel,
			filter_user, offset_user, limit_user, hash=0))
		if not participants.users:
			break
		all_participants.extend(participants.users)
		offset_user += len(participants.users)

	all_users_details = []   # список словарей с интересующими параметрами участников канала

	for participant in all_participants:
		all_users_details.append({
			"id": participant.id,
			"first_name":  participant.first_name,
			"last_name":  participant.last_name,
			"user": participant.username,
			"phone": participant.phone,
			"is_bot": participant.bot})

	with open('channel_users.json', 'a', encoding='utf8') as outfile:
		json.dump(all_users_details, outfile, ensure_ascii=False)


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

		t = open('Russian_text.txt', 'a', encoding='utf-8')
		messages = history.messages
		#translators = Translator(from_lang="en", to_lang="russian")
		for message in messages:
			all_messages.append(message.to_dict())
			print(message.message)
			# if len(message.message) <=500:
			# 	en_message_pice = message.message
			# 	ru_message = translators.translate(en_message_pice[0:500])
			#
			#
			# elif len(message.message)<= 1000:
			# 	#Переводит часть и дозаписывает в блокнот по частям
			# 	en_message_pice = message.message[0:500]
			# 	ru_message1 = translators.translate(en_message_pice)
			#
			# 	en_message_pice = message.message[500:1000]
			# 	ru_message2 = translators.translate(en_message_pice)
			#
			# 	ru_message = ru_message1 + ru_message2
			#
			#
			# elif len(message.message)<=1500:
			# 	en_message_pice = message.message[0:500]
			# 	ru_message1 = translators.translate(en_message_pice)
			#
			# 	en_message_pice = message.message[500:1000]
			# 	ru_message2 = translators.translate(en_message_pice)
			#
			# 	en_message_pice = message.message[1000:1500]
			# 	ru_message3 = translators.translate(en_message_pice)
			#
			# 	ru_message = ru_message1 + ru_message2+ ru_message3

			#t.write(ru_message)
			t.write(message.message)

			# Открывает файл с русским текстом и выкладывает в канал
			bot = telebot.TeleBot(keys.bot_token)
			text_from_file = open('Russian_text.txt', 'r', encoding='utf-8')
			text_now = text_from_file.read()
			bot.send_message(chat_id='@pandaas_music', text=text_now)
			# Очищаем файл от предыдущей записи
			f = open('Russian_text.txt', 'w+')
			f.seek(0)

			# Время между постами
			time.sleep(15)




		offset_msg = messages[len(messages) - 1].id
		total_messages = len(all_messages)
		if total_count_limit != 0 and total_messages >= total_count_limit:
			break


async def main():
	#url = input("Введите ссылку на канал или чат: ")
	url = "https://t.me/lizardofthestreet"
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
