"""
======================
Author: 柠檬班-小简
Time: 2020/6/10 21:38
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""



import unittest
from class_unittest.login import login_check
# import ddt

from ddt import ddt,data

datas = [
    {"user":"python27","passwd":"lemonban","check":{"code": 0, "msg": "登录成功"}},
    {"user":"python27","passwd":"lemonban11","check":{"code": 1, "msg": "账号或密码不正确"}},
    {"user":"python25","passwd":"lemonban","check":{"code": 1, "msg": "账号或密码不正确"}}
]

@ddt
class TestLogin(unittest.TestCase):

    @data(*datas)
    def test_login(self,case):
        # 1、测试数据 # 2、测试步骤
        res = login_check(case["user"],case["passwd"])
        # 3、断言：预期结果与实际结果的比对
        self.assertEqual(res,case["check"])


    def test_demo(self):
        pass


    # def test_loginV(self):
    #     for data in datas:
    #         res = login_check(data["user"], data["passwd"])
    #         # 3、断言：预期结果与实际结果的比对
    #         self.assertEqual(res, data["check"])




    @classmethod
    def setUpClass(cls):
        print("**** TestLogin类下的用例开始执行 *****")

    @classmethod
    def tearDownClass(cls) -> None:
        print("**** TestLogin类下的用例结束 *****")

    def setUp(self):
        print("===== 单个用例开始执行 ======")

    def tearDown(self):
        print("===== 单个用例结束执行 ======")



    # def test_login_1_wrong_passwd(self):
    #     # 1、测试数据 # 2、测试步骤
    #     res = login_check("python27", "lemonban11")
    #     # 3、断言：预期结果与实际结果的比对
    #     self.assertEqual(res, {"code": 1, "msg": "账号或密码不正确"})
    #
    # def test_login_2_wrong_user(self):
    #     # 1、测试数据 # 2、测试步骤
    #     res = login_check("python30", "lemonban")
    #     # 3、断言：预期结果与实际结果的比对
    #     self.assertEqual(res, {"code": 1, "msg": "账号或密码不正确"})
    #
    # def test_login_3_no_user(self):
    #     # 1、测试数据 # 2、测试步骤
    #     res = login_check(password="lemonban11")
    #     # 3、断言：预期结果与实际结果的比对
    #     self.assertEqual(res, {"code": 1, "msg": "所有的参数不能为空"})
    #
    # def test_login_4_no_passwd(self):
    #     # 1、测试数据 # 2、测试步骤
    #     res = login_check("python27")
    #     # 3、断言：预期结果与实际结果的比对
    #     self.assertEqual(res, {"code": 1, "msg": "所有的参数不能为空"})


