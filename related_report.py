from __future__ import print_function
import sys
import re
import time
from gensim import corpora, models, similarities
import logging
import jieba
import os
import pymongo as pm
reload(sys)
sys.setdefaultencoding('utf8')
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
threshold = 0.5

def connect_db():
	conn = pm.MongoClient('192.168.1.2', 27017)
	db = conn.get_database('report_db')
	reports_col = db.get_collection('reports_with_label')
	return reports_col


def get_stop_words(path):
	file = open(path)
	stop_words = file.readlines()
	stop_words = [s.strip() for s in stop_words]
	file.close()
	return stop_words


class ReportIter(object):
	def __init__(self, col):
		self.col = col
	
	def __iter__(self):
		for report in self.col.find():
			yield report['content'].split()
		
# Connect to db
reports_col = connect_db()
# Get the iterator of reports
reports = ReportIter(reports_col)
# Build the LSI model
dictionary = corpora.Dictionary(reports)
corpus = [dictionary.doc2bow(s) for s in reports]
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=15)
index = similarities.MatrixSimilarity(lsi[corpus])
# Get the id and index
id_index = []
for report in reports_col.find():
	id_index.append(report['_id'].__str__())

cnt = 0
for report in reports_col.find():
	content = report['content'].split()
	content_bow = dictionary.doc2bow(content)
	content_lsi = lsi[content_bow]
	sims = index[content_lsi]
	sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
	related = []
	related_id = []
	for i in sort_sims:
		if threshold < i[1] < 1 and id_index[i[0]] != report['_id'].__str__():
			related.append(i[0])
		if i[1] < threshold:
			break
	# print(cnt)
	# cnt += 1
	# print(related)
	for i in related:
		related_id.append(id_index[i])
	reports_col.update({'_id': report['_id']}, {'$set': {'related': related_id}})
	# print(related_id)
