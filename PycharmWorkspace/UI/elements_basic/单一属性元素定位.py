"""
======================
Author: 柠檬班-小简
Time: 2020/8/14 20:07
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""

"""
find_element_by_XXX : 返回的是一个元素。匹配到的第一个。WebElement对象
find_elements_by_XXX : 返回页面当中，匹配表达式的所有元素。结果是一个列表。列表的成员是WebElement对象


"""

from time import sleep

# 引入第三方库
from selenium import webdriver
# 打开浏览器 - 指令1 - 开启与浏览器之间的会话。
driver = webdriver.Chrome()
# 最大化窗口
driver.maximize_window()
# 访问百度首页 - 指令2
driver.get("http://www.baidu.com")

# 合并写法
driver.find_element_by_id("kw").send_keys("selenium webdriver")

# class
ele = driver.find_element_by_class_name("s_ipt") # 只支持一个class值
eles = driver.find_elements_by_class_name("s_ipt")

# tag_name
driver.find_element_by_tag_name("input")
driver.find_elements_by_tag_name("input")

# name
driver.find_element_by_name("wd")
driver.find_elements_by_name("wd")

# link_text  partial_link_text
driver.find_element_by_link_text("hao123")
driver.find_elements_by_link_text("hao123")

driver.find_element_by_partial_link_text("123")
driver.find_elements_by_partial_link_text("123")

sleep(7)
# 关闭当前窗口。
driver.close()
# 关闭浏览器，关闭会话。
driver.quit()

