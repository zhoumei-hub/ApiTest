"""
======================
Author: 柠檬班-小简
Time: 2020/6/8 20:42
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
"""
继承语法 ：class 子类(父类)

私有化：
       父类当中以__开头的属性/方法，仅定义父类内部可用.
       父类对象和子类/子类对象都不可以用。

# 潜规则 - 告诉你这是私有化的，全靠对象自觉。硬要用也是可以的，不会报错。
类定义时，_开头的属性/方法，父类内部/子类内部都可以用。
        父/子对象不建议使用。
  
子类和父类有同名方法的时候：
  重写
  
  继承使用父类的同名方法。但是在父类的基础上，再拓展内容。
  super().同名方法
  
1个父类  =》 N个子类

多继承：任何一个类，可以有N个父类
语法：class 类名(父类1,父类2,父类3....父类N)
问题：菱形继承？？(自行查资料)

继承来讲：自己有用自己的，自己没有用，一层层往上找。


祖先类(默认继承)：object

"""
# 父类
class Base:

    def __init__(self,name):
        print("初始化对象：{}！".format(self))
        self.name = name

    def eat(self):
        print("吃")

    def sleep(self):
        print("睡")

    def hawl(self):
        print("嚎")


class Cat(Base):

    def __init__(self,name,sex):
        super().__init__(name)
        self.sex = sex

    def climb(self):
        print("Cat会爬树！！")
        self.eat() #

    def sleep(self):
        # 完全覆盖。一点都不用父类的。
        # print("cat呼呼大睡！！！")
        # 继承使用父类的同名方法。但是在父类的基础上，再拓展内容。
        super().sleep()
        print("我使用爸爸睡觉的姿势，顺便再加了一个姿势！！")



c = Cat("英短","母")
c.sleep()












# class Dog(Base):
#     def catch_mouse(self):
#         print("Dog会抓老鼠！")
#
#
#
#
# c = Cat()
# d = Dog()
# d.catch_mouse()