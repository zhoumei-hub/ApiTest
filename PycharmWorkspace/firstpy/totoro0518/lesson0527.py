"""
======================
Author: 柠檬班-totoro
Time: 2020/5/27 20:18
Project: firstpy
Company: 湖南零檬信息技术有限公司
======================
"""

# 打印hello Python 100遍

# i = 0
# while i < 100:
#     i += 1 # i=i+1
#     print(i)
#     print("hello python")
#     if i==50:
#         print("已经50次了")
#         break

list_p = ["wee","qwqq","vv"]

for item in list_p:
    print(item)

for index in range(len(list_p)):
    print(index)
    print(list_p[index])



person_info = {
    "name" : "小雨点",
    "sex" : "女",
    "age" : "1"
}

for key in person_info.keys():
    print(key)
    print(person_info[key])


# 遍历键值对
print(person_info.items())
for key,value in person_info.items():
    print(key,value)

# 双层for循环
