#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import print_function
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pymongo as pm
sys.path.append('..')
from model.main import Multi_Label_Model


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
	# Initial for model
	model = Multi_Label_Model()
	labels = [u'计算机网络', u'信息安全', u'云计算&大数据', u'机器学习&模式识别', u'数据科学',
			  u'计算机图形学&图像处理', u'计算机教学', u'数据库', u'计算机组成与结构', u'人机交互',
			  u'软件技术', u'计算机应用', u'信息检索', u'物联网', u'多媒体技术']
	labels = list(range(len(labels)))
	model.load_word2vec_model('model/word2vec_model.txt')
	model.load_scaler('model/scaler.txt')
	model.load_model('model')
	# Initial for mongodb
	conn = pm.MongoClient('localhost', 27017)
	db = conn.get_database('report_db')
	col = db.get_collection('reports_without_label')
	new_col = db.get_collection('reports_with_label')
	# For clean the content
	punc1 = re.compile(r"[。，、；：（）\——《》【】\n,.;:()\-<>\[\]]")
	punc2 = re.compile(r"[\“\”\‘\’\"\']")
	stop_words = get_stop_words('stop_words.txt')
	# Deal with reports which are not labeled
	for c in col.find({'is_labeled': 0}):
		# Classify
		if check_contain_chinese(c['title']) and check_is_cs(c['faculty']):
			# Get label list by model
			new_label = model.predict_class_with_string([c['title']], labels)[0]
			# Set label to this report
			col.update({'_id': c['_id']}, {'$set': {'label': new_label, 'click': 0, 'is_labeled': 1}})
			# Get the content by id
			new_doc = col.find({'_id': c['_id']})[0]
			# Delete the old id
			del new_doc['_id']
			# Insert labeled report to new col
			new_col.insert(new_doc)
		# Clean to get the content
		if c.has_key('abstract'):
			content = c['title'] + c['abstract']
		else:
			content = c['title']
		content = re.sub(punc1, ' ', content)
		content = re.sub(punc2, '', content)
		content = jieba.cut(content)
		content = [s for s in content if s not in stop_words]
		content = ' '.join(content)
		new_col.update({'title': c['title']}, {'$set': {'content': content}})


if __name__ == '__main__':
	classify()




