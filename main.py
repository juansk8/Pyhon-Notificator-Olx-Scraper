from time import sleep
import random
from Scraper_Olx import *

def main(driver,dict_spider2,dict_spider):
    if (dict_spider!=dict_spider2):
        saveData(dict_spider2)
        if (len(dict_spider2)>=len(dict_spider)):
            messageNotification()
            
    return

driver=starChromeDriver('./chromedriver.exe')
dict_spider=Spider(driver)
saveData(dict_spider)

x=0
while True:
    x=x+1
    print('cycle #:',x)
    sleep(random.uniform(20.0*60.0,40.0*60.0))
    dict_spider2=Spider(driver)
    main(driver,dict_spider2,dict_spider)
    dict_spider=dict_spider2
