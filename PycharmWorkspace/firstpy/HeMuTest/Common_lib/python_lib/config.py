#! /usr/bin/env python3
# -*- coding utf-8 -*-
import os
import sys
from datetime import datetime

#window_use
CONFIG_FILE = 'E:\\pycharm\\HeMuTest\\Common_config\\config_data.txt'
LOG_URL = 'E:\\pycharm\\HeMuTest\\logs\\'

#linux_use
# current_path = os.getcwd()
# CONFIG_FILE_DIR = os.path.abspath(current_path + os.path.sep + 'Common_config')
# LOG_URL = os.path.abspath(current_path + os.path.sep + 'logs') + '/'
# CONFIG_FILE = CONFIG_FILE_DIR + '/' + 'config_data.txt'

LOG_FILE_NAME = 'python' + datetime.now().date().strftime('%Y%m%d') + '.log'


if __name__ == '__main__':
    print('ok')
    # print(CURRENT_DIR)
    print(CONFIG_FILE)
    print(LOG_URL)
    # pwd = os.getcwd()
    # father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
    # grader_father = os.path.abspath(os.path.dirname(pwd) + os.path.sep + "..")
    # config_path = os.path.abspath(grader_father + os.path.sep + 'Common_config')
    # print(pwd)
    # print(father_path)
    # print(grader_father)
    # print(config_path)


