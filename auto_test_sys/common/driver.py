#encoding:utf-8

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from capture import capture

def get_driver(url,Chromefile = 'E:/2345Downloads/chromedriver_win32/chromedriver.exe'):
    driver = webdriver.Chrome(Chromefile)  # 创建Chrome浏览器驱动实例
    driver.implicitly_wait(15)  # 设置隐式等待时间
    driver.maximize_window()  # 全屏窗口
    driver.get(url)
    return driver

# def login_web(driver):
#     # 登陆
#     driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='root']/div/div[2]/iframe"))
#     driver.find_element_by_xpath("//*[@id='account']").send_keys('13000000098')
#     driver.find_element_by_xpath("//*[@id='root']/div/div/form/div[2]/div/div/span/span/input").send_keys('123456q')  # 测试环境
#     #driver.find_element_by_xpath("//*[@id='root']/div/div/form/div[2]/div/div/span/span/input").send_keys('jgw1478') #线上
#     driver.find_element_by_xpath("//*[@id='root']/div/div/form/div[3]/div/div/span/button").click()
#     driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/span").click()
#     driver.find_element_by_xpath("//*[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft']/div/ul/li[1]").click()
#     driver.find_element_by_xpath("//*[@id='root']/div/div/button").click()
#     driver.switch_to.default_content()
#     return driver

def getelement(driver,mode,address):#确定用户元素定位方式
    try:
        if mode == "id":
            element = driver.find_element_by_id(address)
        elif mode == "classname":
            element = driver.find_element_by_class_name(address)
        elif mode == "name":
            element = driver.find_element_by_name(address)
        elif mode == "tagname":
            element = driver.find_element_by_tag_name(address)
        elif mode == 'linktext':
            element = driver.find_element_by_link_text(address)
        elif mode == 'partialtext':
            element = driver.find_element_by_partial_link_text(address)
        elif mode == 'xpath':
            element = driver.find_element_by_xpath(address)
        elif mode == 'css':
            element = driver.find_element_by_css_selector(address)
        else:
            element = None
    except:
        element = None
    return element

def asserttest(driver,xpath,string):
    try:
        assert driver.find_element_by_xpath(xpath).text == string
    except AssertionError:
        print ("error!")

def getevent(driver,event,element,string):
    if event == "click":
        element.click()
    elif event == "sendkeys":
        element.send_keys(string)
    elif event == "infarme":
        driver.switch_to.frame(element)
    elif event == 'clear':
        element.clear()
    elif event == 'select':
        Select(element).select_by_visible_text(string)
    elif event == 'quit':
        driver.quit()
    elif event == 'sleep':
        time.sleep(int(string))
    elif event == 'outfarme':
        driver.switch_to.default_content()
    elif event == 'screenshot':
        filephoto = "D:/" + str(string) + ".png"
        capture(driver,filephoto)
    elif event == 'refresh':
        driver.refresh()
    else:
        print ("操作方式输入错误，请按规范输入！"+ str(event))


