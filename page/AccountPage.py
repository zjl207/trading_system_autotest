# coding=utf-8
# @time: 2023/1/10 18:00
# Author: zjl
from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.AccountBase import AccountBase
from common.tools import get_image_path


class AccountPage(ObjectMap, AccountBase):
    def upload_avatar(self, driver, img_name):
        """
        上传个人头像
        :param driver:
        :param img_name:
        :return:
        """
        img_path = get_image_path(img_name)
        upload_xpath = self.basic_info_avatar_input()
        return self.upload(driver, By.XPATH, upload_xpath, img_path)

    def click_save(self, driver):
        """
        个人资料点击保存
        :param driver:
        :return:
        """
        button_xpath = self.basic_info_save_button()
        return self.element_click(driver, By.XPATH, button_xpath)
