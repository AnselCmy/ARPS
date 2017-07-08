# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
sys.path.append('..')
from model.main import Multi_Label_Model

model = Multi_Label_Model()
labels = [u'计算机网络', u'信息安全', u'云计算&大数据', u'机器学习&模式识别', u'数据科学',
          u'计算机图形学&图像处理', u'计算机教学', u'数据库', u'计算机组成与结构', u'人机交互',
          u'软件技术', u'计算机应用', u'信息检索', u'物联网', u'多媒体技术']
labels = list(range(len(labels)))

model.load_word2vec_model('model/word2vec_model.txt')
model.load_scaler('model/scaler.txt')
model.load_model('model')
# a = model.predict_class_with_string([u'一种微阵列数据降维新方法', u'基于网络自有信号的网络线缆故障的检测方法研究'], labels)
print(model.predict_class_with_string([u'道与魔的较量-网络安全技术的新趋势'], labels))
print(model.predict_class_with_string([u'基于网络自有信号的网络线缆故障的检测方法研究'], labels))
# for each in a:
#     print(each)


