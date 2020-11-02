"""
======================
Author: 柠檬班-小简
Time: 2020/6/19 20:27
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
"""
.ini
[section]
option=value
option=value

[section]
option=value
option=value

[section]
option=value
option=value


.ini
读取：
ConfigParse类
1、引入  from configparse import Configparse
2、conf = Configparse()
3、读取.ini文件
   conf.read(fs,encoding="utf-8")
4、通过get方法，获取section下的option的值。
   value = get(section,option) # 字符串
   
   boolean: getboolean() # 布尔值
   int:getint()   # 整数
   float:getfloat()  # 符点数


from configparser import ConfigParser
class HandleConfig(ConfigParser):

    def __init__(self,file_path):
        super().__init__()
        self.read(file_path, encoding="utf-8")
conf = HandleConfig(file_path)


.yaml
  字典、列表
  pyyaml
  import yaml
  1、打开文件 open
  2、加载文件数据为字典对象/列表对象
  yaml.load(fs,loader=yaml.FullLoader)



unittest
openpyxl
logger
.ini

"""