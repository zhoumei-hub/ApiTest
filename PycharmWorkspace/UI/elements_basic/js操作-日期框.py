"""
======================
Author: 柠檬班-小简
Time: 2020/8/21 20:20
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""
"""
python执行js代码

driver.execute_script(js代码,传给js代码的参数)
"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.12306.cn/index/")

# js代码
# js_code = 'a = document.getElementById("train_date");' \
#           'a.removeAttribute("readonly");' \
#           'a.value = "2020-08-29";'
#
# driver.execute_script(js_code)

# 通过python代码找到元素对象
loc = (By.ID,"train_date")
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
ele = driver.find_element(*loc)
set_time = "2020-08-29"

js_code = 'arguments[0].removeAttribute("readonly");' \
          'arguments[0].value = arguments[1];'

# 如果要将外部的值，传给js代码。js的arguments变量用来接收外部参数。
driver.execute_script(js_code,ele,set_time)

sleep(10)
driver.quit()
