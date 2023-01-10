# coding=utf-8
# @time: 2023/1/10 19:30
# Author: zjl

from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.IframeBaiduMapBase import IframeBaiduMapBase


class IframeBaiduMapPage(ObjectMap, IframeBaiduMapBase):
    def get_baidu_map_search_button(self, driver):
        """
        获取百度地图搜索按钮
        :param driver:
        :return:
        """
        button_xpath = self.serch_button()
        return self.element_get(driver, By.XPATH, button_xpath)

    def switch_2_baidu_map_iframe(self, driver):
        """
        切换到百度地图的iframe
        :param driver:
        :return:
        """
        iframe_xpath = self.baidu_map_iframe()
        return self.switch_into_iframe(driver, By.XPATH, iframe_xpath)

    def iframe_out(self, driver):
        """
        从百度地图切换回二手交易系统
        :param driver:
        :return:
        """
        return self.switch_from_iframe_to_content(driver)
