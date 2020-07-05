#encoding:utf-8

import selenium
import requests
import time
from selenium import webdriver
import random


url = 'http://iot.kf315.net/'

driver = webdriver.Chrome("E:/2345Downloads/chromedriver_win32/chromedriver.exe")  # 创建Chrome浏览器驱动实例
driver.implicitly_wait(15)  # 设置隐式等待时间
driver.maximize_window()  # 全屏窗口
driver.get(url)
#登陆
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/input').send_keys('admin')
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/input').send_keys('jgw123')
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/input').click()
#点击设备
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[1]/div/div[1]/div[4]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[1]/div/div[1]/div[4]/div[2]/a[6]').click()

try:
    for t in range(9,10):
        for i in range(1,11):
            xpath = '//*[@id="root"]/div/div/div[3]/div[2]/div/div/div[2]/div/div/div/div/div[3]/div[2]/table/tbody/tr[' + str(i) +']/td[11]/div/a[2]'
            driver.find_element_by_xpath(xpath).click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[5]/div/div/input').clear()
            # driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[5]/div/div/input')
            driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[5]/div/div/input').send_keys(str(random.uniform(118.0000000001,118.9999999999)))
            driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[6]/div/div/input').clear()
            driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[6]/div/div/input').send_keys(str(random.uniform(28.9800000000,29.9999999999)))
            driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
        xpath_ye = '//*[@id="root"]/div/div/div[3]/div[2]/div/div/div[3]/div[2]/ul/li[' + str(t) + ']/a'
        driver.find_element_by_xpath(xpath_ye).click()
        time.sleep(2)
except:
    pass

driver.quit()

