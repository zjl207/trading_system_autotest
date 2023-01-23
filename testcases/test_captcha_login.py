# coding=utf-8
# @time: 2023/1/23 20:33
# Author: zjl

from time import sleep

import pytest
import allure

from common.report_add_img import add_img_2_report
from page.LoginPage import LoginPage


class TestCaptchaLogin:
    @pytest.mark.login
    @allure.feature("登录")
    @allure.description("验证码登录")
    def test_captcha_login(self, driver):
        """
        验证码登录
        :param driver:
        :return:
        """
        with allure.step("登录"):
            LoginPage().login(driver, "jay", need_captcha=True)
            sleep(3)
            add_img_2_report(driver, "登录页")
