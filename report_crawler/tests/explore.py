# -*- coding:utf-8 -*-

import re
import time
import chardet
import HTMLParser
import datetime
from report_crawler.spiders.__Global_function import get_localtime


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





def Filter(text, ab_sign=0):
	# title
	if re.search(u"(((报((?![\u4e00-\u9fa5])[\W])*告|讲((?![\u4e00-\u9fa5])[\W])*座|演((?![\u4e00-\u9fa5])[\W])*讲)*(主((?![\u4e00-\u9fa5])[\W])*题|题((?![\u4e00-\u9fa5])[\W])*目|标((?![\u4e00-\u9fa5])[\W])*题))([ (（](Title|Topic))*|Title|Topic)[）) ]*[：:.]+", text) is not None:
		text = re.sub(u"(((报((?![\u4e00-\u9fa5])[\W])*告|讲((?![\u4e00-\u9fa5])[\W])*座|演((?![\u4e00-\u9fa5])[\W])*讲)*(主((?![\u4e00-\u9fa5])[\W])*题|题((?![\u4e00-\u9fa5])[\W])*目|标((?![\u4e00-\u9fa5])[\W])*题))([ (（](Title|Topic))*|Title|Topic)[）) ]*[：:.]+[\s\S]*", '', text)

	# time
	if re.search(u"(((报((?![\u4e00-\u9fa5])[\W])*告|讲((?![\u4e00-\u9fa5])[\W])*座)*(日期及)*(时((?![\u4e00-\u9fa5])[\W])*间|日((?![\u4e00-\u9fa5])[\W])*期))([ (（]Time)*|Time)[）) ]*[：:.]+", text) is not None:
		text = re.sub(u"(((报((?![\u4e00-\u9fa5])[\W])*告|讲((?![\u4e00-\u9fa5])[\W])*座)*(日期及)*(时((?![\u4e00-\u9fa5])[\W])*间|日((?![\u4e00-\u9fa5])[\W])*期))([ (（]Time)*|Time)[）) ]*[：:.]+[\s\S]*", '', text)

	# address
	if re.search(u"(((报((?![\u4e00-\u9fa5])[\W])*告|讲((?![\u4e00-\u9fa5])[\W])*座)*地((?![\u4e00-\u9fa5])[\W])*点)([ (（](Address|Venue|Location|Meeting Room|Place))*|Address|Venue|Location|Meeting Room|Place)[）) ]*[：:.]+", text) is not None:
		text = re.sub(u"(((报((?![\u4e00-\u9fa5])[\W])*告|讲((?![\u4e00-\u9fa5])[\W])*座)*地((?![\u4e00-\u9fa5])[\W])*点)([ (（](Address|Venue|Location|Meeting Room|Place))*|Address|Venue|Location|Meeting Room|Place)[）) ]*[：:.]+[\s\S]*", '', text)

	# speaker
	#if re.search(u"(((讲((?![\u4e00-\u9fa5])[\W])*授|演((?![\u4e00-\u9fa5])[\W])*讲|报((?![\u4e00-\u9fa5])[\W])*告|主((?![\u4e00-\u9fa5])[\W])*讲)((?![\u4e00-\u9fa5])[\W])*(人|专((?![\u4e00-\u9fa5])[\W])*家|嘉((?![\u4e00-\u9fa5])[\W])*宾)|讲((?![\u4e00-\u9fa5])[\W])*(师|者)|主((?![\u4e00-\u9fa5])[\W])*讲)([ (（]Speaker)*|Speaker)[）) ]*[：:.]+", text) is not None:
	#	text = re.sub(u"(((讲((?![\u4e00-\u9fa5])[\W])*授|演((?![\u4e00-\u9fa5])[\W])*讲|报((?![\u4e00-\u9fa5])[\W])*告|主((?![\u4e00-\u9fa5])[\W])*讲)((?![\u4e00-\u9fa5])[\W])*(人|专((?![\u4e00-\u9fa5])[\W])*家|嘉((?![\u4e00-\u9fa5])[\W])*宾)|讲((?![\u4e00-\u9fa5])[\W])*(师|者)|主((?![\u4e00-\u9fa5])[\W])*讲)([ (（]Speaker)*|Speaker)[）) ]*[：:.]+[\s\S]*", '', text)

	# abstract
	if re.search(u"(((报告|讲座|内容)*(主要)*(摘要|内容|提要)|(报告|讲座|内容)简介)([ (（]Abstract)*|Abstract)[）) ]*[：:.]+", text) is not None:
		text = re.sub(u"(((报告|讲座|内容)*(主要)*(摘要|内容|提要)|(报告|讲座|内容)简介)([ (（]Abstract)*|Abstract)[）) ]*[：:.]+[\s\S]*", '', text)

	# biography
	if re.search(u"((((讲座|主讲|报告|演讲|讲)(者|人|师|专家|嘉宾)|个人)|.*?(教授|院士|博士))(及其)*(简介|介绍|简历)([ (（](Biography|Bio|Short-Biography|Short bio))*|Biography|Bio|Short-Biography|Short bio)[）) ]*[：:.]+", text) is not None:
		text = re.sub(u"((((讲座|主讲|报告|演讲|讲)(者|人|师|专家|嘉宾)|个人)|.*?(教授|院士|博士))(及其)*(简介|介绍|简历)([ (（](Biography|Bio|Short-Biography|Short bio))*|Biography|Bio|Short-Biography|Short bio)[）) ]*[：:.]+[\s\S]*", '', text)

	# chairman
	if re.search(u"主((?![\u4e00-\u9fa5])[\W])*持((?![\u4e00-\u9fa5])[\W])*(人)*([ (（]Chair)*[）) ]*[：:.]+", text) is not None:
		text = re.sub(u"主((?![\u4e00-\u9fa5])[\W])*持((?![\u4e00-\u9fa5])[\W])*(人)*([ (（]Chair)*[）) ]*[：:.]+[\s\S]*", '', text)

	# invitee
	if re.search(u"邀((?![\u4e00-\u9fa5])[\W])*请((?![\u4e00-\u9fa5])[\W])*人([ (（]Invitee)*[）) ]*[：:.]+", text) is not None:
		text = re.sub(u"邀((?![\u4e00-\u9fa5])[\W])*请((?![\u4e00-\u9fa5])[\W])*人([ (（]Invitee)*[）) ]*[：:.]+[\s\S]*", '', text)

	# others
	if re.search(u"欢迎(各位|广大)", text) is not None:
		text = re.sub(u"欢迎(各位|广大)[\s\S]*", '', text)
	if re.search(u"报((?![\u4e00-\u9fa5])[\W])*告((?![\u4e00-\u9fa5])[\W])*([一二三四五]|[\d])[ ]*[：:.]*", text) is not None:
		text = re.sub(u"报[ ]*告[ ]*([一二三四五]|[\d])[ ]*[：:.]*[\s\S]*", '', text)
	if re.search(u"查看次数[：:.]", text) is not None:
		text = re.sub(u"查看次数[：:.][\s\S]*", '', text)
	if re.search(u"附件下载[：:.]", text) is not None:
		text = re.sub(u"附件下载[：:.][\s\S]*", '', text)
	if re.search(u"(主办|讲座|报告|演讲)(人)*(单位|企业)[：:.]", text) is not None:
		text = re.sub(u"(主办|讲座|报告|演讲)(人)*(单位|企业)[：:.][\s\S]*", '', text)
	if re.search(u"[一二三四五六七八九][、.]", text) is not None:
		text = re.sub(u"[一二三四五六七八九][、.][\s\S]*", '', text)
	if re.search(u"请我院相关[\s\S]*", text) is not None:
		text = re.sub(u"请我院相关[\s\S]*", '', text)

	return text


