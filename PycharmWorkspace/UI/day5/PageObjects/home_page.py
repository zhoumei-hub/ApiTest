"""
======================
Author: 柠檬班-小简
Time: 2020/8/24 21:01
Project: day1
Company: 湖南零檬信息技术有限公司
======================
"""

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

    # 点击抢投标按钮
    def click_first_invest_button(self):
        self.click_element(loc.bid_button,"首页_点击抢投标按钮")

