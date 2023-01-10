# coding=utf-8
# @time: 2023/1/10 20:45
# Author: zjl

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.TopRightCornerProfilePictureBase import TopRightCornerProfilePicture


class TopRightCornerProfilePicture(ObjectMap, TopRightCornerProfilePicture):
    def profile_picture(self, driver):
        """
        右上角头像鼠标悬浮
        :param driver:
        :return:
        """
        profile_picture_xpath = self.profile_picture_base()
        move = self.element_get(driver, By.XPATH, profile_picture_xpath)
        return self.action_chains(driver, move)

    def log_out_click(self, driver):
        """
        点击退出登录
        :param driver:
        :return:
        """
        log_out_xpath = self.log_out()
        return self.element_click(driver, By.XPATH, log_out_xpath)
