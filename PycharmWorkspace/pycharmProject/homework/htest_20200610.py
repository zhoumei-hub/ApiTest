"""     """

"""
利用unittest框架，完成课程案例未实现的测试用例 
1、掌握unittest编写用例的步骤
2、掌握unittest的断言表达

"""

import unittest
from py30.class_unittest.login import login_check


class TestLogin(unittest.TestCase):

    def test_login_ok(self):
        # 1、测试数据 # 2、测试步骤
        res = login_check("python27","lemonban")
        # 3、断言：预期结果与实际结果的比对
        self.assertEqual(res,{"code": 0, "msg": "登录成功"})


    def test_login_wrong_passwd(self):
        res1 = login_check("python27", "lemon")
        self.assertEqual(res1,{"code": 1, "msg": "账号或密码不正确"})


    def test_login_wrong_user(self):
        res2 = login_check("python30", "lemonban")
        self.assertEqual(res2, {"code": 1, "msg": "账号或密码不正确"})


    def test_login_no_passwd(self):
        res3 = login_check("python30", None)
        self.assertEqual(res3,{"code": 1, "msg": "所有的参数不能为空"})

    def test_login_no_user(self):
        res4 = login_check(None, "lemonban")
        self.assertEqual(res4,{"code": 1, "msg": "所有的参数不能为空"})
