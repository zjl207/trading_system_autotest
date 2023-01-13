# coding=utf-8
# @time: 2023/1/10 17:34
# Author: zjl

from time import sleep

from page.LoginPage import LoginPage
from page.OrderPage import OrderPage
from page.LeftMenuPage import LeftMenuPage


class TestOrderBuy:
    def test_order_buy(self, driver):
        LoginPage().login(driver, "jay")
        sleep(2)
        LeftMenuPage().click_level_one_menu(driver, "我的订单")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "已买到的宝贝")
        sleep(1)
        tab_list = ["全部", "待付款", "待发货", "运输中", "待确认", "待评价"]
        for tab in tab_list:
            OrderPage().click_order_tab(driver, tab)
            sleep(2)