"""
======================
Author: 柠檬班-小简
Time: 2020/5/22 19:43
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""


"""
字符串：取值、切片、find\count、转义
1、str1 = 'python cainiao 666'
2、卖橘子的计算器：写一段代码，提示用户输入橘子的价格，和重量，最后计算出应该支付的金额！（不需要校验数据，都传入数字就可以了。）
3、my_hobby = "Never stop learning!"
"""

str1 = 'python cainiao 666'
print(str1[4])
str2 = str1

# 先获取长度，再除以2
index = len(str1) // 2
print(index)
index = int(index) - 1

print(str1[index])

my_hobby = "Never stop learning!"

print(my_hobby[-2:])
print(my_hobby[-1:-3:-1])