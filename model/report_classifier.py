#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
from tqdm import tqdm
reload(sys)
sys.path.append('..')
sys.setdefaultencoding('utf8')

import train as model
import report_reader as reader

def check_contain_chinese(check_str):
    for ch in check_str.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

def check_is_cs(check_str):
	if check_str[-3:] == '001':
		return True
	else:
		return False

def classify():
	db = reader.connectDB('report_db')
	col = reader.getCollection(db, 'reports_without_label')
	new_col = reader.getCollection(db, 'reports_with_label')


	for c in tqdm(col.find()):
		if check_contain_chinese(c['title']) and check_is_cs(c['faculty']):
			label = model.test([c['title']])[0]
			col.update({'_id': c['_id']}, {'$set': {'label':label}})
			new_doc = col.find({'_id': c['_id']})[0]
			del new_doc['_id']
			new_col.insert(new_doc)
			col.remove({'_id': c['_id']})


if __name__ == '__main__':
	classify()




