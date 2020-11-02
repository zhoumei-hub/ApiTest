"""
======================
Author: 柠檬班-小简
Time: 2020/6/19 20:33
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
from configparser import ConfigParser

# 1、实例化
conf = ConfigParser()

# 2、读取配置文件
conf.read("nmb.ini",encoding="utf-8")

# 3、读取某一项配置值：get,全部都是字符串
value = conf.get("log","file_ok")
print(value)
print(type(value))

# 读取出来为布尔值
val = conf.getboolean("log","file_ok")
print(val)

# 获取当前的section
# conf.sections()
s = conf.options("log")
print(s)

# # 写入：set
# conf.set("log","file_name","py303030.log")
# # 写入文件
# conf.write(open("nmb.ini","w",encoding="utf-8"))
