"""
======================
Author: 柠檬班-小简
Time: 2020/8/31 21:37
Project: day4
Company: 湖南零檬信息技术有限公司
======================
"""
"""
前置：登陆
"""
import pytest
from PageObjects.home_page import HomePage
from PageObjects.bid_page import BidPage
from PageObjects.user_page import UserPage
from Common.my_logger import logger

@pytest.mark.usefixtures("back_home")
class TestInvest:

    @pytest.mark.smoke
    def test_invest_success(self,back_home):
        logger.info(" **** 正向用例:登陆成功   检验:用户余额是否变化,标的可余额是否变化 ***** ")
        # 前置 - 步骤  - 断言
        # 1、首页 - 选择第1个标，点击抢投标按钮
        HomePage(back_home).click_first_invest_button()
        # 2、标页面 - 获取用户的  投资前的余额
        bp = BidPage(back_home)
        user_money_before_invest = bp.get_user_left_money()
        # 2、标页面 - 获取标的 投资前的标余额
        bid_money_before_invest = bp.get_bid_left_money()
        # 2、标页面 - 输入投资金额2000，点击投资按钮。
        bp.invest(2000)
        # 3、标页面 - 点击查看并激活
        bp.click_activation_button_on_success_popup()

        # 1、用户的钱少了没有
        # 投资之前 - 投资之后 = 2000
        # 用户页面 - 得到用户当前余额
        user_money_after_invest = UserPage(back_home).get_user_left_money()
        # 2、标的可投余额少了没有
        # 标前 - 标后 = 2000
        # 用户页面 - 回退一次
        UserPage(back_home).back_last_page().refresh_page()
        # 刷新页面，
        # 标页面 - 获取投资后的标余额
        bid_money_after_invest = bp.get_bid_left_money()
        # 1、用户的钱少了没有
        assert float(user_money_before_invest) - float(user_money_after_invest) == 2000
        assert float(bid_money_before_invest)*10000 - float(bid_money_after_invest) * 10000 == 2000


    def test_invest_failed_no100(self, back_home):
        logger.info(" **** 异常用例:投资失败   检验:???? ***** ")
        # 前置 - 步骤  - 断言
        # 1、首页 - 选择第1个标，点击抢投标按钮
        HomePage(back_home).click_first_invest_button()
        # 2、标页面 - 输入投资金额50，点击投资按钮。
        bp = BidPage(back_home)
        bp.invest(50)
        # 断言
        assert bp.get_msg_on_invest_faild_popup() == "投标金额必须为100的倍数"

