from datetime import datetime
import smtplib
import random
from time import sleep
from selenium import webdriver
import pandas

def currentTime():
    current=datetime.now()
    current=current.strftime('%H:%M %d/%m/%Y')
    return current

def messageNotification():
    content_message='Se Publicaron nuevos Items, {}'.format(currentTime())
    subject='**ARTICULO NUEVO**'
    whole_message='Subject: {}\n\n{}'.format(subject,content_message)
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('remitter@gmail.com','password')
    server.sendmail('remitter@gmail.com','receiver@gmail.com',whole_message)
    server.quit()
    return

def saveData(dict_items):
    dt_items=pandas.DataFrame(dict_items,columns=['Title','Price'])
    dt_items.to_csv('Database_items.txt',header=True)
    
    return

def starChromeDriver(driver_pathfile):
    driver=webdriver.Chrome(driver_pathfile)
    print('\nopening Browser, 4s...')
    sleep(4.0)
    return driver

def Spider(driver): 
    url='https://www.olx.com.co/carros_c378'

    print('\nloading Page, 20s...')
    driver.get(url)
    sleep(20.0)
    print('got request by Spider')
    
    #for page with item dynamic loading of by any click button
    for i in range(3):
        try:
            button=driver.find_element_by_xpath('//li[@data-aut-id="btnLoadMore"]')
            button.click() 
            sleep(random.uniform(7.0,21.0)) 
        except:
            print('Alert: No Button Loader')
            break

    items=driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

    dict_items={
        'Title':[],
        'Price':[]
    }

    for item in items:
        price=item.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]')
        price=price.text
        title=item.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]')
        title=title.text
        #description=item.find_element_by_xpath('.//div[@data-aut-id="itemDescriptionContent"]')
        dict_items['Title'].append(title)
        dict_items['Price'].append(price)
    
    return dict_items

