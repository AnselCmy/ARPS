
import os
import time

# Write the log head
f = open('log.txt', 'a+')
log_time = time.strftime('DATE: %Y-%m-%d', time.localtime(time.time()))
log_time += '\n' + time.strftime('TIME: %H:%M:%S', time.localtime(time.time())) + '\n'
f.writelines('-'*100 + '\n')
f.writelines(log_time)
f.close()

# Run spider
os.chdir('./report_crawler')
# os.system('python crawler.py')
os.system('scrapy crawl WHU001')
os.chdir('../')

# Run Classifier
os.chdir('./ML_model/test')
os.system('python ./report_classifier.py')
os.chdir('../../')

# Write the log tail
f = open('log.txt', 'a+')
f.writelines('-'*100 + '\n')
f.close()



