# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

title_name = '计算机应用_title.txt'
filename = '计算机应用.txt'
class ClassificationDataPipeline(object):
    def process_item(self, item, spider):
        if not item.has_key('title'):
            return
        with open(title_name, 'a') as t:
            t.write(item['title'] + '\n')
        with open(filename, 'a') as f:
            f.write('***\n')
            f.write('<' + item['title'] + '>' + '\n')
            f.write(item['abstract'] + '\n')
