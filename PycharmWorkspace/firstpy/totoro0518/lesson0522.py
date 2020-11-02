"""
======================
Author: 柠檬班-totoro
Time: 2020/5/22 20:34
Project: firstpy
Company: 湖南零檬信息技术有限公司
======================
"""
# person_info =
#
# # 替换操作
# # replace(原字符串当中要被替换的,新的字符串)
# sss = person_info.replace


"""
# 格式化 format函数
# 字符串.format()
# 动态的去改变字符串的值：占位符{}.有几个占位符就需要几个替代参数
# 不需要指定数据类型
age = input("年龄：")
age = int(age)
name = input("名字：")
# 1
print("我的年龄是：{}岁，我的名字是：{}".format(age,name))

# 2 有一些数据需要重复使用，在占位符{}里加索引
print("我的年龄是：{0}岁，我的名字是{1}，我的老师是{1}，我喜欢{2}".format(age,name,"睡觉"))
"""
# 列表(list) 是一种数据类型 字符串（str） 布尔值（bool） 整数（int） 浮点数（floot）
list_my = [] # 空列表
print(list_my)
# 可以放任意类型的数据
list_python30 = ["小雨点","A","下雨","天晴",1,True,2.0]

# 有序，通过下标取值，0开始
# 取值方式 列表名[下标]
print(list_python30[0])

# 通过值获取下标 列表.index
print(list_python30.index("小雨点"))

# 不可变类型：数字、布尔值、字符串
# 列表：可变类型，可以增删改

#1、添加数据
# 默认追加在末尾 列表.append(数据)
list_python30.append("baba")
print(list_python30)

# 2)插队：麻麻  insert(索引，值) 插在索引的前面，位置针对原来的列表
list_python30.insert(0,"麻麻")
print(list_python30)

# 3)合并 列表.extend 将列表2追加到列表1
new_list = ["小米","华为"]
list_python30.extend(new_list)
print(list_python30)

# 2、修改数据 修改列表中的某个值 ，找到索引，并修改索引的值
index = list_python30.index("baba")
list_python30[index] = "爸爸"
print(list_python30)

# 3、删除数据
# 1）删除某个位置的值
# 列表.remove(数据) 删除列表中第一次出现的指定数据
list_python30.remove(True)
print(list_python30)

# del 列表[索引]
del list_python30[2]
print(list_python30)

# 列表.pop 删除列表末尾数据
list_python30.pop()
print(list_python30)

# 列表.clear 清空列表
# list_python30.clear()
# print(list_python30)

# list_python30.count()

# 获取列表的长度 len()
print(len(list_python30))
item = list_python30[len(list_python30)-1]
print(item)

# 列表一般都是放同一类数据
# 算术运算符、比较、赋值、逻辑
#  成员运算符 成员in列表 成员 not in 列表/字符串

result = '小雨点' in list_python30
print(result)

















