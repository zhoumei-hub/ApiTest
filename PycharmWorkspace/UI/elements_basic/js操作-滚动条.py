"""
======================
Author: 柠檬班-小简
Time: 2020/8/21 21:31
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""
"""
让元素滚动到可见区域后，再操作。
1、大部分的网页自己会滚

2、元素本身：ele.location_once_scrolled_into_view

3、js：element.scrollIntoView()
    js_code = 'arguments[0].scrollIntoView()'
    driver.execute_script(js_code,ele)


"""
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element("id","kw").send_keys("selenium",Keys.ENTER)

loc = (By.XPATH,'//a[text()="下一页 >"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
ele = driver.find_element(*loc)
# ele.location_once_scrolled_into_view
js_code = 'arguments[0].scrollIntoView()'
driver.execute_script(js_code,ele)

sleep(10)
driver.quit()
