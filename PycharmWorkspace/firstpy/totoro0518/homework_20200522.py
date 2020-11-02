"""
======================
Author: 柠檬班python30期-totoro
Time: 2020/5/23 11:33
Project: firstpy
======================
"""
"""
1、.删除如下列表中的"矮穷丑"，写出 2 种或以上方法：
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
"""
# 方法1
info1 = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
info1.remove("矮穷丑")
print(info1)

# 方法1
info2 = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "狼的眼睛是啥样的"]
del info2[3]
print(info2)



"""
2、现在有一个列表 li2=[1，2，3，4，5]，
请通过相关的操作改成li2 = [0，1，2，3，66，4，5，11，22，33]，
"""
li2 = [1,2,3,4,5]
li2.insert(3,66)
li3 = [11,22,33]
li2.extend(li3)
li2.insert(0,0)
print(li2)


"""
3、请写出删除列表中元素的方法。
"""

# 1）删除某个值 从最前面开始
li2.remove(66)
# 2） del 列表[索引]  删除某个位置的值
del li2[2]
# 3）列表.pop 删除列表末尾数据
li2.pop()
# 4）清空列表
li2.clear()


"""
4、有5道小题（使用列表操作完成）：
a.  某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄
b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
c, 平台为了保护你的隐私，需要你删除你的联系方式；
d, 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。
e, 你进一步添加自己的兴趣，至少需要 3 项(列表中成员可以是任意类型，此题考虑添加一个成员，且成员是列表哦！！！)。
"""

# a.某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄
name = input("姓名：")
sex = input("性别：")
age = input("年龄：")
person_info = [name,sex,age]
print(person_info)

# b. 有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
height =  input("身高：")
tel = input("联系方式：")
person_info.append(height)
person_info.append(tel)
print(person_info)

# 平台为了保护你的隐私，需要你删除你的联系方式；
person_info.pop()
print(person_info)

# d, 你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。

person_info[0] = "小雨点"
person_info[3] = "170"
print(person_info)

# e, 你进一步添加自己的兴趣，至少需要 3 项(列表中成员可以是任意类型，此题考虑添加一个成员，且成员是列表哦！！！)。

add_info = ["看电影","吃美食","逛街"]
person_info.extend(add_info)
print(person_info)