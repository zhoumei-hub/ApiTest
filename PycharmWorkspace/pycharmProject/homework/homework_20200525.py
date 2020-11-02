




"""
1、 将字符串中的单词位置反转，“hello xiao mi” 转换为 “mi xiao hello”
（提示：通过字符串分割，拼接，列表反序等知识点来实现）
"""
str1 = "hello xiao mi"
# 根据空格分隔
str2= str1.split(" ")
# 切片后的列表反转再拼接成字符串
ss = " ".join(str2[::-1])
print(ss)


"""
2、字典的增删查改操作： 某比赛需要获取你的个人信息，编写一段代码要求如下：
        1、运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据通过字典存储起来，
        2、数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
        3、有一个人对你很感兴趣，平台需要您补足您的身高和联系方式； 
        4、平台为了保护你的隐私，需要你删除你的联系方式；
        5、你为了取得更好的成绩， 你添加了一项自己的擅长技能。
"""
#  1、运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据通过字典存储起来，
person_info = {
    "name" : input("请输入姓名："),
    "sex" : input("请输入性别："),
    "age" : input("请输入年龄：")
}
print(person_info)

#  2、数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码

print("我的名字{}，今年{}岁，性别{}，喜欢敲代码。".format(person_info.get("name"),person_info.get("age"),person_info.get("sex")))

# 3、有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；

person_info["height"] = input("请输入身高：")
person_info["tel"] = input("请输入联系方式：")
print(person_info)

# 4、平台为了保护你的隐私，需要你删除你的联系方式；

person_info.pop("tel")
print(person_info)

# 5、你为了取得更好的成绩， 你添加了一项自己的擅长技能。

person_skill = ["画画","打羽毛球"]
person_info["skill"] = person_skill
print(person_info)


"""
3、利用下划线将列表li=[“python”,“java”,“php”]的元素拼接成一个字符串，然后将所有字母转换为大写，
"""

li = ["python","java","php"]
str3 = "_".join(li)
ss = str3.upper()
print(ss)


"""
4、利用切片把 'http://www.python.org'中的python字符串取出来
"""

str4 = "http://www.python.org"
str5 = str4.split(".")
str6 = str5[1]
print(str6)


"""
5、有下面几个数据 ，
t1 = ("aa",11)      t2= (''bb'',22)    li1 = [("cc",11)]
请通过学过的知识点，进行相关操作变为如下字典: {"aa":11,"cc":11,"bb":22}
"""
t1 = ("aa",11)
t2= ("bb",22)
li1 = [("cc",11)]

t3 = list(li1[0])

my_dict = {
    t1[0]:t1[1],
    t3[0]:t3[1],
    t2[0]:t2[1]
}

print(my_dict)