class testing():
	def __init__(self):
		self.now_time = time.strftime("%Y-%m-%d", time.localtime())

		self.month_E2C = {
			'Jan': '1',
			'Feb': '2',
			'Mar': '3',
			'Apr': '4',
			'May': '5',
			'June': '6',
			'July': '7',
			'Aug': '8',
			'Sept': '9',
			'Oct': '10',
			'Nov': '11',
			'Dec': '12'
		}

		self.week2day = {
			u'一': '1',
			u'二': '2',
			u'三': '3',
			u'四': '4',
			u'五': '5',
			u'六': '6',
			u'七': '7',
			u'日': '7',
			u'天': '7',
			u'末': '7'
		}

	# day
	def get_day(self, text):
		day = re.search(u"[\d]*((?![\u4e00-\u9fa5])[\W])*(?=(日|号))", text)
		if day is not None:
			day = day.group()
		else:
			Eng_day = re.search(u"(?<=(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))[\s\S]*", text)
			if Eng_day is not None:
				day = re.search(u"[0-9]{1,}", Eng_day.group())
				if day is not None:
					day = day.group()

		return day

	# month
	def get_month(self, text, day):
		month = re.search(u"[\d]*((?![\u4e00-\u9fa5])[\W])*(?=月)", text)
		if month is not None:
			month = month.group()
		else:
			month_pattern = re.compile(u"Jan|Feb|Mar|Apr|May|June|July|Aug|Sept|Oct|Nov|Dec")
			month = re.search(month_pattern, text)
			if month is not None:
				month = self.month_E2C[month.group()]
			elif day is not None:
				now_day = int(self.now_time.split('-')[-1])
				now_month = int(self.now_time.split('-')[-2])
				if int(day) < now_day:
					month = str(now_month + 1)
				else:
					month = str(now_month)

		return month

	# year
	def get_year(self, text, day, month):
		year = re.search(u"[\d]*((?![\u4e00-\u9fa5])[\W])*(?=年)", text)
		if year is not None:
			year = year.group()
			if len(year.strip()) < 4:
				year = "20" + year
		elif day is not None and month is not None:
			now_year = int(self.now_time.split('-')[0])
			now_month_day = int(str(get_localtime(self.now_time))[4:])
			report_month_day = int(month) * 100 + int(day)
			if report_month_day < now_month_day:
				year = str(now_year + 1)
			else:
				year = str(now_year)

		return year

	def get_time(self, text):
		day = self.get_day(text)
		month = self.get_month(text, day)
		year = self.get_year(text, day, month)

		start_time = None
		if day is not None and month is not None and year is not None:
			start_time = year + '-' + month + '-' + day
		else:
			start_time = re.search(u"([\d]*)[-~.,，]*([\d]{1,})[-~.,，]{1,}([\d]{1,})", text)
			if start_time is not None:
				start_time = re.split(u"[-~.,，]*", start_time.group())
				if len(start_time) == 3:
					start_time = start_time[0] + '-' + start_time[1] + '-' + start_time[2]
				elif len(start_time) == 2:
					day = start_time[1]
					month = start_time[0]
					year = self.get_year('', day, month)
					start_time = year + '-' + month + '-' + day
				else:
					start_time = None
			else:
				weekday = re.findall(u"(?:星期|周)(一|二|三|四|五|六|七|日|天|末|[\d])", text)[0]
				if re.sub(u"\\s+", '', weekday) != '':
					if self.week2day.has_key(weekday):
						weekday = int(self.week2day[weekday])
					else:
						weekday = int(weekday)

					now_weekday = datetime.datetime.now().weekday() + 1
					if weekday < now_weekday:
						start_time = str(datetime.datetime.now() + datetime.timedelta(days=weekday + 7 - now_weekday)).split(' ')[0]
					else:
						start_time = str(datetime.datetime.now() + datetime.timedelta(days=weekday - now_weekday)).split(' ')[0]
					print start_time

		if start_time is None or re.sub(u"\\s+", '', start_time) == '':
			return None
		else:
			try:
				return get_localtime(start_time)
			except:
				return None


