#!/usr/bin/env python
import sys
sys.path.append('..')

import train as model
import report_reader as reader

db = reader.connectDB('report_db')
col = reader.getCollection(db, 'test')
new_col = reader.getCollection(db, 'test_classified')


for c in col.find():
	label = model.test([c['title']])[0]
	col.update({'_id': c['_id']}, {'$set': {'label':label}})
	new_doc = col.find({'_id': c['_id']})[0]
	del new_doc['_id']
	new_col.insert(new_doc)
	col.remove({'_id': c['_id']})



