# coding=utf-8
# @time: 2023/1/10 21:02
# Author: zjl

from time import sleep

from config.driver_config import DriverConfig
from page.LoginPage import LoginPage
from page.TopRightCornerProfilePicturePage import TopRightCornerProfilePicture


class TestLogOut:
    def test_log_out(self):
        driver = DriverConfig().driver_config()
        LoginPage().login(driver, "jay")
        sleep(3)
        TopRightCornerProfilePicture().profile_picture(driver)
        sleep(3)
        TopRightCornerProfilePicture().log_out_click(driver)
        sleep(3)
        driver.quit()