def get_information(text):
	text = text.decode('utf-8')
	messages = {}

	# title
<<<<<<< HEAD
<<<<<<< HEAD:report_crawler/WHU001/explore.py
<<<<<<< HEAD
	title_pattern = re.compile(u"(?:题(?:.*?){0,1}目|主(?:.*?){0,1}题|Title)[：:. ](.*?)\n")
=======
	title_pattern = re.compile(u"题(?:.*?){0,1}目[：:. ](.*?)\n")
>>>>>>> LJY
=======
	title_pattern = re.compile(u"主[ ]{0,}题[：:. ](.*?)\n", re.S)
>>>>>>> LJY:report_crawler/tests/explore.py
=======
	title_pattern = re.compile(u"(?:(?:(?:报(?:(?![\u4e00-\u9fa5])[\W])*告|讲(?:(?![\u4e00-\u9fa5])[\W])*座|演(?:(?![\u4e00-\u9fa5])[\W])*讲)*(?:主(?:(?![\u4e00-\u9fa5])[\W])*题|题(?:(?![\u4e00-\u9fa5])[\W])*目|标(?:(?![\u4e00-\u9fa5])[\W])*题))|Title|Topic)[）) ]*[：:.]+([\s\S]*)", re.S)
>>>>>>> LJY
	messages['title'] = re.findall(title_pattern, text)
	if len(messages['title']) == 1:
		messages['title'] = messages['title'][0].strip()
	else:
		messages['title'] = ''
	messages['title'] = Filter(messages['title'], 0)

	# time
	time_pattern = re.compile(u"(?:(?:(?:报(?:(?![\u4e00-\u9fa5])[\W])*告|讲(?:(?![\u4e00-\u9fa5])[\W])*座)*(?:时(?:(?![\u4e00-\u9fa5])[\W])*间|日(?:(?![\u4e00-\u9fa5])[\W])*期))|Time)[）) ]*[：:.]+([\s\S]*)", re.S)
	messages['time'] = re.findall(time_pattern, text)
	if len(messages['time']) == 1:
		messages['time'] = messages['time'][0].strip()
	else:
		messages['time'] = ''
	messages['time'] = re.sub(u"[?!@#$&]", ' ', Filter(messages['time'], 0))

	# address
	address_pattern = re.compile(u"(?:(?:(?:报(?:(?![\u4e00-\u9fa5])[\W])*告|讲(?:(?![\u4e00-\u9fa5])[\W])*座){0,1}地(?:(?![\u4e00-\u9fa5])[\W])*点)|Address|Venue|Location|Meeting Room|Place)[）) ]*[：:.]+([\s\S]*)", re.S)
	messages['address'] = re.findall(address_pattern, text)
	if len(messages['address']) == 1:
		messages['address'] = messages['address'][0].strip()
	else:
		messages['address'] = ''
	messages['address'] = re.sub(u"[?!@#$&]", ' ', Filter(messages['address'], 0))

	# speaker
