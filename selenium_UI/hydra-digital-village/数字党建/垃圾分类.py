#encoding:utf-8

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys
sys.path.append(r"D:\python\selenium_UI\hydra-digital-village\数字党建")
from SZXC_login import login_web,capture

driver = login_web()
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[1]/div/div[1]/div[6]').click()
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/div[1]/div/div[1]/div[6]/div[2]/a').click()
time.sleep(1)
#tianjia
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div[2]/div/div/div/div/div[1]/div/div[1]/div/button').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div[1]/div').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@class="ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft"]/div/ul/li[1]').click()
driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[3]/div/div/input').send_keys('标题')
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="ueditor_0"]'))
driver.find_element_by_xpath('/html/body').send_keys('11111111111111111111111111111111122222222222222222222222222222222')
driver.switch_to.default_content()
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div[5]/div/div/div/div[1]/input').send_keys('D:/cat.jpg')
driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div[2]/form/div[9]/div/div/label[4]/span[1]/span').click()
driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div[3]/div/button[2]').click()
#编辑
