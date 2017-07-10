# -*- coding: utf-8 -*-
from parser_001 import BNU001, BUAA001, ECNU001, NWPU001, SCU001, SDU001, SYSU001, THU001, UESTC001, WHU001, NWSUAF001


def get_information(text, faculty):
	messages = {}

	if faculty[:-3] == 'BNU':
		messages = BNU(text, faculty[-3:])
	elif faculty[:-3] == 'BUAA':
		messages = BUAA(text, faculty[-3:])
	elif faculty[:-3] == 'ECNU':
		messages = ECNU(text, faculty[-3:])
	elif faculty[:-3] == 'NWPU':
		messages = NWPU(text, faculty[-3:])
	elif faculty[:-3] == 'SCU':
		messages = SCU(text, faculty[-3:])
	elif faculty[:-3] == 'SDU':
		messages = SDU(text, faculty[-3:])
	elif faculty[:-3] == 'SYSU':
		messages = SYSU(text, faculty[-3:])
	elif faculty[:-3] == 'THU':
		messages = THU(text, faculty[-3:])
	elif faculty[:-3] == 'UESTC':
		messages = UESTC(text, faculty[-3:])
	elif faculty[:-3] == 'WHU':
		messages = WHU(text, faculty[-3:])
	elif faculty[:-3] == 'NWSUAF':
		messages = NWSUAF(text, faculty[-3:])

	return messages


def BNU(text, faculty_num):
	messages = {}
	if faculty_num == '001':
		messages = BNU001.Parser(text, sub_linefeed)
	return messages


def BUAA(text, faculty_num):
	messages = {}
	if faculty_num == '001':
		messages = BUAA001.Parser(text, sub_linefeed)
	return messages


def ECNU(text, faculty_num):
	messages = {}
	if faculty_num == '001':
		messages = ECNU001.Parser(text, sub_linefeed)
	return messages


def NWPU(text, faculty_num):
	messages = {}
	if faculty_num == '001':
		messages = NWPU001.Parser(text, sub_linefeed)
	return messages


def SCU(text, faculty_num):
	messages = {}
	if faculty_num == '001':
		messages = SCU001.Parser(text, sub_linefeed)
	return messages


def SDU(text, faculty_num):
	messages = {}
	if faculty_num == '001':
		messages = SDU001.Parser(text, sub_linefeed)
	return messages


def SYSU(text, faculty_num):
	messages = {}
	if faculty_num == '001':
		messages = SYSU001.Parser(text, sub_linefeed)
	return messages


def THU(text, faculty_num):
	messages = {}
	if faculty_num == '001':
		messages = THU001.Parser(text, sub_linefeed)
	return messages


def UESTC(text, faculty_num):
	messages = {}
	if faculty_num == '001':
		messages = UESTC001.Parser(text, sub_linefeed)
	return messages


def WHU(text, faculty_num):
	messages = {}
	if faculty_num == '001':
		messages = WHU001.Parser(text, sub_linefeed)
	return messages


def NWSUAF(text, faculty_num):
	messages = {}
	if faculty_num == '001':
		messages = NWSUAF001.Parser(text, sub_linefeed)
	return messages


def sub_linefeed(text):
	sub_text = ''
	for line in text.splitlines():
		line = line.rstrip()
		if line != '':
			line += '\n'
		sub_text += line
	return sub_text
