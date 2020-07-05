#encoding:utf-8


import unittest
import time
import logging
import subprocess

# from 三资管理 import SZXC_SZGL
# from 优秀党员 import SZXC_YXDY
# from log import mklog


logging.basicConfig(level=logging.DEBUG , filename='D:/python/auto_test_sys/log/log.txt',filemode='a+',format=('%(asctime)s - %(name)s - %(filename)s -%(levelname)s -  %(message)s'))

# class Test_php(unittest.TestCase):
#     def test_SZGL(self):
#         a = 1
#         try:
#             p = SZXC_SZGL()
#             mklog('正在运行：' + str(p.__name__))
#         except:
#             a = 0
#             pass
#         self.assertEqual(a,0,'运行成功')
#
#     def test_run(self):
#         a = 1
#         b = 2
#         self.assertEqual(a,b,'111')
#
#
# if __name__ == '__main__':
#     unittest.main()



import os

def run():

    logging.info('start')
    t = 1
    logging.info('waitting time is ' + str(t))
    list_test = ["三资管理", '优秀党员', '党员学习', '党组织管理', '决策公示', '孤寡老人扶助', '工作动态', '我家宝贝', '村民表彰', '残疾人扶助', '民生公示-低保五保',
                  '民生公示-危房改造', '民生公示-大病救助', '民生公示-留守儿童'
      , '组织建设', '责任组管理', '贫困户评定', '通知公告', '集体经济', '项目公开']
    # list_test = ['党组织管理']
    logging.info('all test is '+str(list_test))
    for i in range(len(list_test)):
        test = 'python ./' + list_test[i] + '.py'
        logging.info(test + ' is start')
        f = os.system(test)
        #f =subprocess.Popen(test, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
        try:
            if f == 0:
                logging.info(test + ' is success')
            else:
                logging.info(test + ' is fali')
                # logging.info(str(p.stdout.read()))
            time.sleep(t)
        except:
            logging.info('error!')




run()

