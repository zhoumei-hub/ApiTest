"""
======================
Author: 柠檬班-小简
Time: 2020/8/17 21:49
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""

"""
3、元素在iframe当中。 html当中，内嵌了另外一个html(iframe)
   3.1 分辨元素是否在iframe当中。
   3.2 在代码当中，从当前的html，切换到iframe当中的html，然后再找元素。
      切换的方式：driver.switch_to.frame(iframe的标识)
      iframe的识别 ：index, name属性, or webelement

"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window() # 开启会话
driver.get("http://www.baidu.com")



# 切换到iframe当中的html
driver.switch_to.frame("login_frame_qq") # name属性
driver.switch_to.frame(3) # 下标
driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@name="login_frame_qq"]'))
sleep(1)


# 在新的html当中，查找元素，操作元素
