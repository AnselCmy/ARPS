#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import print_function
import sys
import re
import time
reload(sys)
sys.setdefaultencoding('utf8')
import pymongo as pm

cs_labels = ['计算机网络', '信息安全', '云计算&大数据', '机器学习&模式识别', '数据科学',
				'计算机图形学&图像处理', '计算机教学', '数据库', '计算机组成与结构', '人机交互',
				'软件技术', '计算机应用', '信息检索', '物联网', '多媒体技术']

regions = { u'华东': ['上海市', '江苏省', '浙江省', '安徽省', '江西省', '山东省', '福建省'],
			u'华北': ['北京市', '天津市', '山西省', '河北省'],
			u'华中': ['河南省', '湖北省', '湖南省'],
			u'华南': ['广东省', '广西壮族自治区', '海南省', '香港特别行政区', '澳门特别行政区'],
			u'西南': ['四川省', '贵州省', '云南省', '重庆市', '西藏自治区'],
			u'西北': ['陕西省', '甘肃省', '青海省', '宁夏回族自治区', '新疆维吾尔自治区'],
			u'东北': ['黑龙江省', '吉林省', '辽宁省'] }
	
region_weight = [0.5, 0.3, 0.2]
region_area_weight = [0.5, 0.5]


def get_localtime(times):
	date = times.split('-')
	if len(date) == 3:
		year, month, day = date[0].strip(), date[1].strip(), date[2].strip()
		if len(year) != 4:
			year = time.strftime("%Y", time.localtime())[:2] + year
	else:
		month, day = date[0].strip(), date[1].strip()
		year = time.strftime("%Y", time.localtime())

	time_number = int(year) * 10000 + int(month) * 100 + int(day)
	return time_number


def connect_db()
	conn = pm.MongoClient('192.168.1.2', 27017)
	db = conn.get_database('report_db')
	reports_col = db.get_collection('reports_without_label')
	users_col = db.get_collection('users')
	retunr reports_col, users_col


def get_loc_list(loc):
	pattern = re.compile(u'([\u4e00-\u9fa5]+):([\u4e00-\u9fa5]+)-([\u4e00-\u9fa5]+)')
	if '-' not in loc:
		loc = loc+'-市辖区'
	return pattern.search(loc).groups()


def get_region(province):
	for reg, prov in regions.items():
		if province in prov:
			return reg
	else:
		raise ValueError('invalid province: %s' % province)


if __name__ == '__main__':
	now_time = get_localtime(time.strftime("%Y-%m-%d", time.localtime()))
	for user in users_col.find():
		p = user['province']
		c = user['city']
		# Get the location info of user
		user_loc_list = [get_region(p), p, c]
		for report in reports_col.find():
			# The score of location
			report_loc_list = get_loc_list(report['location'])
			diff = list(map(lambda x: x[0]==x[1], zip(user_loc_list, report_loc_list)))
			if not diff[1]:
				diff[2] = False
			region_score = reduce(lambda x,y: x+y, map(lambda x:x[0]*int(x[1]), zip(region_weight, diff)))
			# The score of academic area
			area_score = 0
			for a in user['area']:
				if cs_labels.index(a) in report['label']:
					area_score = 1
			# Get the total score
			score = reduce(lambda x,y: x+y,
			               map(lambda x:x[0]*x[1], zip(region_area_weight, zip(region_score, area_score))))
			# Update the score in users_col
			if not user.has_key('reports_score'):
				reports_score = {}
			else:
				reports_score = user['reports_score']
			new_reports_score = {user['_id'], score}
			update_reports_score = dict(reports_score, **new_reports_score)
			users_col.update({'_id': user['_id']},
			                 {'$set': {'reports_score': update_reports_score}})
	