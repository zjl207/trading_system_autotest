# coding=utf-8
# @time: 2023/1/10 21:02
# Author: zjl

from time import sleep
import allure

from page.LoginPage import LoginPage
from page.TopRightCornerProfilePicturePage import TopRightCornerProfilePicture
from common.report_add_img import add_img_2_report


class TestLogOut:
    def test_log_out(self, driver):
        LoginPage().login(driver, "jay")
        add_img_2_report(driver, "登录页")
        sleep(3)
        TopRightCornerProfilePicture().profile_picture(driver)
        sleep(3)
        TopRightCornerProfilePicture().log_out_click(driver)
        sleep(3)
        add_img_2_report(driver, "退出登录")
