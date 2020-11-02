"""
======================
Author: 柠檬班-小简
Time: 2020/6/19 21:18
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
from configparser import ConfigParser

class HandleConfig(ConfigParser):

    def __init__(self,file_path):
        super().__init__()
        self.read(file_path, encoding="utf-8")


import os
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"nmb.ini")
conf = HandleConfig(file_path)

if __name__ == '__main__':
    conf = HandleConfig("nmb.ini")
    conf.get("log","name")