<<<<<<< HEAD
<<<<<<< HEAD:report_crawler/WHU001/explore.py
<<<<<<< HEAD
	speaker_pattern = re.compile(u"(?:主(?:.*?){0,1}讲|报(?:.*?){0,1}告)(?:.*?){0,1}人[：:.](.*?)\n")
=======
	speaker_pattern = re.compile(u"(?:(?:主(?:.*?){0,1}讲|报(?:.*?){0,1}告)(?:.*?){0,1}人|嘉(?:.*?){0,1}宾)[：:.](.*?)\n")
>>>>>>> LJY
=======
	speaker_pattern = re.compile(u"讲[ ]{0,}师[：:.](.*?)\n", re.S)
>>>>>>> LJY:report_crawler/tests/explore.py
=======
	speaker_pattern = re.compile(u"(?:(?:讲(?:(?![\u4e00-\u9fa5])[\W])*授|演(?:(?![\u4e00-\u9fa5])[\W])*讲|报(?:(?![\u4e00-\u9fa5])[\W])*告|主(?:(?![\u4e00-\u9fa5])[\W])*讲)[ ]*(?:人|专(?:(?![\u4e00-\u9fa5])[\W])*家|嘉(?:(?![\u4e00-\u9fa5])[\W])*宾)|讲(?:(?![\u4e00-\u9fa5])[\W])*(?:师|者)|主(?:(?![\u4e00-\u9fa5])[\W])*讲|Speaker)[）) ]*[：:.]+([\s\S]*)", re.S)
>>>>>>> LJY
	messages['speaker'] = re.findall(speaker_pattern, text)
	if len(messages['speaker']) == 1:
		messages['speaker'] = messages['speaker'][0].strip()
	else:
		messages['speaker'] = ''
	messages['speaker'] = re.sub(u"[?!@#$&]", ' ', Filter(messages['speaker'], 0))

	# abstract
<<<<<<< HEAD
<<<<<<< HEAD:report_crawler/WHU001/explore.py
<<<<<<< HEAD
	abstract_pattern = re.compile(u"(?:摘要|内容|内容简介|Bio)[：:.]([\s\S]*)(?:(?:(?:报告|主讲)人(?:简介|介绍))|Abstract)[：:.]", re.S)
