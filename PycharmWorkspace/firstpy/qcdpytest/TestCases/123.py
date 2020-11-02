"""
======================
Project: firstpy
Time: 2020/10/10 15:46
Author: zhoumei
======================
"""

# str = "Test Engneer"
# ss = str[::-1]
# print(ss)

# sum = 0
# num =1
# for i in range(1,10001):
#     for j in range(1,11):
#         num *= i
#     sum += num
# print(sum)

"""
什么是lambda函数？它有什么好处？请结合lambda编程实现从1~100中过滤出21的倍数。
lambda 又叫匿名函数，平时我们在使用函数之前先要定义。而用匿名函数我们不需要事先定义，直接通过 lambda
            表达式就可以了，在逻辑比较简单的函数调用过程中使用起来更加方便。

a = filter(lambda x: x%21==0, range(1, 101))

print(list(a))
"""


"""
1.编写如下程序使用while循环实现输出2 - 3 + 4 - 5 + 6 ... + 100 的和
"""
# i = 2   # 定义循环变量
# num = 0  # 定义一个变量用于保存结果
# while i <= 100:
#      if i % 2 == 0:
#         num += i
#      else:
#         num -= i
#      i += 1  # 修改循环变量
# print("2 - 3 + 4 - 5 + 6 ... + 100之和为{}".format(num))

"""
 2.编写如下程序
用户输入考试成绩，当分数高于90（包含90）时打印A；否则如果分数高于80（包含80）时打印B；否则如果当分数高于70（包含）时打印C；否则如果当分数高于60（包含60）时打印D；其他情况就打印E
"""
# score = float(input("请输入你的考试成绩："))
# if score >= 90:
#     print("你成绩为：A")
# elif score >= 80:
#     print("你成绩为：B")
# elif score >= 70:
#     print("你成绩为：C")
# elif score >= 60:
#    print("你成绩为：D")
# else:
#    print("你成绩为：E")

"""
3.编写如下程序
假设一年的定期利率为3.52%，需要几年才能让定期存款连本带息的翻一番（例如：需要几年10000才能变成20000）
"""
# save_money = float(input("请输入你要存入银行的钱："))
# print("你存了{}元到银行!".format(save_money))
# TOTAL_MONEY = save_money * 2   # 定义变量用于保存总钱数
# year = 1    # 定义变量用于记录年份
# while save_money < TOTAL_MONEY:
#     save_money *= (1 + 0.0352)
#     year += 1
# print("定期利率为3.52%，需要{}年本金和才能翻一番。".format(year))

"""
编写如下程序从键盘获取一个数字，然后计算它的阶乘，例如输入的是3，那么即计算3!的结果，并输出 提示：
 a. 1!等于 1
 b. 2!等于 1*2
 c. 3!等于 1*2*3 
 d. n!等于 1*2*3*...*n
"""
# def is_int(int_num):
#     """
#     :param int_num:
#     :return:
#     """
#     if isinstance(int_num, str):  # 判断是否为字符串类型
#         if int_num.isdigit():
#             return True
#         else:
#             return False
#     elif isinstance(int_num, int):  # 判断是否为整数类型
#         return True
#     else:
#         return False
#
# def count_factorial(one_num):
#     """    count one_num's fatorial    """
#     result = 1
#     if one_num < 0:
#         print("{}为负数，没有阶乘！".format(one_num))
#         return None
#     elif one_num in (0, 1):
#         return 1
#     else:
#         for i in range(1, one_num + 1):
#             result *= i
#         return result
#
#
# input_num = input("请输入一个正整数：")
# if is_int(input_num):
#      input_num = int(input_num)
#      print("{}的阶乘为：{}".format(input_num, count_factorial(input_num)))
# else:
#      print("输入的{}有误，请输入一个正整数!".format(input_num))

"""
拆数字游戏
"""
# import random
# computer = random.randint(1,100)
# print(computer)
# while True:
#     pp = int(input("请输入一个数字："))
#     if computer > pp:
#         print("大一点")
#     elif computer < pp:
#         print("小一点")
#     else:
#         print("猜对了")
#         break

"""
斐波那契 Fibonacci
"""
# 一、从最大值考虑
# numMax = int(input('please input  a maxnumber : '))
# def fibonacci(numMax):
#     c = []
#     a, b = 0, 1
#     while a <= numMax:
#         c.append(a)
#         # a, b = b, a + b
#     print(c)
# fibonacci(numMax)

# 二、从位数考虑 0 1 1 2

# num = int(input('please input  a number : '))
# def fibonacci(num):
#     list = []
#     for i in range(num):
#         if i <= 1:
#             list.append(i)
#         else:
#             ll = list[-2] + list[-1]
#             list.append(ll)
#     return list
# print("斐波那契前{}位的数列为:{}".format(num,fibonacci(num)))  # 输出num位数列