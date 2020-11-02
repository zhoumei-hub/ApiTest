"""
======================
Project: firstpy
Time: 2020/9/19 17:24
Author: zhoumei
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