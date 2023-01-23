# coding=utf-8
# @time: 2023/1/3 20:33
# Author: zjl
import time

from selenium.webdriver.common.by import By

from base.LoginBase import LoginBase
from base.ObjectMap import ObjectMap
from common.yaml_config import GetConf
from logs.log import log
from common.report_add_img import add_img_path_2_report
from common.ocr_identify import OcrIdentify


class LoginPage(LoginBase, ObjectMap):
    def login_input_value(self, driver, input_placeholder, input_value):
        """
        登录页输入值
        :param driver:
        :param input_placeholder:
        :param input_value:
        :return:
        """
        log.info("输入" + input_placeholder + "为：" + str(input_value))
        input_xpath = self.login_input(input_placeholder)
        # return driver.find_element_by_xpath(input_xpath).send_keys(input_value)
        return self.element_fill_value(driver, By.XPATH, input_xpath, input_value)

    def click_login(self, driver, button_name):
        """
        点击登录
        :param driver:
        :param button_name:
        :return:
        """
        log.info("点击登录")
        button_xpath = self.login_button(button_name)
        return self.element_click(driver, By.XPATH, button_xpath)

    def login(self, driver, user, need_captcha=False):
        """
        登录
        :param driver:
        :param user:
        :param need_captcha: 是否点击勾选验证码按钮
        :return:
        """
        log.info("跳转登录页")
        self.element_to_url(driver, "/login")
        if need_captcha:
            time.sleep(3)
            log.info("需要验证码")
            self.select_need_captcha(driver)
            captcha_xpath = self.captcha()
            ele_img_path = self.element_screenshot(driver, By.XPATH, captcha_xpath)
            add_img_path_2_report(ele_img_path, "图像验证码")
            identify = OcrIdentify().identify(ele_img_path)
            log.info("验证码为：" + str(identify))
            input_captcha_xpath = self.input_captcha()
            log.info("填入验证码")
            self.element_fill_value(driver, By.XPATH, input_captcha_xpath, identify)
            time.sleep(3)
        username, password = GetConf().get_username_password(user)
        self.login_input_value(driver, "用户名", username)
        self.login_input_value(driver, "密码", password)
        self.click_login(driver, "登录")
        self.assert_login_success(driver)

    def login_assert(self, driver, img_name):
        """
        登录后判断头像
        :param driver:
        :param img_name:
        :return:
        """
        return self.find_img_in_source(driver, img_name)

    def assert_login_success(self, driver):
        """
        验证是否登录成功
        :param driver:
        :return:
        """
        success_xpath = self.login_success()
        self.element_appear(driver, By.XPATH, success_xpath, timeout=2)

    def select_need_captcha(self, driver):
        """
        点击勾选是否需要验证码
        :param driver:
        :return:
        """
        log.info("点击勾选是否需要验证码")
        select_xpath = self.need_captcha()
        return self.element_click(driver, By.XPATH, select_xpath)
