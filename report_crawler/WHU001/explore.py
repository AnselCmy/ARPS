# -*- coding:utf-8 -*-

import re


def sub_linefeed(text):
	sub_text = ''
	for line in text.splitlines():
		line = line.rstrip()
		if line != '':
			line += '\n'
		sub_text += line
	return sub_text


def connect_messages(messages, mode):
	text = ''
	if mode == 'start':
		for message in messages[1:]:
			text += message.strip()
	else:
		for message in messages[:-1]:
			text += message.strip()
	return text


def get_information(text):
	text = text.decode('utf-8')
	messages = {}

	# title
<<<<<<< HEAD
	title_pattern = re.compile(u"(?:题(?:.*?){0,1}目|主(?:.*?){0,1}题|Title)[：:. ](.*?)\n")
=======
	title_pattern = re.compile(u"题(?:.*?){0,1}目[：:. ](.*?)\n")
>>>>>>> LJY
	messages['title'] = re.findall(title_pattern, text)
	if len(messages['title']) == 1:
		messages['title'] = messages['title'][0].strip()
	else:
		messages['title'] = ''

	# time
	time_pattern = re.compile(u"时(?:.*?){0,1}间[：:. ](.*?)\n")
	messages['time'] = re.findall(time_pattern, text)
	if len(messages['time']) == 1:
		messages['time'] = messages['time'][0].strip()
	else:
		messages['time'] = ''

	# address
	address_pattern = re.compile(u"地(?:.*?){0,1}点[：:.](.*?)\n")
	messages['address'] = re.findall(address_pattern, text)
	if len(messages['address']) == 1:
		messages['address'] = messages['address'][0].strip()
	else:
		messages['address'] = ''

	# speaker
<<<<<<< HEAD
	speaker_pattern = re.compile(u"(?:主(?:.*?){0,1}讲|报(?:.*?){0,1}告)(?:.*?){0,1}人[：:.](.*?)\n")
=======
	speaker_pattern = re.compile(u"(?:(?:主(?:.*?){0,1}讲|报(?:.*?){0,1}告)(?:.*?){0,1}人|嘉(?:.*?){0,1}宾)[：:.](.*?)\n")
>>>>>>> LJY
	messages['speaker'] = re.findall(speaker_pattern, text)
	if len(messages['speaker']) == 1:
		messages['speaker'] = messages['speaker'][0].strip()
	else:
		messages['speaker'] = ''

	# abstract
<<<<<<< HEAD
	abstract_pattern = re.compile(u"(?:摘要|内容|内容简介|Bio)[：:.]([\s\S]*)(?:(?:(?:报告|主讲)人(?:简介|介绍))|Abstract)[：:.]", re.S)
=======
	abstract_pattern = re.compile(u"(?:摘要|内容|Abstract)[：:.】]([\s\S]*)(?:(?:(?:报告|主讲)人|嘉宾)(?:简介|介绍)|Bio|Biography)[：:.】]", re.S)
>>>>>>> LJY
	messages['abstract'] = re.findall(abstract_pattern, text)
	if len(messages['abstract']) == 1:
		messages['abstract'] = sub_linefeed(messages['abstract'][0].strip())
	else:
<<<<<<< HEAD
		abstract_pattern = re.compile(u"(?:摘要|内容|内容简介|Bio)[：:.]([\s\S]*)", re.S)
=======
		abstract_pattern = re.compile(u"(?:摘要|内容|Abstract)[：:.】]([\s\S]*)", re.S)
>>>>>>> LJY
		messages['abstract'] = re.findall(abstract_pattern, text)
		if len(messages['abstract']) == 1:
			messages['abstract'] = sub_linefeed(messages['abstract'][0].strip())
		else:
			messages['abstract'] = ''
<<<<<<< HEAD
	if re.search(u"[五六七八九][、.]", messages['abstract']) != None:
		messages['abstract'] = re.findall(u"([\s\S]*)[五六七八九][、.]", messages['abstract'], re.S)[0]
	elif re.search(u"主办单位", messages['abstract']) != None:
		messages['abstract'] = re.findall(u"([\s\S]*)主办单位", messages['abstract'], re.S)[0]


	# biography
	biography_pattern = re.compile(u"(?:人(?:简介|介绍)|Abstract)[：:.]([\s\S]*)(?:(?:报告|讲座|内容)(?:摘要|内容|简介)|Bio)[：:.]", re.S)
=======
	if re.search(u"[【】]", messages['abstract']) is not None:
		messages['abstract'] = re.sub(u"[【】]", '', messages['abstract'])

	# biography
	biography_pattern = re.compile(u"(?:(?:人|嘉宾)(?:简介|介绍)|Bio|Biography)[：:.】]([\s\S]*)(?:(?:报告|讲座|内容)(?:摘要|简介)|Abstract)[：:.】]", re.S)
>>>>>>> LJY
	messages['biography'] = re.findall(biography_pattern, text)
	if len(messages['biography']) == 1:
		messages['biography'] = sub_linefeed(messages['biography'][0].strip())
	else:
<<<<<<< HEAD
		biography_pattern = re.compile(u"(?:人(?:简介|介绍)|Abstract)[：:.]([\s\S]*)", re.S)
=======
		biography_pattern = re.compile(u"(?:(?:人|嘉宾)(?:简介|介绍)|Bio|Biography)[：:.】]([\s\S]*)", re.S)
>>>>>>> LJY
		messages['biography'] = re.findall(biography_pattern, text)
		if len(messages['biography']) == 1:
			messages['biography'] = sub_linefeed(messages['biography'][0].strip())
		else:
			messages['biography'] = ''
<<<<<<< HEAD
	if re.search(u"[五六七八九][、.]", messages['biography']) != None:
		messages['biography'] = re.findall(u"([\s\S]*)[五六七八九][、.]", messages['biography'], re.S)[0]
	elif re.search(u"主办单位", messages['biography']) != None:
		messages['biography'] = re.findall(u"([\s\S]*)主办单位", messages['biography'], re.S)[0]

	print messages['abstract']
	return messages


f = open('13.txt', 'r').read()
=======
	if re.search(u"[【】]", messages['biography']) is not None:
		messages['biography'] = re.sub(u"[【】]", '', messages['biography'])

	print messages['biography']
	return messages


f = open('18.txt', 'r').read()
>>>>>>> LJY
dict = get_information(f)
print f

