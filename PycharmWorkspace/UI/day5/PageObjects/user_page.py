"""
======================
Author: 柠檬班-小简
Time: 2020/8/31 21:53
Project: day4
Company: 湖南零檬信息技术有限公司
======================
"""
from PageLocators.user_page_loc import UserPageLoc as loc
from Common.basepage import Basepage

class UserPage(Basepage):

    def get_user_left_money(self):
        value = self.get_text(loc.user_leftMoney,"用户页面_获取用户可用余额")
        return value.strip("元")
