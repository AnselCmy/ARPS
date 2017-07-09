import os
import time
import shutil
import traceback
from report_crawel.spiders.Global_function import get_localtime
from report_crawel.settings import SAVEDIR

now_time = get_localtime(time.strftime("%Y-%m-%d", time.localtime()))


# now_time = '20170425'

class Spider_starter(object):
    def crawl(self):
        # running the spider
        # self.HFUT()
        self.USTC()
        self.SYSU()
        self.WHU()
        self.THU()
        self.NPU()
    
    def run_spider(self, spider_name):
        dirname = SAVEDIR + '/' + str(now_time) + '/' + spider_name[0:len(spider_name) - 3] + '/' + spider_name
        # If the dir is exist, clear the dir(today)
        if os.path.exists(dirname):
            shutil.rmtree(dirname, True)
        # If one of the spiders has error, the print_exc() function will tell us which is criminal
        try:
            os.system('scrapy crawl ' + spider_name)
        except:
            traceback.print_exc()
    
    def HFUT(self):
        # self.run_spider('HFUT000')
        pass
    
    def NPU(self):
        self.run_spider('NPU001')
    
    def USTC(self):
        self.run_spider('USTC001')
        # self.run_spider('USTC002')
        # self.run_spider('USTC003')
        # self.run_spider('USTC004')
        # self.run_spider('USTC005')
        # self.run_spider('USTC006')
    
    def SYSU(self):
        self.run_spider('SYSU001')
    
    def THU(self):
        self.run_spider('THU001')
        # self.run_spider('THU002')
        # self.run_spider('THU003')
        # self.run_spider('THU007')
    
    def WHU(self):
        self.run_spider('WHU001')
        
    def ECNU(self):
        self.run_spider('ECNU001')
        
    def HUST(self):
        self.run_spider('HUST001')
        
    def JLU(self):
        self.run_spider('JLU001')
        
    def NWPU(self):
        self.run_spider('NWPU001')

    def SCU(self):
        self.run_spider('SCU001')

    def SDU(self):
        self.run_spider('SDU001')


if __name__ == '__main__':
    starter = Spider_starter()
    starter.crawl()
