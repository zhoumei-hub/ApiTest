""" 20200612 homework"""

"""
函数入参：
注意：参数传字符串类型，不需要考虑其他类型。
参数1：账号  
参数2：密码1
参数2：密码2 


函数内部处理的逻辑：
   判断是否有参数为空，
    判断账号密码是否在6-18位之间，
    判断账号是否被注册过，
    判断两个密码是否一致。
    上面添加都校验通过才能注册成功，其他情况都注册失败，
各种情况的返回结果如下：  
   注册成功               返回结果：{"code": 1, "msg": "注册成功"}
   有参数为空，            返回结果 {"code": 0, "msg": "所有参数不能为空"}   
   两次密码不一致          返回结果：{"code": 0, "msg": "两次密码不一致"}
   账户已存在             返回结果：{"code": 0, "msg": "该账户已存在"}
   密码不在6-18位之间      返回结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}              
   账号不在6-18位之间      返回结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}

         
"""
import unittest
from my_unittest.register import register
from ddt import ddt,data
from my_unittest.my_logger import mlogger

import os
from my_unittest.handle_excel import HandleExcel
# datas = [
#     {"user":"python27","passwd1":"123456","passwd2":"123456","check":{"code": 1, "msg": "注册成功"}},
#     {"user":"python28","passwd1":"123456","passwd2":"","check":{"code": 0, "msg": "所有参数不能为空"}},
#     {"user": "python28", "passwd1": "", "passwd2": "123456", "check": {"code": 0, "msg": "所有参数不能为空"}},
#     {"user": "", "passwd1": "123456", "passwd2": "123456", "check": {"code": 0, "msg": "所有参数不能为空"}},
#     {"user":"python28","passwd1":"123456","passwd2":"654321","check":{"code": 0, "msg": "两次密码不一致"}},
#     {"user": "python26", "passwd1": "111111", "passwd2": "111111", "check": {"code": 0, "msg": "该账户已存在"}},
#     {"user": "python1234567890123", "passwd1": "123456", "passwd2": "123456", "check": {"code": 0, "msg": "账号和密码必须在6-18位之间"}},
#     {"user": "python28", "passwd1": "python1234567890123", "passwd2": "python1234567890123", "check":{"code": 0, "msg": "账号和密码必须在6-18位之间"}},
#
# ]

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"register_cases.xlsx")
exc = HandleExcel(file_path,"register")
cases = exc.read_all_datas()  #从excel读取到数据，存入列表
exc.close_file()  #关闭excel
#处理列表中的数据
for i in range(len(cases)):
    cases[i]["check"] = eval(cases[i]["check"])
    if cases[i]["passwd1"] != None:
        cases[i]["passwd1"] = str(cases[i]["passwd1"])
    if cases[i]["passwd2"] != None:
        cases[i]["passwd2"] = str(cases[i]["passwd2"])

@ddt
class TestReg(unittest.TestCase):

    @data(*cases)
    def test_reg(self,case):
        mlogger.info("***********  开始执行测试用例 **************")
        mlogger.info("测试数据为：{}".format(case))
        # 1、测试数据 # 2、测试步骤
        res = register(case["user"],case["passwd1"],case["passwd2"])
        mlogger.info("实际运行结果为：{}".format(res))
        # 3、断言：预期结果与实际结果的比对
        try:
            self.assertEqual(res, case["check"])
        except AssertionError:
            mlogger.exception("断言失败，用例不通过！")
            raise
        else:
            mlogger.info("断言成功，用例通过！")
        mlogger.info("***********  测试用例执行结束 **************")




