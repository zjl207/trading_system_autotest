# coding=utf-8
# @time: 2023/1/10 17:08
# Author: zjl

from time import sleep

from page.ExternalLinkPage import ExternalLinkPage
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage


class TestWindowHandle:
    def test_switch_window_handles(self, driver):
        LoginPage().login(driver, "jay")
        sleep(3)
        LeftMenuPage().click_level_one_menu(driver, "外链")
        sleep(1)
        title = ExternalLinkPage().goto_imooc(driver)
        print("title:" + title)