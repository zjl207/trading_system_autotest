# coding=utf-8
# @time: 2023/1/3 20:41
# Author: zjl

from time import sleep
from page.LoginPage import LoginPage


class TestLogin:
    def test_login(self, driver):
        """登陆后断言头像图片"""
        LoginPage().login(driver, "jay")
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
