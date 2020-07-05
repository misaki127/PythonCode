#encoding:utf-8
import sys
import logging
sys.path.append('D:/python/auto_test_sys/common')
sys.path.append('D:/python/auto_test_sys/config')
from mkexcel import read_excel,write_excel
from driver import get_driver,getelement,asserttest,getevent
from mkconfig import read_config

logging.basicConfig(level=logging.DEBUG , filename='D:/python/auto_test_sys/log/log.txt',filemode='a+',format=('%(asctime)s - %(name)s - %(filename)s -%(levelname)s -  %(message)s'))

filename='D:/python/auto_test_sys/config/selenium.config'
config_data = read_config(filename)
logging.info('read config file is' + filename)

model = 'test' #测试为test，线上为online
logging.info('model=' + model)
url = config_data[model][0][1]
logging.info('open url is'+ url)

fileexcel = config_data[model][3][1]
logging.info('read excel file is' + fileexcel)
all_content = read_excel(fileexcel)
logging.info('read data is' + str(all_content))


errorNum = 0
success = False
while errorNum < 5 and not success:
    try:
        for i in all_content[0]:

            driver = get_driver(url)
            logging.info('open Chrome')
            try:
                data = all_content[1][i]
                for p in range(1,len(data)):
                    string = str(data[p][4])  # 内容
                    address = str(data[p][3])  # 地址
                    mode = str(data[p][1])  # 定位方式
                    event = str(data[p][2])  # 操作方法
                    logging.info('data:string is' + string +',address is' + address + ',mode is'+ mode +',event is'+ event)
                    element = getelement(driver, mode, address)
                    logging.debug(type(element))
                    getevent(driver, event, element, string)
                    logging.debug(getevent.__name__)

            except:
                logging.info('error , now i is' +str(i))
        success = True
    except:
        errorNum += 1
        if errorNum >= 5:
            break
