"""
======================
Author: 柠檬班-小简
Time: 2020/6/12 20:44
Project: py30
Company: 湖南零檬信息技术有限公司
======================
"""
"""
表达用例  -        收集用例    -                               执行用例  -    生成报告
setup            TestSuite                                     TextTestRunner 不用
teardown         TestLoader().discover(搜索路径)                 HtmlTestRunner - 实例化后调用run方法，html报告
setupClass       用例搜索原则：目录-文件(test*.py)-测试用例          BeautifulReport - 实例化对象后，report方法
teardownClass

执行用例的顺序：ASCII  

ddt: 一个测试流程，N组测试数据。

1、列表 = 准备好N组测试数据

2、
import ddt
类名上：@ddt.ddt
测试流程函数上：@ddt.data(*列表)
测试流程函数：用一个变量接收每一组测试数据


定义测试类 ，继承unittest.TestCase
在测试类当中，以test_开头，定义测试函数。
每一个test_开头的函数，就是一个测试用例。
编写用例：
    1、测试数据
    2、测试步骤 
    3、断言：预期结果与实际结果的比对
       AssertionError: 断言失败 - 用例失败
       assert 表达式(True表示通过，False表示失败)
       self.assertXXXXX()

    4、前置后置(fixture) - 前置条件、后置工作
       微信聊天功能 - 前置条件：登陆/有个好友

自动化用例：1、前置后置  2、步骤   3、断言

AssertionError: 断言失败。是unitest框架，识别用例失败的标识之一。



1、setup,teardown - 类下面的每一个用例在执行之前，会执行setup,
                           在每一个用例执行之后，会执行teardown
  setup  测试用例   teardown

2、setupClass,teardownClass  - 类里面的第一个用例执行之前，执行setupClass
                               类里面的最 隍一个用例执行之后，执行teardownClass
   setupClass  测试类   teardownClass


收集用例：
  TestSuite -  addTest addTests
  TestLoader - discover(搜索目录)  test*.py  


执行用例+测试报告
HtmlTestRunner - 先实例化，再运行用例，生成html报告
BeautifulReport - 先实例化，再运行用例，生成html报告
   pip install BeautifulReport


用例执行顺序：ASCII码顺序  从小到大
0~9<A~Z<a~z

如果你想自己指定执行顺序，在文件名或者用例名称上做文章
调整优秀级

测试思维：ddt   data driven test
        一个测试流程  N组测试用例   流程不变，只是测试数据和断言的数据不一样。


参数化

模块名：ddt,一定要跟测试框架一起用。
pip install ddt
  将多组测试数据，依次传递给一个测试流程
  
0、引入ddt  
import ddt

1、在测试类名的上面，用@ddt.ddt

2、在测试函数上面，用@ddt.data(*列表)
   在测试函数的参数中，定义一个参数用来接收每一组测试数据。
"""