"""
======================
Author: 柠檬班-小简
Time: 2020/6/19 21:45
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""

import yaml

with open("nmb.yaml",encoding="utf-8") as fs:
    data = yaml.load(fs,yaml.FullLoader)
    print(data)
    for key,value in data.items():
        print(key)
        print(value)