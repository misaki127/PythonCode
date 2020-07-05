#enconding:utf-8

from selenium import webdriver
import time

def login_web():
    url = "http://ceshicun.jgwcjm.com/#/user/login"  #线上
    #url = 'http://system.nine.kf315.net/#/user/login'  # 测试环境
    #url = 'http://ceshicun.system.kf315.net'
    driver = webdriver.Chrome("E:/2345Downloads/chromedriver_win32/chromedriver.exe")  # 创建Chrome浏览器驱动实例
    driver.implicitly_wait(15)  # 设置隐式等待时间
    driver.maximize_window()  # 全屏窗口
    driver.get(url)
    # 登陆
    driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='root']/div/div[2]/iframe"))
    driver.find_element_by_xpath("//*[@id='account']").send_keys('13000000098')
    #driver.find_element_by_xpath("//*[@id='root']/div/div/form/div[2]/div/div/span/span/input").send_keys('123456q')  # 测试环境
    driver.find_element_by_xpath("//*[@id='root']/div/div/form/div[2]/div/div/span/span/input").send_keys('jgw1478') #线上
    driver.find_element_by_xpath("//*[@id='root']/div/div/form/div[3]/div/div/span/button").click()
    driver.find_element_by_xpath("//*[@id='root']/div/div/div/div/span").click()
    driver.find_element_by_xpath("//*[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft']/div/ul/li[1]").click()
    driver.find_element_by_xpath("//*[@id='root']/div/div/button").click()
    driver.switch_to.default_content()
    return driver


def capture(driver,filephoto):  #截取屏幕
	driver.execute_script("""
		  (function () {
		  var y = 0;
		  var step = 100;
		  window.scroll(0, 0);
		  function f() {
		  if (y < document.body.scrollHeight) {
		  y += step;
		  window.scroll(0, y);
		  setTimeout(f, 50);
		  } else {
		  window.scroll(0, 0);
		  document.title += "scroll-done";
		  }
		  }
		  setTimeout(f, 1000);
		  })();
		 """)
	for i in range(30):
		if "scroll-done" in driver.title:
			break
		time.sleep(1)
	beg = time.time()
	for i in range(10):
		driver.save_screenshot(filephoto)
	end = time.time()
	print("截屏操作时间：")
	print(end - beg)
