
#coding:utf-8

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import sys
sys.path.append(r"D:\python\selenium_UI\hydra-digital-village\数字党建")
from SZXC_login import login_web,capture

def SZXC_SZGL():
	driver = login_web()
	driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div[1]/div/div[1]/div[13]").click()
	element = driver.find_element_by_xpath("//*[@id='root']/div/div/div[1]/div[1]/div/div[1]/div[13]/div[2]/a[7]")
	driver.execute_script("arguments[0].click();", element)
	time.sleep(1)
	#添加
	driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[1]/div/div/div/button").click()
	time.sleep(2)
	driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/form/div[1]/div/div/div").click()
	time.sleep(2)
	driver.find_element_by_xpath("//*[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft']/div/ul/li[3]").click()
	driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/form/div[3]/div/div/div/span/div/i").click()
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/table[@class='el-year-table']/tbody/tr[1]/td[2]/a").click()
	driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/form/div[4]/div/div/input").send_keys("三资管理")
	driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='ueditor_0']"))
	driver.find_element_by_xpath("/html/body").send_keys("李克强表示，这次疫情突如其来，对人类来说是个全新的传染病，到现在可以说还是未知大于已知。病毒是没有国界的，它是全世界、全人类的敌人，各国都在进行防控，也在探索中前进，目前还没有完整的经验。我们一方面要控制住疫情的发展，加快研发疫苗、有效药物、检测试剂，这将是人类战胜这个病毒的强有力武器。中国和许多国家都在进行投入，我们也愿意开展国际合作。这些产品是全球公共产品，我们愿意共享，最终让人类能够共同战胜病毒这个敌人。")
	driver.switch_to.default_content()
	driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/button[2]").click()
	capture(driver,filephoto="D:/" + str(time.time()) + ".png")
	#查看
	driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/table/tbody/tr/td[4]/div/div/a[1]").click()
	capture(driver,filephoto="D:/" + str(time.time()) + '.png')
	driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[2]/button").click()
	#编辑
	driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/table/tbody/tr/td[4]/div/div/a[2]").click()
	time.sleep(2)
	driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div[2]/div[2]/div/form/div[4]/div/div/input").send_keys("1")
	driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div[2]/div[3]/div/button[2]").click()
	capture(driver,filephoto="D:/" + str(time.time()) + '.png')
	#删除
	driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/div/div[3]/div[2]/table/tbody/tr/td[4]/div/div/a[3]").click()
	capture(driver,filephoto="D:/" + str(time.time()) + '.png')

	time.sleep(3)
	driver.quit()
SZXC_SZGL()