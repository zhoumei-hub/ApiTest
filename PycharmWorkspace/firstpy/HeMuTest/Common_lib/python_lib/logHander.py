#! /usr/bin/env python3
# -*- coding utf-8 -*-
# import time
import logging
from logging import handlers
from config import LOG_URL,LOG_FILE_NAME
# from config import LOG_FILE_NAME,LOG_URL

class LogHander(object):
    level_set = {'debug':logging.DEBUG, 'info':logging.INFO, 'warning':logging.WARNING, 'error':logging.ERROR, 'critical':logging.CRITICAL}
    def __init__(self, logfile_name, level='info',file_split_way= 'D',bak_count=5, time_fmt = '%(asctime)s - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(logfile_name)
        self.logger.setLevel(self.level_set.get(level)) # 日志打印级别
        time_fmt = logging.Formatter(time_fmt)  # 日志打印时间格式
        screen_put = logging.StreamHandler()  # 实例化屏幕打印对象
        logfile_put = handlers.TimedRotatingFileHandler(filename=logfile_name, when=file_split_way, backupCount=bak_count, encoding='utf-8')
        """
        实例化日志文件输入的对象
        interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        S 秒,M 分,H 小时,D 天,W 每星期（interval==0时代表星期一）,midnight 每天凌晨
        """
        screen_put.setFormatter(time_fmt)  # 设置文件里写入的格式
        logfile_put.setFormatter(time_fmt)
        self.logger.addHandler(screen_put)  # 把对象加到logger里
        self.logger.addHandler(logfile_put)

LOGFILE = LOG_URL + LOG_FILE_NAME
log_output = LogHander(LOGFILE)
def log_print(*content):
    log_output.logger.info(content)

if __name__ == '__main__':
    log_print('hello,world')