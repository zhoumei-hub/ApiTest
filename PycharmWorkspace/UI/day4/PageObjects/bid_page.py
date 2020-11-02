"""
======================
Author: 柠檬班-小简
Time: 2020/8/31 21:45
Project: day4
Company: 湖南零檬信息技术有限公司
======================
"""
"""
原则：没有业务上必然的前后操作顺序关系，都分开来写。

# 2、标页面 - 获取用户的  投资前的余额
# 2、标页面 - 获取标的 投资前的标余额
# 2、标页面 - 输入投资金额2000，点击投资按钮。
# 3、标页面 - 点击查看并激活
# 4、标页面 - 获取文本内容
"""
# from PageLocators.login_page_locs import LoginPageLocs as loc
from Common.basepage import Basepage



class BidPage(Basepage):

    def get_user_left_money(self):
        pass

    def get_bid_left_money(self):
        pass

    def invest(self,money):
        pass

    # 点击成功的弹框里，激活并点击按钮
    def click_activation_button_on_success_popup(self):
        pass

