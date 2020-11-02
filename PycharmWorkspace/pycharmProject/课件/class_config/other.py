"""
======================
Author: 柠檬班-小简
Time: 2020/6/19 21:54
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
from class_config.handle_config import conf

value = conf.get("mysql","user")
print(value)