=======
	abstract_pattern = re.compile(u"(?:摘要|内容|Abstract)[：:.】]([\s\S]*)(?:(?:(?:报告|主讲)人|嘉宾)(?:简介|介绍)|Bio|Biography)[：:.】]", re.S)
>>>>>>> LJY
=======
	abstract_pattern = re.compile(u"讲座简介[ ]{0,}[：:.]([\s\S]*)", re.S)
>>>>>>> LJY:report_crawler/tests/explore.py
=======
	abstract_pattern = re.compile(u"(?:(?:报告|讲座|内容)*(?:主要)*(?:摘要|内容|提要)|(?:报告|讲座|内容)简介|Abstract)[）) ]*[：:.]+([\s\S]*)", re.S)
>>>>>>> LJY
	messages['abstract'] = re.findall(abstract_pattern, text)
	if len(messages['abstract']) == 1:
		messages['abstract'] = sub_linefeed(messages['abstract'][0].strip())
	else:
<<<<<<< HEAD:report_crawler/WHU001/explore.py
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
=======
		messages['abstract'] = ''
	messages['abstract'] = Filter(messages['abstract'], 1)

	# biography
<<<<<<< HEAD
	biography_pattern = re.compile(u"讲师简介[ ]{0,}[：:.]([\s\S]*)", re.S)
>>>>>>> LJY:report_crawler/tests/explore.py
=======
	biography_pattern = re.compile(u"(?:(?:(?:(?:讲座|主讲|报告|演讲|讲)(?:者|人|师|专家|嘉宾)|个人)|.*?(?:教授|院士|博士))(?:及其)*(?:简介|介绍|简历)|Biography|Bio|Short-Biography|Short bio)[）) ]*[：:.]+([\s\S]*)", re.S)
>>>>>>> LJY
	messages['biography'] = re.findall(biography_pattern, text)
	if len(messages['biography']) == 1:
		messages['biography'] = sub_linefeed(messages['biography'][0].strip())
	else:
<<<<<<< HEAD:report_crawler/WHU001/explore.py
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
=======
		messages['biography'] = ''
<<<<<<< HEAD
	if re.search(u"讲座简介[ ]{0,}[：:.]|除[0-9]*级全体本科生|欢迎参加", messages['biography']) is not None:
		messages['biography'] = re.sub(u"(讲座简介[ ]{0,}[：:.]|除[0-9]*级全体本科生|欢迎参加)([\s\S]*)", '', messages['biography'])
>>>>>>> LJY:report_crawler/tests/explore.py
=======
	messages['biography'] = Filter(messages['biography'], 1)

	# If speaker is not exist, we could get it from the biography.
	if messages['speaker'] == '':
		speakerFromBioChina = re.match(u"(.*?)(教授|副教授|博士|讲师)", messages['biography'])
		messages['speaker'] = '' if speakerFromBioChina is None else speakerFromBioChina.group()
	if messages['speaker'] == '':
		speakerFromBioEng = re.match(u"([A-Z][a-zA-Z]*[ .]*)+", messages['biography'])
		messages['speaker'] = '' if speakerFromBioEng is None else speakerFromBioEng.group()
	if messages['speaker'] == '':
		speakerFromBioAll = re.search(u"(.*?)(教授|院士|博士)(及其)*(简介|介绍|简历)[：:.]+", text)
		messages['speaker'] = '' if speakerFromBioAll is None else re.sub(u"(及其)*(简介|介绍|简历)[：:.]+", '', speakerFromBioAll.group().strip())
>>>>>>> LJY

	print messages['speaker']
	# a = testing()
	# x = a.get_time(messages['time'])
	# print x
	return messages


<<<<<<< HEAD
<<<<<<< HEAD:report_crawler/WHU001/explore.py
f = open('18.txt', 'r').read()
>>>>>>> LJY
=======
f = open('12.txt', 'r').read()
>>>>>>> LJY:report_crawler/tests/explore.py
dict = get_information(f)
=======
f = open('2.txt', 'r').read()
# dict = get_information(f)
print re.findall(u"报(?:(?![\u4e00-\u9fa5])[\W])*告(?:(?![\u4e00-\u9fa5])[\W])*人[：:.]", unicode(f, 'utf-8'))[0]
>>>>>>> LJY
print f

