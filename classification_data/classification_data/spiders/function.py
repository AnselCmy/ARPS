# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_title():
	title = []
	with open('/mnt/hgfs/chen/code/ARPS/classification_data/title.txt', 'r') as f:
		lines = f.readlines()
		print len(lines)
		for line in lines:
			title.append(line.strip())
	return title

get_title()
