# coding=utf-8
# @time: 2023/1/3 20:41
# Author: zjl

from time import sleep
import allure
import pytest

from page.LoginPage import LoginPage
from common.report_add_img import add_img_2_report


class TestLogin:
    @allure.description("登录")
    @allure.epic("登录")
    @allure.feature("登录")
    @allure.story("登录")
    @allure.tag("登录")
    @pytest.mark.login
    def test_login(self, driver):
        """使用错误账号登录"""
        with allure.step("登录"):
            LoginPage().login(driver, "failure")
            sleep(3)
            add_img_2_report(driver, "登录页")
            # """登陆后断言头像图片"""
            # assert LoginPage().login_assert(driver, "head_img.jpg") > 0.9
