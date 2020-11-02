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

from TestDatas import global_datas as g_data
from PageObjects.login_page import LoginPage
from Common.my_logger import logger

# 定义fixture - 前置后置 - 作用域 - 返回值
@pytest.fixture(scope="class")
def init():
    # 实例化driver,访问登陆页面
    logger.info("========== class级 前置操作:打开谷歌浏览器,访问系统登陆页面 ===============")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(g_data.login_url)
    yield driver
    logger.info("========== class级 后置操作:关闭谷歌浏览器,退出会话 ===============")
    driver.quit()

@pytest.fixture
def back_login(init):
    init.get(g_data.login_url)
    yield init

# 前置条件：用户已登陆   后置条件：关闭浏览器
@pytest.fixture(scope="class")
def access(init):
    logger.info("========== class级 前置操作:登陆系统 ===============")
    LoginPage(init).login(*g_data.user)
    yield init

@pytest.fixture
def back_home(access):
    access.get(g_data.home_url)
    yield access
