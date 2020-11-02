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

# 功能封装。函数 -
# 为什么封装成类？ --整体。：属性和行为(功能)。
# excel

# 定义类/实现类
# 生成对象。
"""
class 类名(大驼峰):
    属性
    方法(功能(函数))


self: 对象本身。
实例方法: 第一个参数是self

# 在创建对象的同时，个性化的定制对象的属性。
# 初始化：魔法函数  __init__
# 在你创建对象的同时，自动化调用。
# 类当中可有可无。

"""
# 定义类
class Dog:
    # kind = None
    # kind = "串串" # 不论类的哪一个对象，它的kind全都是一样的。
    kind = "狗"  # 类属性。所有的对象都是一样的。
    # 名字、品种，年龄

    def __init__(self,name,kind,age):
        self.name = name
        self.kind = kind
        self.age = age

    # 叫 - 方法
    def bark(self):
        print("汪汪汪。。。")

    # 吃 - 方法
    def eat(self):
        print("吃狗粮。。")

    # 跑 - 方法
    def run(self):
        print("self本身：",self)
        print("跑起来。。")


# 创建符合类的对象。-- 实例化。
# 语法：对象名 = 类名()
cqg = Dog("陈钱罐","金毛和泰迪的混血","3个月")  # cqg就是Dog类的一个对象。
print("对象本身：",cqg)
# 通过对象.属性/方法()  去获取对象的属性，去调用行为。
# print(cqg.kind)
cqg.run()
cqg.eat()
cqg.bark()
print(cqg.kind)
print("cqg对象的名字：",cqg.name)


print("**********************************")

you_jm = Dog("小金","金毛","1岁")
you_jm.run()
you_jm.bark()
print(you_jm.kind)

print("********************************")
# print(Dog.eat())
# 个性化属性 -- self
# 在创建对象的同时，个性化的定制对象的属性。
#

