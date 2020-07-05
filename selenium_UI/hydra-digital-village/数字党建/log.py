#encoding:utf-8

import logging


def mklog(msg):
        #创建logger
    logger = logging.getLogger('test')
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:

        fh = logging.FileHandler('test.log',encoding='utf-8')
        ch = logging.StreamHandler()

        formatter = logging.Formatter(
            fmt='%(asctime)s %(name)s %(filename)s %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

    logger.info(msg)

