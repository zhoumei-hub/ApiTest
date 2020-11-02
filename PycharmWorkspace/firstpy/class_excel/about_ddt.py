"""
======================
Author: 柠檬班-小简
Time: 2020/6/15 20:21
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
from ddt import ddt,data
import unittest

@ddt
class TestABC(unittest.TestCase):

    # @data([[1,2],[3,4]])
    # def test_add(self,case):
    #     print("1111")
    #     print(case)

    my_dict = {"name":"xj","age":18}.items()
    @data(*my_dict)
    def test_add(self, case):
        print("222222")
        print(case)