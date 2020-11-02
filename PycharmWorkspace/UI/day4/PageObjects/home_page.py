"""
======================
Author: 柠檬班-小简
Time: 2020/8/24 21:01
Project: day1
Company: 湖南零檬信息技术有限公司
======================
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

from PageLocators.home_page_locs import HomePageLocs as loc
from Common.basepage import Basepage

class HomePage(Basepage):

    def is_exit_exist(self):
        try:
            self.wait_ele_visible(loc.exit_loc,"首页_等待退出元素可见")
        except:
            return False
        else:
            return True

    def click_first_invest_button(self):
        pass

