"""
======================
Author: 柠檬班-小简
Time: 2020/6/12 20:30
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""

import unittest
from class_unittest.test_1_login import TestLogin
from class_unittest.test_0_register import TestDemo

# 1、实例化测试套件TestSuite
# s = unittest.TestSuite()

# 添加1个用例  addTest(类名("用例名")) 添加一个测试用例
# s.addTest(TestLogin("test_login_ok"))

# 添加多个用例
# s.addTests([TestLogin("test_login_ok"),TestLogin("test_login_wrong_user")])

# 从start_directory这个目录下开始，搜索所有的测试用例，并加载到测试套件当中。
# 1、指定搜索目录
# 2、文件过滤规则：以文件名匹配。test*.py
# 3、在文件当中过滤用例：继承了unittest.TestCase类的测试类，类当中以test_开头的测试函数。

s = unittest.TestLoader().discover(r"D:\Pychram-Workspace\py30")
print(type(s))
print(s)

# 运行测试用例并生成结果
# runner = unittest.TextTestRunner()
# runner.run(s)

# 运行测试用例并生成html的结果
from HTMLTestRunnerNew import HTMLTestRunner
# 创建一个html文件，以写的模式打开，支持中文
with open("report.html","wb") as fs:
    # 运行测试用例，将结果写html当中
    runner = HTMLTestRunner(fs,title="py30期单元测试报告",tester="小简")
    runner.run(s)


# from BeautifulReport import BeautifulReport
# br = BeautifulReport(s)
# br.report("py30期单元测试报告","bp_report.html")