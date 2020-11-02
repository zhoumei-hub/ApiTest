"""
======================
Author: 柠檬班-totoro
Time: 2020/6/7 23:52
Project: firstpy
======================
"""
"""
1、类属性怎么定义？ 实例属性怎么定义？
"""
# 类属性：直接在类当中定义，不在任何实例方法中
# 实例属性：定义在__init__函数中，在实例化时需要传入，创建对象的同时，自动调用。


"""
2、实例方法中的self代表什么？（简答）
"""
# self代表实例对象本身


"""
3、类中__init__方法在什么时候会调用的？（简答）
"""
# __init__方法在创建对象的同时调用


"""
4、定义一个登录的测试用例类Case
属性：用例名称
用例步骤
预期结果
实际结果
方法：运行用例、用例结果(比对预期结果和实际结果是否相等)
实例化2个测试用例 ，并运行用例 ，呈现用例结果
"""
class Case:
    def __init__(self,name,step,expect,actual):
        self.test_name = name
        self.test_step = step
        self.expect_result = expect
        self.actual_result = actual
    def test_result(self):
        print("运行用例：{}".format(self.test_name))
        print("执行步骤：{}".format(self.test_step))
        if self.actual_result == self.expect_result:
            print("预期结果为：{}\n实际结果为：{}\n用例执行通过！".format(self.expect_result,self.actual_result))
        else:
            print("预期结果为：{}\n实际结果为：{}\n用例执行不通过！".format(self.expect_result, self.actual_result))


testcase1 = Case("TEST01","登录www.baidu.com","登录成功","登录成功")
testcase1.test_result()

testcase2 = Case("TEST02","登录www.baidu.com","登录成功","登录失败")
testcase2.test_result()




"""
5、封装一个学生类Student，(自行分辨定义为类属性还是实例属性，方法定义为实例方法)
-  属性：身份(学生)，姓名，年龄，性别，英语成绩，数学成绩，语文成绩，
-  方法一：计算总分，方法二：计算三科平均分，方法三：打印学生的个人信息：我的名字叫XXX，年龄：xxx, 性别：xxx。
实例化1个学生, 并打印学生个人信息，计算总分。
"""
class Student:
    identify = "学生"
    def __init__(self,name,age,sex,english,math,chinese):
        self.name = name
        self.age = age
        self.sex = sex
        self.english = english
        self.math = math
        self.chinese = chinese
    def total_score(self):
        t_score = self.english + self.math +self.chinese
        return t_score

    def average_score(self):
        a_score = self.total_score()/3
        print("平均分：{}".format(a_score))

    def student_info(self):
        print("我的名字是：{}，年龄：{}，性别：{}".format(self.name,self.age,self.sex))

student_a = Student("A",18,"女",95,90,98.5)
student_a.student_info()
print("总分：",student_a.total_score())
student_a.average_score()