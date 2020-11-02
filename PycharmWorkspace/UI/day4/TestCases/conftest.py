"""
======================
Author: 柠檬班-小简
Time: 2020/8/24 21:31
Project: day1
Company: 湖南零檬信息技术有限公司
======================
"""
import pytest
from selenium import webdriver

from TestDatas import global_datas as gd

# 定义fixture - 前置后置 - 作用域 - 返回值
@pytest.fixture(scope="class")
def init():
    # 实例化driver,访问登陆页面
    driver = webdriver.Chrome()
    driver.get(gd.login_url)
    yield driver
    driver.quit()

@pytest.fixture
def back_login(init):
    init.get(gd.login_url)
    yield init

