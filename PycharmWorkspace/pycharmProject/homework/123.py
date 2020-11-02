import unittest
class TestReg(unittest.TestCase):

1、实例化测试套件TestSuite
s = unittest.TestSuite()

添加1个用例  addTest(类名("用例名")) 添加一个测试用例
s.addTest(TestLogin("test_login_ok"))

添加多个用例
s.addTests([TestLogin("test_login_ok"),TestLogin("test_login_wrong_user")])


runner = unittest.TextTestRunner()
runner.run(s)

from BeautifulReport import BeautifulReport
br = BeautifulReport(s)
br.report("py30期单元测试报告","bp_report.html")