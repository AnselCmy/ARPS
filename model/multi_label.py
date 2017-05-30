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
from sklearn.externals import joblib

instance = [
	'乳腺癌患者围术期多媒体信息化辅助下的护理干预',
	'智慧图书馆顶层设计研究',
	'全业财务"云管理"棵析',
	'云计算机环境下的网络新技术探索',
	'基于云计算的电网智能调度平台的构建'
]

label = [
	[1, 0, 0, 0],
	[0, 1, 1, 0],
	[0, 1, 0, 0],
	[0, 1, 0, 1],
	[0, 1, 0, 0]
]



class Multi_Label_Model(object):
	def __init__(self, mode='train', multi_model=None, params=None, path=None):
		if mode == 'train':
			self.model = GridSearchCV(multi_model, params, verbose=1)
		else:
			self.model = self.load_model(path)

	def fit(self, x_train, y_train):
		y_train = np.array(y_train)
		self.model.fit(x_train, y_train)
		print self.model.best_params_

	def predict(self, x_test):
		ans = self.model.predict(x_test).toarray()
		return ans

	def predict_prob(self, x_test):
		ans = self.model.predict_proba(x_test).toarray()
		return ans

	def save_model(self, path):
		joblib.dump(self.model, path)

	def load_model(self, path):
		return joblib.load(path)

def get_vector(sentence, word_model):
	word_number = 0
	vector = np.zeros([200])
	for word in sentence:
		if word in word_model:
			# print '!!!!'
			vector += word_model[word]
			word_number += 1
	vector /= word_number * 1.0
	return vector

def sent_to_vec(X, word_model):
	sentences = map(lambda x: ' '.join(jieba.cut(x)).split(' '), [k for k in X])
	vectors = map(lambda x: get_vector(x, word_model), [sent for sent in sentences])
	return vectors

# if __name__ == '__main__':
# 	multi_model = ClassifierChain()
# 	params = {
# 		'classifier': [DecisionTreeClassifier(), GaussianNB()],
# 	}
# 	sentences = map(lambda x: ' '.join(jieba.cut(x)).split(' '), [k for k in instance])
# 	word_model = gensim.models.Word2Vec(sentences, size=200, min_count=1)
# 	# input = sent_to_vec(instance, word_model)
#
# 	model = Multi_Label_Model(mode='test', path='m.model')
# 	# model.fit(input, label)
#
# 	test = sent_to_vec(['全业财务"云计算"棵析'], word_model)
# 	a = model.predict_prob(test)
# 	print a
# 	# model.save_model('m.model')
