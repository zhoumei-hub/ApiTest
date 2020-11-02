"""
======================
Author: 柠檬班-小简
Time: 2020/6/3 21:12
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""

# os模块  path处理路径
import os

"""
__file__  : 当前文件名。
获取当前文件的绝对路径：os.path.abspath(__file__)
获取当前文件所在目录：os.path.dirname
路径拼接：os.path.join

__name__ : 如果是运行当前文件，那么 它的值为：__main__
"""
print(__file__)
print("**********************************8")
# 1
res = os.path.abspath(__file__)
print(res)

# 2
s = os.path.dirname(res)  # 参数是个绝对路径
print(s)

# 3
base_dir = os.path.dirname(s)
print(base_dir)

# 4 得到项目目录下，另外一个文件的绝对路径
# 路径拼接
res = os.path.join(base_dir,"hello_py.py")
print(res)

# basedir = os.path.dirname(os.path.dirname(os.path.abspath("hello.py")))


print("***********************************")
result = os.path.isdir(r"D:\Pychram-Workspace\py30\hello_py.py")
print(result)

files = os.listdir(r"D:\Pychram-Workspace\py30\py_module")
print(files)

print(os.path.realpath(__file__))





