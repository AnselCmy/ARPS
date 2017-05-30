# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import jieba
import gensim

def get_data(filename):
	title = []
	with open(filename, 'r') as f:
		lines = f.readlines()
		for i in xrange(len(lines)):
			if i % 3 == 0:
				title.append(lines[i])
		f.close()
	return title

sentences = get_data('train.txt')
sentences = map(lambda x: ' '.join(jieba.cut(x)).split(' '), [s for s in sentences])
print 'Start:'
model = gensim.models.Word2Vec(sentences, size=200, min_count=1)
print 'Completed'
model.save('w2v.model')
