# coding=utf-8
# @time: 2023/1/10 17:34
# Author: zjl

from time import sleep

import pytest

from page.LoginPage import LoginPage
from page.OrderPage import OrderPage
from page.LeftMenuPage import LeftMenuPage

tab_list = ["全部", "待付款", "待发货", "运输中", "待确认", "待评价"]


class TestOrderBuy:
    @pytest.mark.parametrize("tab", tab_list)
    def test_order_buy(self, driver, tab):
        LoginPage().login(driver, "jay")
        sleep(2)
        LeftMenuPage().click_level_one_menu(driver, "我的订单")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "已买到的宝贝")
        sleep(1)
        OrderPage().click_order_tab(driver, tab)
        sleep(2)
