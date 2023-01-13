# coding=utf-8
# @time: 2023/1/10 19:37
# Author: zjl

from time import sleep

from page.IframeBaiduMapPage import IframeBaiduMapPage
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage


class TestIframeBaiduMap:
    def test_iframe_baidu_map(self, driver):
        LoginPage().login(driver, "jay")
        sleep(3)
        LeftMenuPage().click_level_one_menu(driver, "iframe测试")
        sleep(1)
        IframeBaiduMapPage().switch_2_baidu_map_iframe(driver)
        IframeBaiduMapPage().get_baidu_map_search_button(driver)
        IframeBaiduMapPage().iframe_out(driver)
        LeftMenuPage().click_level_one_menu(driver, "首页")
        sleep(3)