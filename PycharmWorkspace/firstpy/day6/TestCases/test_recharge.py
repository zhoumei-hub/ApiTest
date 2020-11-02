"""
======================
Author: 柠檬班-小简
Time: 2020/7/6 21:13
Project: day6
Company: 湖南零檬信息技术有限公司
======================
"""
"""
充值接口：
   所有用例的前置：登陆！
                拿到2个数据：id，token
   把前置的数据，传递给到测试用例。
   
   充值接口的请求数据：id
             请求头：token

"""

import unittest
from jsonpath import jsonpath

from Common.handle_phone import get_old_phone
from Common.handle_requests import send_requests


class TestRecharge(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 得到登陆的用户名和密码
        user,passwd = get_old_phone()
        # 登陆接口调用。
        resp = send_requests("POST","member/login",{"mobile_phone":user,"pwd":passwd})
        # 得到的id,token设置为类属性
        # print("登陆的响应结果为：")
        # print(resp.text)
        cls.user_id = jsonpath(resp.json(),"$..id")[0]
        cls.token = jsonpath(resp.json(),"$..token")[0]

        # cls.id = "10000"
        # cls.token = "111111"

    def test_recharge(self):
        print(self.user_id)
        print(self.token)
        pass