# coding=utf-8
# @time: 2023/1/24 22:25
# Author: zjl

from time import sleep
import allure
import pytest

from page.LoginPage import LoginPage
from common.report_add_img import add_img_2_report


class TestLoginAssert:
    @pytest.mark.login
    @allure.feature("登录")
    @allure.description("登录后断言图片")
    def test_login_assert(self, driver):
        """登陆后断言头像图片"""
        with allure.step("登录"):
            LoginPage().login(driver, "william")
            sleep(3)
            add_img_2_report(driver, "登录")

        with allure.step("断言图片"):
            assert LoginPage().login_assert(driver, "head_img.jpg") > 0.9
