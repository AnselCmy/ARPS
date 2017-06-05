# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("..")

import os
import time
import requests
import pymongo as pm
from settings import SAVEDIR
from spiders.Global_function import get_localtime

now_time = str(get_localtime(time.strftime("%Y-%m-%d", time.localtime())))
# now_time = '20170425'

class ReportSpiderPipeline(object):
    def process_item(self, item, spider):
        if item['title'] == '':
            return
        # find or make the dir for school and faculty
        dirname = SAVEDIR + '/' + now_time + '/' + item['school'] + '/' + item['faculty'] + '/' + str(item['number'])
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        filename = dirname + '/' + str(item['number'])
        # if the img exist, we should save the img
        if item.has_key('img_url'):
            self.img_save(item['img_url'], filename)
        # text save
        self.text_save(item, filename)
        # save to database
        self.DB_save(item)
        return item

    def text_save(self, all_messages, filename):
        filename += '.txt'
        # We only save six things: title, speaker, time, address, person_introduce, content
        with open(filename, 'w') as f:
            # school
            f.write('School:' + '\n' + all_messages['school_name'] + '\n' * 2)
            # organizer
            f.write('Organizer:' + '\n' + all_messages['organizer'] + '\n' * 2)
            # title must have
            f.write('Title:' + '\n' + all_messages['title'] + '\n' * 2)
            # others may not have
            if all_messages.has_key('speaker'):
                f.write('Speaker: ' + '\n' + all_messages['speaker'] + '\n' * 2)
            if all_messages.has_key('time'):
                f.write('Time: ' + '\n' + all_messages['time'] + '\n' * 2)
            if all_messages.has_key('address'):
                f.write('Address: ' + '\n' + all_messages['address'] + '\n' * 2)
            if all_messages.has_key('person_introduce'):
                f.write('Person_introduce: ' + '\n' + all_messages['person_introduce'] + '\n' * 2)
            if all_messages.has_key('content'):
                f.write('Content: ' + '\n' + all_messages['content'] + '\n' * 2)

    def img_save(self, img_url, filename):
        # get img
        img = requests.get(img_url)
        # save
        filename += '.jpg'
        with open(filename, 'w') as f:
            f.write(img.content)
            f.close()

    def DB_save(self, all_messages):
        conn = pm.MongoClient('localhost', 27017)
        db = conn.get_database('report_db')
        # col = db.get_collection('col' + now_time)
        col = db.get_collection('reports_without_label')
        col.insert(all_messages)
