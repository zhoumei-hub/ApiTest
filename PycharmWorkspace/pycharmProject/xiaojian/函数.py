"""
======================
Author: 柠檬班-小简
Time: 2020/6/1 19:46
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""

"""
def 函数名称(参数):
    函数实现
    return  # 如果需要返回内容，就用return
            # 分支/循环 。在某一个分支退出函数，那就return.
            # 没有return，返回就是None 
"""
"""
局部变量：函数内部定义的变量
全局变量：函数外部定义的变量
"""
# sum_global = 0

# 求和。传进来的参数的和。
# def add(*args):
#     global sum_global
#     sum_num = 0  # 局部变量。只有函数内部可用
#     for item in args:
#         sum_num += item
#         sum_global += 1  # 全局变量在函数内部可以使用。但不可以修改。需要用global申明为全局变量
#     return sum_num

# sum_global += add(1,3,4,5,6)
# sum_global += add(100,200,300,400)

# print(sum_global)
# add(100,200,300,400)
# print(sum_global)

num_list = [100,200,300,400]

def add(a,b,c,d):
    sum_num = a +b +c+d
    print(sum_num)
    # return sum_num

add(*num_list)  # 调用函数时，传参的时候，利用*变量名拆包

def print_info(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key,value)

# person_info = {"name":"xx","age":20,"city":"北京"}
# print_info(**person_info)

# nums = [100,133,144,61]
# print(max(nums))
# print(min(nums))
# print(sum(nums))