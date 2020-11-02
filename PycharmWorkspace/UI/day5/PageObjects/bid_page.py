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
from PageLocators.bid_page_loc import BidPageLoc as loc
from Common.basepage import Basepage



class BidPage(Basepage):

    def get_user_left_money(self):
        return self.get_attribute(loc.money_input,"标页面_获取用户余额","data-amount")

    def get_bid_left_money(self):
        return self.get_text(loc.bid_money_text,"标页面_获取标可投资余额")

    def invest(self,money):
        self.input_text(loc.money_input,"标页面_输入投资金额",money)
        self.click_element(loc.invest_button,"标页面_点投资按钮")

    # 点击成功的弹框里，激活并点击按钮
    def click_activation_button_on_success_popup(self):
        self.click_element(loc.active_button_on_successPop,"标页面_点击激活并查看按钮")

    def get_msg_on_invest_faild_popup(self):
        return self.get_text(loc.invest_failed_popup,"标页面_获取投资失败弹出框的文本")
