"""
======================
Author: 柠檬班-小简
Time: 2020/6/19 21:18
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
"""
获取ini配置文件中sever,log,mysql等配置
"""

from configparser import ConfigParser
import os

from qianchengdai.Conmon.handle_path import conf_dir


class HandleConfig(ConfigParser):

    def __init__(self,file_path):
        super().__init__()
        self.read(file_path,encoding="utf-8")


file_path = os.path.join(conf_dir,"config.ini")
conf = HandleConfig(file_path)



if __name__ == '__main__':
    file_path = os.path.join(conf_dir, "config.ini")
    conf = HandleConfig(file_path)
    cc = conf.get("server","base_url")
    print(cc)
