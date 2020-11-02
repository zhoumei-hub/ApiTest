"""
=====================
配置文件引入封装
======================
"""
from configparser import ConfigParser
import os

class HandleConfig(ConfigParser):
    def __init__(self,file_path):
        super().__init__()
        self.read(file_path, encoding="utf-8")


file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"nmb.ini")
conf = HandleConfig(file_path)

if __name__ == '__main__':
    conf = HandleConfig("nmb.ini")
    conf.get("log","name")
