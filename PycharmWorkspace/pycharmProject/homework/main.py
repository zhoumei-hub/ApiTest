import unittest


# 收集测试用例
s = unittest.TestLoader().discover(r"D:\pycharmProject\homework")

from BeautifulReport import BeautifulReport
br = BeautifulReport(s)
br.report("注册","beauty_report.html")

