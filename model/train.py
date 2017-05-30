# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import jieba
import gensim
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from skmultilearn.problem_transform import ClassifierChain
from sklearn.naive_bayes import GaussianNB
from multi_label import Multi_Label_Model, sent_to_vec

label_number = {
	'云计算&大数据': 0,
	'人机交互': 1,
	'信息安全': 2,
	'信息检索': 3,
	'多媒体': 4,
	'数据库': 5,
	'数据科学': 6,
	'机器学习&模式识别': 7,
	'物联网': 8,
	'计算机图形学&图像处理': 9,
	'计算机应用': 10,
	'计算机教学': 11,
	'计算机组成与结构': 12,
	'计算机网络': 13,
	'软件技术': 14,
}

def get_data(filename):
	title = []
	label = []
	with open(filename, 'r') as f:
		lines = f.readlines()
		for i in xrange(len(lines)):
			if i % 3 == 0:
				title.append(lines[i])
			if i % 3 == 1:
				label.append(map(lambda x: label_number[x], [l for l in lines[i].strip().split(' ')]))
		f.close()
	return title, label


def one_hot(target):
	label = np.zeros([len(target), 15])
	for i in xrange(len(target)):
		for each in target[i]:
			label[i][each] = 1
	return label

def train():
	X, y = get_data('train.txt')
	# X = map(lambda x: ' '.join(jieba.cut(x)).split(' '), [s for s in X])
	w2v = gensim.models.Word2Vec.load('w2v.model')
	label = one_hot(y)

	multi_model = ClassifierChain()
	params = {
		'classifier': [GaussianNB()],
	}
	input = sent_to_vec(X, w2v)

	print 'Build model:'
	model = Multi_Label_Model(multi_model=multi_model, params=params)

	print 'Start training:'
	model.fit(input, label)
	model.save_model('classify.model')


def test(test_data):
	model = Multi_Label_Model(mode='test', path='classify.model')
	w2v = gensim.models.Word2Vec.load('w2v.model')
	input = sent_to_vec(test_data, w2v)

	l = model.predict(input)
	ans = []
	for label in l:
		mid = []
		for i in xrange(len(label)):
			if label[i]:
				mid.append(i)
		ans.append(mid)
	return ans

if __name__ == '__main__':
	# train()
	pred = test(['翻转课堂理念下高校计算机应用基础课程教学设计',
	             '信息能力视角下的高校检索课课改——基于选课学生的问卷分析'])
	print pred
