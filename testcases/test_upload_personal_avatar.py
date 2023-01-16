# coding=utf-8
# @time: 2023/1/10 18:12
# Author: zjl

from time import sleep

import allure

from page.LoginPage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.AccountPage import AccountPage
from common.report_add_img import add_img_2_report


class TestPersonalInfo:
    @allure.description("窗口句柄description")
    @allure.epic("窗口句柄epic")
    @allure.feature("窗口句柄feature")
    @allure.story("窗口句柄story")
    @allure.tag("窗口句柄tag")
    def test_upload_personal_avatar(self, driver):
        LoginPage().login(driver, "jay")
        sleep(2)
        LeftMenuPage().click_level_one_menu(driver, "账户设置")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver, "个人资料")
        sleep(1)
        AccountPage().upload_avatar(driver, "个人头像1.jpg")
        sleep(3)
        AccountPage().click_save(driver)
        add_img_2_report(driver, "保存上传头像")
        sleep(1)
