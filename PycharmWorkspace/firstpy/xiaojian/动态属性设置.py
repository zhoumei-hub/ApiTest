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
ss = People("xx")
# hasattr,getattr,setattr,delattr

# res = hasattr(People,"name")
# print(res)
# res = hasattr(p,"name")
# print(res)

# getattr  获取属性
# s = getattr(p,"name")
# print(s)

# setattr  如果属性存在，修改属性值。如果不存在，添加属性。
setattr(People,"kind","黄种人")
print(People.kind)

setattr(p,"kind","黄种人")
print(p.kind)
print("=================================")
# delattr(p,"name")
# print(p.name)
#
# print("=================================")
# s = isinstance(p,People)
# print(s)

# is
# print(id(p))
# print(id(ss))
# print(ss is None)
# print(type(ss) is People)

