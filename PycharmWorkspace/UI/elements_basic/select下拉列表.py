"""
======================
Author: 柠檬班-小简
Time: 2020/8/19 21:59
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""
"""
Select类

select_by_value
select_by_index
select_by_visible_text

1、找到页面有Select的
2、找到Select元素
3、实例化Select类，将select元素对象传进去。
4、通过下标/value/文本选值
"""
from selenium.webdriver.support.select import Select
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("file:///D:/Pychram-Workspace/py30-web/day05_元素操作/处理alert.html")

# 找到select元素
ele = driver.find_element("id","hobby")

# 实例化Select类，将select元素对象传进去。
s = Select(ele)

# 通过下标/value/文本选值
s.select_by_value("看书")
sleep(3)
s.select_by_index(4)
sleep(3)
s.select_by_visible_text("看剧")

sleep(10)
driver.quit()