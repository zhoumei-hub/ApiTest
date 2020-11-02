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

from BeautifulReport import BeautifulReport
br = BeautifulReport(s)
br.report("py30期单元测试报告","bp_report.html")