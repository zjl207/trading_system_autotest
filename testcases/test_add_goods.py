# coding=utf-8
# @time: 2023/1/8 23:54
# Author: zjl

from time import sleep
import allure

import pytest

from common.report_add_img import add_img_2_report
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage

goods_info_list = [
    {
        "goods_title": "新增批量商品测试book1",
        "goods_details": "新增批量商品测试详情1",
        "goods_num": 1,
        "goods_pic_list": ["商品图片book.jpg"],
        "goods_price": 100,
        "goods_status": "上架",
        "bottom_button_name": "提交"
    },
    {
        "goods_title": "新增批量商品测试book2",
        "goods_details": "新增批量商品测试详情2",
        "goods_num": 2,
        "goods_pic_list": ["商品图片book.jpg"],
        "goods_price": 100,
        "goods_status": "上架",
        "bottom_button_name": "提交"
    }
]


class TestAddGoods:
    @allure.description("窗口句柄description")
    @allure.epic("窗口句柄epic")
    @allure.feature("窗口句柄feature")
    @allure.story("窗口句柄story")
    @allure.tag("窗口句柄tag")
    @pytest.mark.parametrize("goods_info", goods_info_list)
    def test_add_goods_001(self, driver, goods_info):
        """新增二手商品"""
        LoginPage().login(driver, "jay")
        sleep(2)
        LeftMenuPage().click_level_one_menu(driver, "产品")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "新增二手商品")
        sleep(2)
        GoodsPage().add_new_goods(
            driver,
            goods_title=goods_info["goods_title"],
            goods_details=goods_info["goods_details"],
            goods_num=goods_info["goods_num"],
            goods_pic_list=goods_info["goods_pic_list"],
            goods_price=goods_info["goods_price"],
            goods_status=goods_info["goods_status"],
            bottom_button_name=goods_info["bottom_button_name"])
        sleep(3)
        add_img_2_report(driver, "上架商品")
