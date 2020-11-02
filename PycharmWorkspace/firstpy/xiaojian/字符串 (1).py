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
person_info = '我是小简老师，我喜欢"python30期"，我今天跟你们过节呢！'

# 取某一个位置的值
# 从0开始。正向，+1  逆向 -1   变量名[索引]
print(person_info[6])
print(person_info[-1])

# 区间取值 -  子字符串   起始点  结束点  步长
# 从0开始，到下标为6   变量名[起:结束]
# 如果步长为正数，表示正向切片。  从0开始
# 如果步长为负数，表示负向切片。  倒着

print(person_info[0:6])  # 0,1,2,3,4,5  步长:1
print(person_info[:7])  # 0,1,2,3,4,5,6

print(person_info[:7:2]) # 0,2,4,6  步长为2
# print(person_info[7:1:-2]) # 7,5,3  步长为2
print(person_info[-1:-10:-1]) # -1,-2,-3,-4,-5,-6,-7,-8,-9

print(person_info[:])
print(person_info[::-1])  # 面试

print("******************  常用方法/功能   *******************")
# find(子字符串) 正向查找子字符串，找到返回的值都是>=0。没找着就是-1
index = person_info.find("我是小简老师111")  # 0 正向查找子字符串。
print(index)

# count(字符/字符串) 统计在原字符串当中出现的次数
count = person_info.count("我")
print(count)

# len(字符串)  获取字符串的总长度
print(len(person_info))

# upper() 将字符串的字母转换成大写。重新生成一个字符串。不会修改原来的字符串。
res = person_info.upper()
print(res)
print(person_info)







