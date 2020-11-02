"""
======================
Author: 柠檬班-小简
Time: 2020/6/15 19:28
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""

"""
unittest框架：
1、4个核心概念？ --- 
   用例编写TestCase --- (断言self.assertXXXXXX，fixture前置后置 - setup/teardown，setupClass/teardownClass)
   用例套件TestSuite - 容器，放用例。addTest,addTests
   用例收集TestLoader - 收集用例 - discover(搜索目录)，返回TestSuite对象
   生成报告TextTestRunner
   
   AsssertionError: 断言失败，用例失败！！
   
   美化报告：
       HtmlTestRunner
       BeautifulReport
   



openpyxl : 
  load_workbook
  sheet
  cell(row=,cloumn=).value

sh.rows: 
sh.columns: 所有列的对象


"""