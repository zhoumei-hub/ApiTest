"""
======================
Author: 柠檬班-小简
Time: 2020/8/26 21:26
Project: day1
Company: 湖南零檬信息技术有限公司
======================
"""
from selenium.webdriver.common.by import By

class HomePageLocs:
    # 退出按钮
    exit_loc = (By.XPATH, '//a[text()="退出"]')