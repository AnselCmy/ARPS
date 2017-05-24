from flask import Flask
from flask import render_template
from pymongo import MongoClient

app = Flask(__name__)
conn = MongoClient('localhost', 27017)
db = conn.get_database('report_db')

@app.route('/<string:school>')
def report_by_school(school = None):
	school = school.upper()
	reports = db.col20170524.find({'school':school})
	return render_template('report_by_school.html', reports = reports)

@app.route('/')
def school_select():
	return render_template('school_select.html')


if __name__ == '__main__':
	app.run(debug = True)