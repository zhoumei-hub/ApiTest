"""
======================
Author: 柠檬班-小简
Time: 2020/8/21 20:13
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""
"""
Keys类

"""
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element("id","kw").send_keys("selenium",Keys.ENTER)
# driver.find_element("id","kw").send_keys(Keys.CONTROL,"c")

sleep(7)
driver.quit()