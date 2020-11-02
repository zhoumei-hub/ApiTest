"""
======================
Author: 柠檬班-小简
Time: 2020/8/17 20:19
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
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

# xpath表达式
# driver.find_element_by_xpath('//div[@id="u1"]//a[@name="tj_login"]').click()
# css定位
# driver.find_element_by_css_selector('div#u1 a[name="tj_login"]').click()

# find_element方法
from selenium.webdriver.common.by import By

# 找到登陆按钮，并点击
loc = (By.XPATH,'//div[@id="u1"]//a[@name="tj_login"]')
# driver.find_element(By.XPATH,'//div[@id="u1"]//a[@name="tj_login"]')
driver.find_element(*loc).click()
# find_elements
# driver.find_elements()

# 在登陆的窗口当中，点击  用户名登陆
loc = (By.ID,'TANGRAM__PSP_11__footerULoginBtn')
driver.save_screenshot("登陆窗口.png")  # 截图
driver.find_element(*loc).click()



sleep(7)
# 关闭当前窗口。
driver.close()
# 关闭浏览器，关闭会话。
driver.quit()