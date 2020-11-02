"""
======================
Author: 柠檬班-小简
Time: 2020/5/20 20:14
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""

num1 = 10
num2 = 52

res = num1 + num2
print(res)

res2 = num1 - num2
print(res2)

res3 = num1 * num2
print(res3)

res4 = num1 / num2
print(res4)

print(100/5)

# ZeroDivisionError
# print(100/0)

res5 = num1 % num2
print(res5)


res6 = (num1 * num2) + (num1 * num2)
print(res6)

print("**************************************************")

# 赋值运算：值赋给变量

# 巧克力  120   小龙虾  80     红酒   200
# 收银台结账  sum = 0
sum = 0
# 巧克力  120
# sum = sum +120
sum += 120
print(sum)
# 小龙虾  80
sum += 80
# 红酒   200
sum += 200
print(sum)

# 在原来的基础上，减掉200
# sum = sum - 200
sum -= 200
print("我最终为520支付的人民币为：")
print(sum)

# money = 800
# left_money = money - sum
# get_money = 520

print("************************     比较运算符     *****************************")
my_money = 2000
you_money = 520

# 是否相等
print(my_money == you_money)
# 不相等
print(my_money != you_money)
# 大于
print(my_money > you_money)
# 大于等于
print(my_money >= you_money)
# 小于
print(my_money < you_money)
# 小于等于
print(my_money <= you_money)


print("************************     逻辑运算符     *****************************")
# input() 接收用户的输入  字符串的数据类型
age = input("请输入相亲候选人的年龄：")
height = input("请输你相亲候选人的身高：")
salary = input("请输入相亲候选人的收入：")

# age = "30"
# 字符串的数字，转换成int类型. int(数字形式的字符串)

# 第一个人的要求
# res = (int(age) > 20) and (int(height) > 175) and (int(salary) > 10000)
# print(res)

# 第二个人的要求
# res1 = (int(age) > 20 or int(height) > 175) and (int(salary) > 10000)
# print(res1)

# 非运算 - 取反 - 唱反调
res2 = not (int(age) > 20)
print(res2)
