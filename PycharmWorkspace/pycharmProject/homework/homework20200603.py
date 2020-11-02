

"""
1. 异常捕获的语法是什么样的？    请列举你遇到过的/见过的错误类型。
"""

"""   异常捕获的语法如下
try:
    可能会出错的代码
except:
    如果出错捕获异常
[else:

finally:

]
"""

"""  常见的错误类型
name 'a' is not defined  没有定义
invalid syntax  语法无效
could not convert string to float: 'a'   字符串“a”不能转换float
list assignment index out of range   索引超出范围
"""




"""
2.编写如下程序
优化去生鲜超市买橘子程序

a.收银员输入橘子的价格，单位：元／斤

b.收银员输入用户购买橘子的重量，单位：斤

c.计算并且 输出 付款金额

新需求：

d.使用捕获异常的方式，来处理用户输入无效数据的情况
"""
a = 1
while a == 1:
    try:
        a += 1
        price = float(input("请输入橘子的价格（元/斤）："))
        weight = float(input("请输入橘子的重量（斤）："))
    except:
        print("价格或者重量输入不正确，请重新输入")
        a = 1
    else:
        count = price * weight
        print("付款金额为{:.2f}".format(count))


