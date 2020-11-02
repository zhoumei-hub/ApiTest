"""
======================
Author: 柠檬班-小简
Time: 2020/6/3 20:23
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""

import keyword
print(keyword.kwlist)

# 导入  把其它的文件导进来给自己用。
"""
库：提供一系列的功能。
1、内置库/包  - 不需要安装可以直接引入使用 Lib
2、第三方库/包 - 先pip安装再使用  Lib\site-packages
3、自定义的模块/包:
   同级目录：import 模块名
   相对工程目录引入：
   
模块：.py文件   包:__init__.py的文件夹

模块名太长了，取个别名方便使用。
import 模块名 
from 包名.[包名.包名] import 模块名 
from 包名.[包名.包名] import 模块名 [as 别名]
from 包名.[包名.包名].模块名 import 变量名/函数名/类名


得到搜索路径：
import sys
sys.path

自己创建py文件的时候，命名千万不要用库名。
"""
# import sys
# for item in sys.path:
#     print(item)

# import hello
# import py_module.hello
# py_module.hello.LEVEL
# from py_module import hello
# import hello_py
#
# print(hello.LEVEL)
# print(hello_py.LEVEL)
# hello.get_level()

# from py_module.hello import LEVEL

import hello_py  # 没有使用就是灰色的



