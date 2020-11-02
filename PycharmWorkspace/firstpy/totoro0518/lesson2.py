"""
======================
Author: 柠檬班-totoro
Time: 2020/5/20 20:09
Project: firstpy
Company: 湖南零檬信息技术有限公司
======================
"""

# + - * / %
num1 = 10
num2 = 52
res1 = num1 + num2
print(res1)

sum = 50
#  累加 sum = sum + 120
sum +=120
print(sum)

#累减 sum = sum -100
sum -=100
print("最终支付：",sum)

money = 200
left_money = money - sum
print(left_money)
print(left_money == money)


print("****************逻辑运算***********************")
# input() 接受用户的输入  字符串的数据类型
#age = input("请输入你的年龄:")
#height = input("请输入你的身高:")
#salary = input("请输入你的工资:")
# 字符串的数字，转换成int类型。int(数字形式的字符串)
#res11 = (int(age) > 18) and (int(height) > 180)
#res22 = (int(age) > 18) or (int(salary) > 10000)
#print(res11)
#print(res22)
#print(not res22)

s = ""  # 空字符串
s1 = None # 不代表任何一个数据类型
print(s)
print(s1)
print(type(s1))

# 转义字符：\ 作为常规的数据内容，不作为Python的特殊处理
person_info = '我是totoro,喜欢\'python\'我们一起来学习'
print(person_info)