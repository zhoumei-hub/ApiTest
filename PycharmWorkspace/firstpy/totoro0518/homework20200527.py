
"""
1、一家商场在降价促销，所有原价都是整数（不需要考虑浮点情况），如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，
如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格。
"""
# original_price = input("请输入购买商品的价格：")
#
# if  50 <= int(original_price) <= 100:
#     print("您享受的折扣是10%！")
#     pay = int(original_price) - int(original_price)*0.1
# elif int(original_price) > 100:
#     print("您享受的折扣是20%！")
#     pay = int(original_price) - int(original_price)*0.2
# else:
#     print("您没有任何折扣！")
#     pay = int(original_price)
# print("您需要支付的金额为{}元".format(pay))


"""
2 判断是否为闰年
提示:
输入一个有效的年份（如：2019），判断是否为闰年（不需要考虑非数字的情况）
如果是闰年，则打印“2019年是闰年”；否则打印“2019年不是闰年”
什么是闰年，请自行了解（需求文档没有解释）
"""
# r_year = input("请输入年份：")
# aa = int(r_year) % 4
# if aa == 0:
#     print("{}年是闰年".format(r_year))
# else:
#     print("{}年不是闰年".format(r_year))



"""
3.求三个整数中的最大值
提示：定义 3 个变量
"""
# num1 = input("请输入第一个整数：")
# num2 = input("请输入第二个整数：")
# num3 = input("请输入第三个整数：")
#
# if int(num1) >= int(num2):
#     aa = int(num1)
# else:
#     aa = int(num2)
# if aa >= int(num3):
#     max = aa
# else:
#     max = int(num3)
# print("{}，{}，{}中最大整数为{}".format(num1,num2,num3,max))


"""
4，  使用for打印九九乘法表

提示：

输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）

1 * 1 = 1	
1 * 2 = 2    2 * 2 = 4	
1 * 3 = 3    2 * 3 = 6      3 * 3 = 9	
1 * 4 = 4    2 * 4 = 8      3 * 4 = 12    4 * 4 = 16	
1 * 5 = 5    2 * 5 = 10    3 * 5 = 15    4 * 5 = 20    5 * 5 = 25	
1 * 6 = 6    2 * 6 = 12    3 * 6 = 18    4 * 6 = 24    5 * 6 = 30    6 * 6 = 36	
1 * 7 = 7    2 * 7 = 14    3 * 7 = 21    4 * 7 = 28    5 * 7 = 35    6 * 7 = 42    7 * 7 = 49	
1 * 8 = 8    2 * 8 = 16    3 * 8 = 24    4 * 8 = 32    5 * 8 = 40    6 * 8 = 48    7 * 8 = 56    8 * 8 = 64	
1 * 9 = 9    2 * 9 = 18    3 * 9 = 27    4 * 9 = 36    5 * 9 = 45    6 * 9 = 54    7 * 9 = 63    8 * 9 = 72    9 * 9 = 81
"""

for i in range(1,10):
    for j in range(1,i+1):
        value1 = i * j
        print("{} * {} = {}".format(j,i,value1),end="\t")
    print("")
"""  *************************扩展题*******************************  """

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

# import random
# print("***********石头剪刀布游戏开始***********")
# list_q = ["石头", "剪刀", "布", "退出"]
# print("请按下面提示出拳：")
# for index in range(1,len(list_q)):
#     print("********第{}回合*********".format(index))
#     print("石头【1】\t剪刀【2】\t布【3】\t退出【4】")
#     user = input("请输入你的选项：")
#     if user not in ["1","2","3","4"]:
#         print("输入参数不合法,游戏结束！")
#         break
#     elif int(user) == 4:
#         print("游戏结束！")
#         break
#     else:
#         computer = random.randint(1, 3)
#         aa = computer - int(user)
#         if aa==0:
#             print("您的出拳为：{},电脑的出拳为：{},平局！".format(list_q[int(user)-1],list_q[computer-1]))
#         elif aa in (1,-2):
#             print("您的出拳为：{},电脑的出拳为：{},您赢了！".format(list_q[int(user)-1],list_q[computer-1]))
#         else:
#             print("您的出拳为：{},电脑的出拳为：{},您输了！".format(list_q[int(user)-1],list_q[computer-1]))
#     print("*********游戏结束*********")

"""
2、编写如下程序
a.用户输入1-7七个数字，分别代表周一到周日

b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”

c.如果输入0，退出循环

d.输入其他内容，提示：“输入有误，请重新输入！”

提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确。不用考虑浮点数等情况。
"""

# dict2 = {"1":"周一","2":"周二","3":"周三","4":"周四","5":"周五"}
# print(dict2["1"])
# num2 = input("请输入1-7的整数：")
# try:
#     int(num2)
# except ValueError:
#     print("输入有误，请重新输入！")
# if 1<= int(num2) <=5:
#     print("{}".format(dict2[num2]))
# elif int(num2) in [6,7]:
#     print("周末")
# else:
#     print("输入不合法")







"""
3、冒泡排序（不要求提交，面试之前背熟）


使用循环实现排序算法（冒泡，选择等算法选择一个，请自行了解。）

提示：利用for循环，完成a=[1,7,4,89,34,2]的排序（小的数字排前面，大的排后面），不能使用sort、sorted等内置函数或方法
"""



