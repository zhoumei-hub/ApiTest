"""
======================
Author: 柠檬班-totoro
Time: 2020/5/29 20:45
Project: firstpy
Company: 湖南零檬信息技术有限公司
======================
"""

def mine():
    print("我中了500万！")

mine()


def mine_a(num,password,count):
    """
    函数功能说明
    :param num:
    :param password:
    :param count:
    :return:
    """
    print("我的卡号{}密码{}取现{}元！".format(num,password,count))

mine_a("123","123456","500")