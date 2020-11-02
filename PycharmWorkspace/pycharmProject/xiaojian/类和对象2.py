"""
======================
Author: 柠檬班-小简
Time: 2020/6/5 21:36
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""

"""
======================
Author: 柠檬班-小简
Time: 2020/6/5 20:33
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
# 我懂，但是应用起来是有点儿难的。
# 类和对象概念
# 类：同一类事物的  抽象描述(属性、功能)。
# 对象：符合类描述的  具体存在。
#

# 功能封装。函数 -
# 为什么封装成类？ --整体。：属性和行为(功能)。
# excel

# 定义类/实现类
# 生成对象。
"""
class 类名(大驼峰):
    属性
    方法(功能(函数))

1个类 ==  多个对象！
self: 对象本身。
实例方法: 第一个参数是self

# 在创建对象的同时，个性化的定制对象的属性。
# 初始化：魔法函数  __init__
# 在你创建对象的同时，自动调用。
# 类当中可有可无。
# 实例化的同时，自动调用__init__。__init__有几个参数，那你在实例化时，就要传几个。


类属性：直接在类当中定义的。不在任何的实例方法当中。
类方法：函数加上@classmethod  参数默认为cls。cls表示类本身。
      可以通过cls访问类的属性，但是不能访问实例属性。
类可以访问，对象可以访问。


实例属性：self.属性名
实例方法：参数第一个是self
    实例都是可以访问类属性，类方法的。
只有实例才可以访问。

"""
# 定义类
class Dog:
    # kind = None
    # kind = "串串" # 不论类的哪一个对象，它的kind全都是一样的。
    kind = "狗"  # 类属性。所有的对象都是一样的。
    # 名字、品种，年龄

    def __init__(self,name,kind,age):
        self.dog_name = name
        self.dog_kind = kind
        self.dog_age = age
        # flag = "hello,world!!"

    @classmethod  # 声明为类方法
    def set_kind(cls):  # cls代表当前类。可以访问类属性的。
        print("我是类行为！！")
        print(cls.kind)

    # 叫 - 方法
    def bark(self):
        print("汪汪汪。。。")
        print(self.dog_name)

    # 吃 - 方法
    def eat(self):
        print("吃狗粮。。")

    # 跑 - 方法
    def run(self):
        print(self.dog_name,"跑起来。。")

    # def sleep(self):

# 实例化的同时，自动调用__init__。__init__有几个参数，那你在实例化时，就要传几个。
cqg = Dog("陈钱罐","金毛和泰迪的混血","3个月")  # cqg就是Dog类的一个对象。
print("cqg对象的名字：",cqg.dog_name)
cqg.run()
print(cqg.kind)  # 通过实例访问类属性
# print(Dog.dog_name) # 不可以通过类访问实例属性
cqg.set_kind()  # 实例调用类方法
Dog.set_kind()  #类调用类方法


