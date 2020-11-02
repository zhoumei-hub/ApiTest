"""
======================
Author: 柠檬班-小简
Time: 2020/6/8 20:33
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
"""
实例方法
类方法
静态方法

"""

def hello():
    print("hello")

class Dog:

    def bark(self):
        print("叫")

    @classmethod
    def set_kind(cls):
        cls.kind = "狗"

    @staticmethod
    def hello(flag=True):
        print("hello,dog!!")


Dog.hello()
d = Dog()
d.hello()