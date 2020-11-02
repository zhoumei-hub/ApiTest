"""
======================
Author: 柠檬班-小简
Time: 2020/6/12 20:30
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""

import unittest
import os


cases_dir = os.path.dirname(os.path.abspath(__file__))
s = unittest.TestLoader().discover(cases_dir)

# 运行测试用例并生成html的结果
from HTMLTestRunnerNew import HTMLTestRunner
# 创建一个html文件，以写的模式打开，支持中文
with open("report.html","wb") as fs:
    # 运行测试用例，将结果写html当中
    runner = HTMLTestRunner(fs,title="py30期单元测试报告",tester="小简")
    runner.run(s)
