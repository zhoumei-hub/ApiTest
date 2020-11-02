"""
======================
Author: 柠檬班-小简
Time: 2020/8/19 21:20
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""
"""
select+option -- Select类

"""

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

sleep(2)
loc = (By.XPATH,'//*[@id="s-usersetting-top"]')

# 1、先找到鼠标要操作的元素对象
ele = driver.find_element(*loc)
# 2、ActionChains实例化
ta = ActionChains(driver)
# 3、调用鼠标操作
ta.move_to_element(ele).click(ele)
# 4、调用perfrom()执行鼠标操作
ta.perform()

# 等待下拉列表的元素可见，操作
loc = (By.XPATH,'//a[text()="高级搜索"]')
wait = WebDriverWait(driver,20)
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

#点击元素，结果：出现下拉列表
loc = (By.XPATH,'//span[@id="adv-setting-ft"]//div[contains(@class,"adv-ft-select")]')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 等待下拉当中要操作的元素可见，然后再操作
loc = (By.XPATH,'//p[@data-value="xls"]')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

sleep(10)
driver.quit()


