"""
======================
Author: 柠檬班-小简
Time: 2020/7/1 20:06
Project: py30-接口自动化
Company: 湖南零檬信息技术有限公司
======================
"""
import unittest
import os

from Common.handle_requests import send_requests
from Common.handle_excel import HandleExcel
from Common.myddt import ddt,data
from Common.handle_path import datas_dir
from Common.my_logger import logger
from Common.handle_db import HandleDB


he = HandleExcel(datas_dir+"\\api_cases.xlsx","注册")
cases = he.read_all_datas()
he.close_file()

db = HandleDB()

@ddt
class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        logger.info("======  注册模块用例 开始执行  ========")

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("======  注册模块用例 执行结束  ========")


    @data(*cases)
    def test_register_ok(self,case):
        # print("本条测试数据：",case)
        logger.info("*********   执行用例{}：{}   *********".format(case["id"],case["title"]))
        expected = eval(case["expected"])
        # 步骤 测试数据 - 发起请求
        response = send_requests(case["method"],case["url"],case["request_data"])
        # 断言 - code == 0 msg == ok
        logger.info("用例的期望结果为：{}".format(case["expected"]))
        try:
            # self.assertEqual(response.json()["code"],expected["code"])
            # self.assertEqual(response.json()["msg"], expected["msg"])
            # 如果check_sql有值，说明要做数据库校验。
            if case["check_sql"]:
                # logger.info()
                result = db.select_one_data(case["check_sql"])
                self.assertIsNotNone(result)
        except AssertionError:
            logger.exception("断言失败！")
            raise
