"""  类和对象2  """


"""
1， 详细总结类和对象知识点，包括：
**类的定义
抽象描述同一类事物的功能属性，定义方法如下：
class 类名(大驼峰):
    属性
    方法(功能(函数))
    
**对象的初始化
使用魔法函数（__init__）个性化的定制对象的属性，在创建对象的同时调用。
语法：对象名 = 类名(参数1，参数2)

**类属性
直接在类中定义，不在任何实例方法中

**实例属性
定义在实例方法中的属性，一般定义在魔法函数__init__中，self.属性名定义

**实例方法
def 方法名(self):# 参数第一个是self，self代表实例本身。

**类方法
函数加上@classmethod  参数默认为cls。cls表示类本身。类可以调用，实例不能调用。
@classmethod  # 声明为类方法
def 方法名(cls):  # cls代表当前类，可以访问类属性的。
    
**静态方法
静态方法是类方法，主要是用来存一些逻辑属于类，但是和类本身没有什么交互关系的代码。
@staticmethod
def 函数名:
       
**继承
一个子类可以继承多个父类，继承后可以使用父类的方法(私有化的除外)，在子类中可以self.去调用
语法：class 子类名(父类1,父类2,父类3....父类N)

**重写
子类方法名和形参和父类相同，可以重写，调用时使用自己的。

**super 函数
子类方法名和父类相同，在继承父类的同时扩展，添加子类自己的代码
super().同名方法名()
"""


"""
2， 定义一个类 Dog, 包含 2 个属性：名字和年龄。
定义一个方法 eat 吃东西。
定义一个类 TeddyDog, 继承 Dog 类， Teddy 在吃东西的时候还会望着你，  定义方法 watch_you.
定义一个类 BabyTeddyDog, 继承 TeddyDog,  BabyTeddy 吃东西不仅会望着你，还会四处转悠， 定义方法 go_around
"""


class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def eat(self):
        print("{},{}岁,一边吃东西".format(self.name,self.age))


class TeddyDog(Dog):
    def watch_you(self):
        self.eat()
        print("一边看着你")


class BabyTeddyDog(TeddyDog):
    def go_around(self):
        self.watch_you()
        print("还在四处转悠")


bai = TeddyDog("小白",5)
bai.watch_you()

xiaoxiaobai = BabyTeddyDog("小小白",1)
xiaoxiaobai.go_around()




"""
二、选作题（不需要提交)
1.编写如下程序
编写一个工具箱类和工具类
工具类：需要有工具具的名称、功能描述、价格。
工具箱类：能够添加工具、删除工具、查看工具，并且能获取工具箱中工具的总数。
实例化几个工具。并在工具箱对象当中做添加/删除/查看工具操作，获取工具箱对象中有几个工具。
工具比如锤子、斧头、螺丝刀等工具。
"""
toollist = []

class Tool:
    def __init__(self,name,price,features):
        self.name = name
        self.price = price
        self.features = features


class ToolBox(Tool):

    def addtool(self):
        toollist.append(self.name)

    def delettool(self):
        toollist.remove(self.name)

    def viewtool(self):
        print("{},价格{}元,{}".format(self.name,self.price,self.features))

    def numtool(self):
        num = len(toollist)
        print("工具箱中工具个数为：{}，包括{}".format(num,toollist))


hammer = ToolBox("锤子","50","敲打物体使其移动或变形的工具。")
axx = ToolBox("斧头","60","是一种用于砍削的工具。")
screwdriver = ToolBox("螺丝刀","15","是一种用来拧转螺丝以使其就位的常用工具。")
# 添加工具到工具箱
hammer.addtool()
axx.addtool()
screwdriver.addtool()
# 查看工具
hammer.viewtool()
axx.viewtool()
screwdriver.viewtool()
# 工具箱工具数量
screwdriver.numtool()
# 删除工具
axx.delettool()

# 工具箱工具数量
axx.numtool()