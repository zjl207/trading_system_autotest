# coding=utf-8
# @time: 2023/1/8 22:34
# Author: zjl

from selenium.webdriver.common.by import By

from base.LeftMenuBase import LeftMenuBase
from base.ObjectMap import ObjectMap


class LeftMenuPage(LeftMenuBase, ObjectMap):
    def click_level_one_menu(self, driver, menu_name):
        """
        点击一级菜单
        :param driver:
        :param menu_name:
        :return:
        """
        menu_xpath = self.lever_one_menu(menu_name)
        return self.element_click(driver, By.XPATH, menu_xpath)

    def click_level_two_menu(self, driver, menu_name):
        """
        点击二级菜单
        :param driver:
        :param menu_name:
        :return:
        """
        menu_xpath = self.lever_two_menu(menu_name)
        return self.element_click(driver, By.XPATH, menu_xpath)
