# coding=utf-8
# @time: 2023/1/10 17:34
# Author: zjl

from time import sleep

import pytest
import allure

from page.LoginPage import LoginPage
from page.OrderPage import OrderPage
from page.LeftMenuPage import LeftMenuPage
from common.report_add_img import add_img_2_report

tab_list = ["全部", "待付款", "待发货", "运输中", "待确认", "待评价"]


class TestOrderBuy:
    @pytest.mark.parametrize("tab", tab_list)
    @allure.description("窗口句柄description")
    @allure.epic("窗口句柄epic")
    @allure.feature("窗口句柄feature")
    @allure.story("窗口句柄story")
    @allure.tag("窗口句柄tag")
    def test_order_buy(self, driver, tab):
        LoginPage().login(driver, "jay")
        sleep(2)
        LeftMenuPage().click_level_one_menu(driver, "我的订单")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "已买到的宝贝")
        sleep(1)
        OrderPage().click_order_tab(driver, tab)
        add_img_2_report(driver, "已买到的宝贝状态截图")
        sleep(2)
