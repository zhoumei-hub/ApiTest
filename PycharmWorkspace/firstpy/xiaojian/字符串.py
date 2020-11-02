"""
======================
Author: 柠檬班-小简
Time: 2020/5/20 21:02
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
# 空字符串
s = ""  # 字符串
s1 = None  # 不代表任何一个数据类型。
# print(s)
# print(s1)
# print(type(s1))

# 成双成对的。双引号开头，必须以双引号结尾。单引号开头，必须以单引号结尾。
# person_info = '我是小简老师，我喜欢"python30期"，我今天跟你们过节呢！'
# print(person_info)
#
# # 字符串的转义：\   作为长规的数据内容，不作为python特别的处理。
# person_info = '我是小简老师，我喜欢\'python30期\'，我今天跟你们过节呢！'

# 字符串：是不可变数据类型。只读不能够对字符串本身去修改。
# 数字、布尔值 都是不可变类型。


# 取某一个位置的值
# 从0开始。正向，+1  逆向 -1   变量名[索引]
# print(person_info[6])
# print(person_info[-1])

# 区间取值 -  子字符串   起始点  结束点  步长
# 从0开始，到下标为6   变量名[起:结束]
# 如果步长为正数，表示正向切片。  从0开始
# 如果步长为负数，表示负向切片。  倒着
#
# print(person_info[0:6])  # 0,1,2,3,4,5  步长:1
# print(person_info[:7])  # 0,1,2,3,4,5,6
#
# print(person_info[:7:2]) # 0,2,4,6  步长为2
# # print(person_info[7:1:-2]) # 7,5,3  步长为2
# print(person_info[-1:-10:-1]) # -1,-2,-3,-4,-5,-6,-7,-8,-9
#
# print(person_info[:])
# print(person_info[::-1])  # 面试

print("******************  常用方法/功能   *******************")
# find(子字符串) 正向查找子字符串，找到返回的值都是>=0。没找着就是-1
# index = person_info.find("我是小简老师111")  # 0 正向查找子字符串。
# print(index)
#
# # count(字符/字符串) 统计在原字符串当中出现的次数
# count = person_info.count("我")
# print(count)
#
# # len(字符串)  获取字符串的总长度
# print(len(person_info))
#
# # upper() 将字符串的字母转换成大写。重新生成一个字符串。不会修改原来的字符串。
# res = person_info.upper()
# print(res)
# print(person_info)

person_info = '我是小简老师，我喜欢"python30期"，我今天跟你们过节呢！'
# split() 分割。分隔符：
# sep: 分隔符。不会出现在分割后的数据当中。
# maxsplit: 1  分割的次数。
str_pian = person_info.split("，")
print(str_pian)  # str_pian是个列表

s2 = person_info.split("我")
print(s2)

# join()  拼接。按照拼接符将其拼接起来。
# 把支离破碎的几个字符串，拼接成一个完整的字符串！
# 1、拼接符：一定是字符串。;
ss = "    ".join(str_pian)  # 按照一定的规律去拼接 列表里的字符串。
print(ss)

# 替换操作
# replace(原字符串当中要被替换，新的字符)
sss = person_info.replace("我","你")
print(person_info)
print(sss)

# 格式化 format函数
# 字符串.format()
# 动态的去改变字符串的值：占位符{}。有几个占位符，就需要几个替换参数。
# 不需要指定数据类型。
# age = input("年龄：")
# # age = int(age)
# name = input("名字")
#
# # 1 没写序号，顺序赋值
# print("我的年龄是: {}岁，我的名字是：{}".format(age,name))
#
# # 2 有一些数据需要重复使用。在占位符{}里加索引。
# # {0}  {1}  {2}。根据序号对应的位置，去赋值。
# print("我的年龄是: {1}岁，我的名字是：{2},我的老师是：{2}。我喜欢干什么：{0}".format(age,name,"睡觉"))
#

# 3、只保留2位小数点{:.2f}.百分比：{:.2%}会对数据乘以100
# print("我昨天的作业得了{:.2f} 分   完成度为 {:.2%}".format(89.88888,0.98))
#

# print("我的成绩是：%.2f" % 2.12)

print(" hello,world! \n hello,py30!")  # \n 表示换行

print(" hello,world! \t hello,py30!")  # \t tab

print(r" hello,world! \n hello,py30!")  # r 取消转义，正常输出！！

# 拼接 +  字符串
str1= " hello,world!!!"
str2 = "hello,python!"
str3 = "No!!!"
int1 = 20
print(str1 + str2 + str3 + str2)
