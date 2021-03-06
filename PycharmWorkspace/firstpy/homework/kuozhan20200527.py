"""
======================
Author: 柠檬班-totoro
Time: 2020/5/29 19:36
Project: firstpy
Company: 湖南零檬信息技术有限公司
======================
"""



"""
使用遍历循环完成剪刀石头布游戏，提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4）
电脑随机出拳比较胜负，显示用户胜、负还是平局。运行如下图所示：
提示：电脑随机出拳
使用随机数，首先需要导入随机数的模块 —— “工具包”
import random
导入模块后，可以直接在 模块名称 后面敲一个"."然后按 Tab键，会提示该模块中包含的所有函数
random.randint(a, b)，返回[a, b]之间的整数，包含a和b
random.randint(1, 10)  # 生成的随机数n: 1 <= n <= 10   
random.randint(4, 4)  # 结果永远是 4 
random.randint(25, 12)  # 该语句是错误的，下限必须小于上限
"""

import random
print("***********石头剪刀布游戏开始***********")
list_q = ["石头", "剪刀", "布", "退出"]
print("请按下面提示出拳：")
for index in range(len(list_q)):
    print("石头【1】\t剪刀【2】\t布【3】\t退出【4】")
    user = input("请输入你的选项：")
    if user not in ["1","2","3","4"]:
        print("输入参数不合法,游戏结束！")
        break
    elif int(user) == 4:
        print("游戏结束！")
        break
    else:
        computer = random.randint(1, 3)
        aa = computer - int(user)
        if aa==0:
            print("您的出拳为：{},电脑的出拳为：{},平局！".format(list_q[int(user)-1],list_q[computer-1]))
        elif aa in (1,-2):
            print("您的出拳为：{},电脑的出拳为：{},您赢了！".format(list_q[int(user)-1],list_q[computer-1]))
        else:
            print("您的出拳为：{},电脑的出拳为：{},您输了！".format(list_q[int(user)-1],list_q[computer-1]))
print("*********游戏结束*********")

"""
2、编写如下程序
a.用户输入1-7七个数字，分别代表周一到周日

b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”

c.如果输入0，退出循环

d.输入其他内容，提示：“输入有误，请重新输入！”

提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确。不用考虑浮点数等情况。
"""

dict2 = {"1":"周一","2":"周二","3":"周三","4":"周四","5":"周五"}
num2 = input("请输入1-7的整数：")
while num2 not in ["0","1","2","3","4","5","6","7"]:
    print("输入有误，请重新输入！")
    num2 = input("请输入1-7的整数：")
while num2 in ["0","1","2","3","4","5","6","7"]:
    if 1<= int(num2) <=5:
        print("{}".format(dict2[num2]))
        num2 = input("请输入1-7的整数：")
    elif int(num2) in [6,7]:
        print("周末")
        num2 = input("请输入1-7的整数：")
    elif int(num2) ==0:
        print("输入不合法，退出！")
        break





"""
3、冒泡排序（不要求提交，面试之前背熟）


使用循环实现排序算法（冒泡，选择等算法选择一个，请自行了解。）

提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法
"""
# 冒泡排序
a = [1,7,4,89,34,2]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] >a[j]:
            aa = a[j]
            a[j] = a[i]
            a[i] = aa
print(a)


