"""
======================
Author: 柠檬班-小简
Time: 2020/6/8 21:51
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""

class People:

    def __init__(self,name):
        self.name = name

p = People("xj")
# print(p.name)
# p.name = "黄花菜"
# print(p.name)
# p.sex = "女"  #
# print(p.sex)

res = hasattr(People,"name")
print(res)
res = hasattr(p,"name")
print(res)