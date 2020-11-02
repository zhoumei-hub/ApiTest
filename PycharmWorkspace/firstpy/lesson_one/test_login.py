"""
======================
Author: 柠檬班-小简
Time: 2020/6/10 21:38
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
import unittest
from ddt import ddt,data
import os

from class_excel_logger.handle_excel import HandleExcel
from class_unittest.login import login_check
from class_excel_logger.my_logger import logger

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "login_cases.xlsx")
exc = HandleExcel(file_path, "login")
cases = exc.read_all_datas()
exc.close_file()


@ddt
class TestLogin(unittest.TestCase):


    @data(*cases)
    def test_login(self,case):
        logger.info("***********  开始执行测试用例 **************")
        logger.info("测试数据为：{}".format(case))
        # 1、测试数据 # 2、测试步骤
        res = login_check(case["user"],case["passwd"])
        logger.info("实际运行结果为：{}".format(res))
        # 3、断言：预期结果与实际结果的比对
        try:
            self.assertEqual(res,eval(case["check"]))
        except AssertionError:
            logger.exception("断言失败，用例不通过！")
            raise
        else:
            logger.info("断言成功，用例通过！")
        logger.info("***********  测试用例执行结束 **************")



