# -*- coding:utf-8 -*-
import re


def Filter(text, ab_sign=0):
	# title
	if re.search(u"(((报[ ]{0,}告|讲[ ]{0,}座){0,}(主[ ]{0,}题|题[ ]{0,}目))|Title)[：:.]", text) is not None:
		text = re.sub(u"(((报[ ]{0,}告|讲[ ]{0,}座){0,}(主[ ]{0,}题|题[ ]{0,}目))|Title)[：:.][\s\S]*", '', text)

	# time
	if re.search(u"(((报[ ]{0,}告|讲[ ]{0,}座){0,}时[ ]{0,}间)|Time)[：:. ]", text) is not None:
		text = re.sub(u"(((报[ ]{0,}告|讲[ ]{0,}座){0,}时[ ]{0,}间)|Time)[：:. ][\s\S]*", '', text)

	# address
	if re.search(u"(((报[ ]{0,}告|讲[ ]{0,}座){0,1}地[ ]{0,}点)|Address)[：:.]", text) is not None:
		text = re.sub(u"(((报[ ]{0,}告|讲[ ]{0,}座){0,1}地[ ]{0,}点)|Address)[：:.][\s\S]*", '', text)

	# speaker
	if re.search(u"((讲[ ]{0,}授|演[ ]{0,}讲|报[ ]{0,}告|主[ ]{0,}讲)[ ]{0,}人|讲[ ]{0,}(师|者)|Speaker)[：:.]", text) is not None:
		text = re.sub(u"((讲[ ]{0,}授|演[ ]{0,}讲|报[ ]{0,}告|主[ ]{0,}讲)[ ]{0,}人|讲[ ]{0,}(师|者)|Speaker)[：:.][\s\S]*", '', text)

	# abstract
	if re.search(u"(((报告|讲座|内容){0,}(摘要|内容))|(报告|讲座)简介|Abstract)[ ]{0,}[：:.]", text) is not None:
		text = re.sub(u"(((报告|讲座|内容){0,}(摘要|内容))|(报告|讲座)简介|Abstract)[ ]{0,}[：:.][\s\S]*", '', text)

	# biography
	if re.search(u"((主讲人|报告人|个人|讲者)(?:简介|介绍)|Biography)[ ]{0,}[：:.]", text) is not None:
		text = re.sub(u"((主讲人|报告人|个人|讲者)(?:简介|介绍)|Biography)[ ]{0,}[：:.][\s\S]*", '', text)

	# others
	if re.search(u"欢迎各位", text) is not None:
		text = re.sub(u"欢迎各位[\s\S]*", '', text)
	if re.search(u"报[ ]{0,}告[ ]{0,}[一二三四五][ ]{0,}[：:.]", text) is not None:
		text = re.sub(u"报[ ]{0,}告[ ]{0,}[一二三四五][ ]{0,}[：:.][\s\S]*", '', text)

	return text


def Parser(text, sub_linefeed):
	text = text.decode('utf-8')
	messages = {}

	# title
	title_pattern = re.compile(u"(?:(?:(?:报[ ]{0,}告|讲[ ]{0,}座){0,}(?:主[ ]{0,}题|题[ ]{0,}目))|Title)[：:.]([\s\S]*)", re.S)
	messages['title'] = re.findall(title_pattern, text)
	if len(messages['title']) == 1:
		messages['title'] = messages['title'][0].strip()
	else:
		messages['title'] = ''
	messages['title'] = Filter(messages['title'], 0)

	# time
	time_pattern = re.compile(u"(?:(?:(?:报[ ]{0,}告|讲[ ]{0,}座){0,}时[ ]{0,}间)|Time)[：:. ]([\s\S]*)", re.S)
	messages['time'] = re.findall(time_pattern, text)
	if len(messages['time']) == 1:
		messages['time'] = messages['time'][0].strip()
	else:
		messages['time'] = ''
	messages['time'] = Filter(messages['time'], 0)

	# address
	address_pattern = re.compile(u"(?:(?:(?:报[ ]{0,}告|讲[ ]{0,}座){0,1}地[ ]{0,}点)|Address)[：:.]([\s\S]*)", re.S)
	messages['address'] = re.findall(address_pattern, text)
	if len(messages['address']) == 1:
		messages['address'] = messages['address'][0].strip()
	else:
		messages['address'] = ''
	messages['address'] = Filter(messages['address'], 0)

	# speaker
	speaker_pattern = re.compile(u"(?:(?:讲[ ]{0,}授|演[ ]{0,}讲|报[ ]{0,}告|主[ ]{0,}讲)[ ]{0,}人|讲[ ]{0,}(?:师|者)|Speaker)[：:.]([\s\S]*)", re.S)
	messages['speaker'] = re.findall(speaker_pattern, text)
	if len(messages['speaker']) == 1:
		messages['speaker'] = messages['speaker'][0].strip()
	else:
		messages['speaker'] = ''
	messages['speaker'] = Filter(messages['speaker'], 0)

	# abstract
	abstract_pattern = re.compile(u"(?:(?:(?:报告|讲座|内容){0,}(?:摘要|内容))|(?:报告|讲座)简介|Abstract)[ ]{0,}[：:.]([\s\S]*)", re.S)
	messages['abstract'] = re.findall(abstract_pattern, text)
	if len(messages['abstract']) == 1:
		messages['abstract'] = sub_linefeed(messages['abstract'][0].strip())
	else:
		messages['abstract'] = ''
	messages['abstract'] = Filter(messages['abstract'], 1)

	# biography
	biography_pattern = re.compile(u"(?:(?:主讲人|报告人|个人|讲者)(?:简介|介绍)|Biography)[ ]{0,}[：:.]([\s\S]*)", re.S)
	messages['biography'] = re.findall(biography_pattern, text)
	if len(messages['biography']) == 1:
		messages['biography'] = sub_linefeed(messages['biography'][0].strip())
	else:
		messages['biography'] = ''
	messages['biography'] = Filter(messages['biography'], 1)

	return messages
