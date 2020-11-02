"""
======================
Author: 柠檬班-totoro
Time: 2020/5/31 18:37
Project: firstpy
Company: 湖南零檬信息技术有限公司
======================
"""


"""
1、定义函数：（要求：定义函数处理逻辑。input输入操作在函数之外。）
将用户输入的所有数字相乘之后对20取余数
用户输入的数字个数不确定
"""
# str1 = input("请输入要计算的数字，以逗号隔开：")
# list_a = str1.split(",")
# print("您输入的数字为：{}".format(list_a))
#
# def my_calculate(*args):
#     if len(args) == 0:
#         count = 0
#     else:
#         count1 = 1
#         for index in range(len(args)):
#             count1 = count1 * int(args[index])
#         count = count1 % 20
#     print("数字相乘，除20的余数为：{}".format(count))
#
# my_calculate(*list_a)



"""
2、编写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
"""

# str2 = input("请输入列表元素，以逗号隔开：")
# ll = str2.split(",")
# print("原始列表为：{}".format(ll))
# def my_list(list_b):
#     if len(list_b) > 2:
#         new_list = list_b[0:2]
#     else:
#         new_list = list_b
#     print("新列表为：{}".format(new_list))
# my_list(ll)



"""
3、列表去重
定义一个函数 def remove_element(m_list):，将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素
"""

# list_c = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
# def remove_element(m_list):
#     list_d = []
#     for element in m_list:
#         if element not in list_d:
#             list_d.append(element)
#     print(list_d)
# remove_element(list_c)



"""
4、编写如下程序（要求：定义函数处理逻辑。input输入操作在函数之外。）
尝试函数封装：
输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
b.根据BMI指数，给与相应提醒
低于18.5： 过轻 18.5-25：   正常 25-28：      过重 28-32：      肥胖 高于32：   严重肥胖
"""
# height = input("请输入您的身高(m)：")
# weight = input("请输入您的体重(kg)：")
# def your_bmi(heigh,weigh):
#     bmi = float(weigh) / float(heigh) ** 2
#     print("您的BMI值为：{:.2f}".format(bmi))
#     if bmi < 18.5:
#         print("过轻")
#     elif 18.5 <= bmi <= 25:
#         print("正常")
#     elif 25 < bmi <= 28:
#         print("过重")
#     elif 28 < bmi <= 32:
#         print("肥胖")
#     else:
#         print("严重肥胖")
#
# your_bmi(height,weight)

"""
5， 定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典
"""

# str5 = input("请输入一个字符串：")
# dict5 = {
#     "name" : input("请输入姓名："),
#     "sex" : input("请输入性别："),
#     "age" : input("请输入年龄：")
# }
# def my_dict(str,**kwargs):
#     if str not in kwargs.values():
#         kwargs["new"] = str
#     print(kwargs)
#     return kwargs
#
# my_dict(str5,**dict5)


"""
6， 通过定义一个计算器函数，调用函数传递两个参数，然后提示选择【1】加 【2】减【3】乘 【4】除 操作，选择之后返回对应操作的值。
"""
# n1 = float(input("请输入第一个参数："))
# print("请根据提示选择，【1】加\t【2】减\t【3】乘\t【4】除")
# operat = int(input("请选择："))
# n2 = float(input("请输入第二个参数:"))
#
# def Calculator(str1,str2,op):
#     if op == 1:
#         cal = str1 + str2
#     elif op == 2:
#         cal = str1 - str2
#     elif op == 3:
#         cal = str1 * str2
#     elif op == 4:
#         cal = str1 / str2
#     else:
#         print("你输入的操作有误！")
#     print("您的计算结果为：{:.2f}".format(cal))
#
# Calculator(n1,n2,operat)

"""
7， 一个足球队在寻找年龄在15岁到22岁的女孩做拉拉队员（包括15岁和22岁）加入。编写一个程序，询问用户的性别和年龄，然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。(

（要求：定义函数处理逻辑。但是input输入操作在函数之外。在for循环当中，调用input和自己定义的函数)
"""

def laladui(sex,age):
    if sex != "女":
        print("您的性别不符合条件！")
        return 0
    else:
        if 15 <= age <= 22:
            print("满足条件，欢迎加入！")
            return 1
        else:
            print("您的年龄不符合要求！")
            return 0

num_m = 0
for i in range(10):
    print("第{}人：".format(i+1))
    sss = input("请输入您的性别：")
    aaa = int(input("请输入您的年龄："))
    ccc = laladui(sss,aaa)
    num_m += int(ccc)
    print("满足条件总人数为：{}人".format(num_m))





