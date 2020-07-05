#encoding:utf-8
import yaml
import logging.config
import logging



logging.basicConfig(level=logging.DEBUG , filename='log.txt',filemode='a+',format=('%(asctime)s - %(name)s - %(filename)s -%(levelname)s -  %(message)s'))

logging.info('---------fun start--------')
for i in range(9):
    for p in range(9):
        a = p*i
        b = p+1/(i+1)

        logging.info('{0} is {1}'.format(a,b))