"""
======================
Author: 柠檬班-小简
Time: 2020/8/19 20:10
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""
"""
1、动作：导致新窗口的出现
2、获取：所有窗口的句柄。driver.window_handles
3、切换：driver.switch_to.window(新窗口句柄)

获取当前窗口的句柄：driver.current_window_handle
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element(By.ID,"kw").send_keys("selenium")
driver.find_element(By.ID,"su").click()

# 点击搜索结果当中的 selenium官网。 结果：打开一个新窗口。
loc = (By.XPATH,"//a[text()=\" automates browsers. That's it!\"]")
wait = WebDriverWait(driver,20)
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

# 切换到新的窗口，然后在新窗口当中，点击
# 获取
sleep(1)
win_hans = driver.window_handles  # 列表。按照窗口出现的先后顺序添加
print("打开的窗口句柄们: ",win_hans)
print("当前正在使用的窗口句柄：",driver.current_window_handle)

# 切换到新窗口。进入了新的html
driver.switch_to.window(win_hans[-1])

# 新的页面里，等待元素可见，查找元素，操作元素
loc = (By.XPATH,'//h3[text()="Selenium IDE"]/following-sibling::div//a')
wait.until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()


sleep(10)
driver.quit()
