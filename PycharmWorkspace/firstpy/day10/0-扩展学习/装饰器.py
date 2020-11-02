"""
======================
Project: firstpy
Time: 2020/11/1 12:46
Author: zhoumei
======================
"""

"""
装饰器不一定是闭包

开放封闭原则:
封闭：已经实现的功能代码对修改是封闭的
开放：对代码功能的扩展功能是开放的
"""
def doc(func):
    """
    :param func: 接收被装饰的函数
    :return:
    """
    def wrapper(*args):
        print("装饰器拓展功能")
        print("打印函数的参数",args)
#       调用原函数功能
        func(*args)

    return wrapper

#  @doc的作用等价于add_number = doc(add_number(a,b))
@doc
def add_number1(a):
    print("a+b的结果：", a ** 2)


@doc
def add_number2(a,b):
    print("a+b的结果：", a + b)

@doc
def add_number3(a,b,c):
    print("a+b的结果：", a + b + c)

print("-----------")
add_number1(3)
print("-----------")
add_number2(3,7)
print("-----------")
add_number3(3,7,4)
