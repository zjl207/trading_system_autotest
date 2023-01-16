# coding=utf-8
# @time: 2023/1/3 20:41
# Author: zjl

from time import sleep
import allure

from page.LoginPage import LoginPage
from common.report_add_img import add_img_2_report


class TestLogin:
    @allure.description("窗口句柄description")
    @allure.epic("窗口句柄epic")
    @allure.feature("窗口句柄feature")
    @allure.story("窗口句柄story")
    @allure.tag("窗口句柄tag")
    def test_login(self, driver):
        """登陆后断言头像图片"""
        LoginPage().login(driver, "jay")
        add_img_2_report(driver, "登录页")
        sleep(3)
        assert LoginPage().login_assert(driver, "head_img.jpg") > 0.9
        # driver.get("http://www.tcpjwtester.top")
        # sleep(3)
        # LoginPage().login_input_value(driver, "用户名", "周杰伦")
        # sleep(1)
        # LoginPage().login_input_value(driver, "密码", "123456")
        # sleep(1)
        # LoginPage().click_login(driver, "登录")
        # sleep(3)
