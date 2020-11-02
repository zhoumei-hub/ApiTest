"""
======================
Author: 柠檬班-小简
Time: 2020/8/19 20:50
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""
"""
alert: js弹窗
Alert类

1、动作：导致alert的出现
3、切换：driver.switch_to.alert

更多的处理方案：http://testingpai.com/article/1596527701066
"""

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("file:///D:/Pychram-Workspace/py30-web/day05_元素操作/处理alert.html")

# 导致alert弹框 出现
driver.find_element("id","press").click()
sleep(1)

# 切换
al = driver.switch_to.alert

# 如果要获取文本
print(al.text)

# 关闭弹出框
al.accept()



sleep(10)
driver.quit()



