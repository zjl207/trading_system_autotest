# coding=utf-8
# @time: 2023/1/10 19:37
# Author: zjl

from time import sleep
import allure

from page.IframeBaiduMapPage import IframeBaiduMapPage
from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from common.report_add_img import add_img_2_report


class TestIframeBaiduMap:
    @allure.description("窗口句柄description")
    @allure.epic("窗口句柄epic")
    @allure.feature("窗口句柄feature")
    @allure.story("窗口句柄story")
    @allure.tag("窗口句柄tag")
    def test_iframe_baidu_map(self, driver):
        LoginPage().login(driver, "jay")
        sleep(3)
        LeftMenuPage().click_level_one_menu(driver, "iframe测试")
        sleep(1)
        IframeBaiduMapPage().switch_2_baidu_map_iframe(driver)
        IframeBaiduMapPage().get_baidu_map_search_button(driver)
        add_img_2_report(driver, "百度地图")
        IframeBaiduMapPage().iframe_out(driver)
        LeftMenuPage().click_level_one_menu(driver, "首页")
        add_img_2_report(driver, "首页")
        sleep(3)
