"""
======================
Author: 柠檬班-小简
Time: 2020/8/17 20:39
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""
"""
no such element: Unable to locate element:

1、在运行结果的页面当中，copy自己的元素定位，然后通过F12确认元素定位表达式是否有错。
2、等待不到位。
   可以截图，查看查找时页面的状态。
3、元素在iframe当中。 html当中，内嵌了另外一个html(iframe)
   3.1 分辨元素是否在iframe当中。
   3.2 在代码当中，从当前的html，切换到iframe当中的html，然后再找元素。
 
   
4、等待方式：
   sleep: 强制方式。-- 辅助。
   
   智能等待：超时时间：10
      1、隐性等待-implicity_wait: 
         3.1 每个会话只调用一次。
         3.2 找元素、命令执行完成。
         
      2、显性等待  等待(WebDriverWait类) + 条件(expected_condition)
        WebDriverWait(driver,超时时间,查看周期=0.5).until(条件)
        WebDriverWait(driver,超时时间,查看周期=0.5).not_until(条件)
        
        条件：
        presence_of_element_located ：元素存在
        visibility_of_element_located：元素可见
        element_to_be_clickable: 元素可点击


"""
"""
======================
Author: 柠檬班-小简
Time: 2020/8/17 20:19
Project: py30-web
Company: 湖南零檬信息技术有限公司
======================
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window() # 开启会话
driver.get("http://www.baidu.com")

# 隐性等待
driver.implicitly_wait(10) # 10

# 找到登陆按钮，并点击，弹出登陆窗口
loc = (By.XPATH,'//div[@id="u1"]//a[@name="tj_login"]')
driver.find_element(*loc).click()

sleep(2)
# 显性等待
wait = WebDriverWait(driver,20)
# 元素表达
loc = (By.ID,'TANGRAM__PSP_11__footerULoginBtn')
# 等待 - 等待元素可见。
wait.until(EC.visibility_of_element_located(loc))
# 在登陆的窗口当中，点击  用户名登陆
driver.save_screenshot("登陆窗口.png")  # 截图
driver.find_element(*loc).click()

# 等待用户名输入框可见，然后输入用户名
loc = (By.ID,"TANGRAM__PSP_11__userName")
ele = wait.until(EC.visibility_of_element_located(loc))
print("等待元素可见的返回对象是：",ele)
driver.find_element(*loc).send_keys("123456789")





sleep(7)
# 关闭当前窗口。
driver.close()
# 关闭浏览器，关闭会话。
driver.quit()