"""
======================
Author: 柠檬班-小简
Time: 2020/5/29 19:38
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
# print()
# input()

# 函数的定义！！
# 基本语法
def get_money():   #冒号之后，是功能的实现代码。
    print("取了500万！！")
    print("我笑醒了！")
    print("不用上班了！")


# 调用 函数名称()
# get_money()  # 不知道如何实现的，但是我只是使用了它。


# ()准备几个坑，相当于告诉调用者，必须把坑填满，否则功能使用不了。
# 定义时，()放的形参，并不是具体的数据。形参用变量表达。形参用来接收 - 调用者实际传进来的数据。
# 形参个数由什么来决定？ 需求。功能实现需要几个用户数据。
def get_money_V2(cardNum,passwd,count):
    """
    函数功能说明
    :param cardNum: 卡号
    :param passwd: 密码
    :param count: 取款金额
    :return:
    """
    # 卡号必须大于10位。
    if len(cardNum) < 10:
        print("卡号错了，再见！")
    # 密码必须为6位。否则不玩了。
    if len(passwd) != 6:
        print("密码长度出错，再见！")
    # 金额必须为100的整数倍。不然提示你金额出错。
    if int(count) % 100 != 0:
        print("金额不为100的整数倍！")
    # pass   # 我还没有想好写什么代码。不写呢，又要报错。使用pass占位。

# 调用
# 1、所有参数必须得传
# 2、位置传参。对应的位置传对应的值。
# 调用的时候，传的是具体的数据。叫做实参。
# get_money_V2("12345678900","4567","500")
# get_money_V2("12345678900",4567,"500")
# print() # ctrl+B 看源码。

# 默认参数：如果你没有传对应的实参。我就默认我在定义时提供的值。
# 定义时，形参=值
# 默认参数在最后。
# 不限定个数。
def get_money_V3(cardNum,passwd="123456",count=1000):
    # 卡号必须大于10位。
    if len(cardNum) < 10:
        print("卡号错了，再见！")
    # 密码必须为6位。否则不玩了。
    if len(passwd) != 6:
        print("密码长度出错，再见！")
    # 金额必须为100的整数倍。不然提示你金额出错。
    if int(count) % 100 != 0:
        print("金额不为100的整数倍！")
    else:
        print(count)

# get_money_V3("123456789",)  # 使用默认值。
# get_money_V3("12345678900","123000")  # 部分使用默认值。
# # 调用时，关键字参数. 传参时，形参=实参。
# get_money_V3("12345678900",count=2000)


def get_money_V4(cardNum,*args,**kwargs):
    # args是元组。()
    # kwargs是字典。{key:value}
    # 卡号必须大于10位。
    if len(cardNum) < 10:
        print("卡号错了，再见！")
    print(args)
    print(kwargs)
    for item in args:
        print(item)

# get_money_V4("12345678900")
# get_money_V4("12345678900",True,"123456",100)
# res = get_money_V4("12345678900",True,"123456",name="小简",city="长沙")
# get_money_V4("12345678900",True,"123456",name="小简",city="长沙")

# 位置参数(必传No1)，默认参数(可传可不传)、不定长参数(支持传多个)
# 顺序(参考print)：不定长参数   默认参数(可传可不传)
# *args,**kwargs

# 返回值。 礼尚往来。
# s = print(res)
# print(s)

def get_money_V5(cardNum,passwd="123456",count=1000):
    # 卡号必须大于10位。
    if len(cardNum) < 10:
        print("卡号错了，再见！")
        return cardNum  # 遇到return就退出函数调用。
    # 密码必须为6位。否则不玩了。
    if len(passwd) != 6:
        print("密码长度出错，再见！")
        return
    # 金额必须为100的整数倍。不然提示你金额出错。
    if int(count) % 100 != 0:
        print("金额不为100的整数倍！")
    else:
        # 三个条件 都满足了，我就给你吐钱！
        print("条件满足，准备吐钱。。。")
        return cardNum,count


# 接收返回值  变量 = 函数调用
# carn,money = get_money_V5("123456789000",count=2000)  # 调用
# print(carn,money)
# res = get_money_V5("123456789000")
# print(res)

# tuple_my = "hello",True
# print(tuple_my)

res = get_money_V5("12345678") # 不满足其中一个分支。执行过程中当遇到了return，退出了函数调用。
print(res)

# 函数
# 函数是干嘛的吗？？？ 功能实现！
# 函数先定义再调用。
# 定义：def 函数名称():
#            实现功能

# 参数：与用户交互。用户输入。
# 在实现功能的时候，需要与外部交互。需要外部提供一定的数据，以实现功能。
# 由需求来决定，有没有参数，有几个参数。

# 参数的类型：位置参数、默认参数、不定长参数(*args,**kwargs)
# 调用的时候：必传位置参数，默认参数可传可不传，也可以用关键字传参(形参=实参)、不定长参数可以传多个。

# 函数在使用之后，给用户的输出。有输入有输出。有反馈。
# 返回值。return关键字实现。
# 1、函数无return，默认调用后的返回值为None
# 2、return 值   值可以是任意类型数据。
# 3、return后可以不跟值。表示返回为None
# 4、调用函数时，遇到return，则结束函数调用。
# 调用的时候，接收功能的输出：变量 = 函数调用
