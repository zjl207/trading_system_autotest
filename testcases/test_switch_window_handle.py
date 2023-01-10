# coding=utf-8
# @time: 2023/1/10 17:08
# Author: zjl

from time import sleep

from page.ExternalLinkPage import ExternalLinkPage
from config.driver_config import DriverConfig
from page.LeftMenuPage import LeftMenuPage
from page.LoginPage import LoginPage


class TestWindowHandle:
    def test_switch_window_handles(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, "jay")
        sleep(3)
        LeftMenuPage().click_level_one_menu(driver, "外链")
        sleep(1)
        title = ExternalLinkPage().goto_imooc(driver)
        print("title:" + title)
        driver.quit()
