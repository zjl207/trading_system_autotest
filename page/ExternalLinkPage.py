# coding=utf-8
# @time: 2023/1/10 17:05
# Author: zjl

from base.ObjectMap import ObjectMap


class ExternalLinkPage(ObjectMap):

    def goto_imooc(self, driver):
        """
        切换窗口为慕课网
        :param driver:
        :return:
        """
        self.switch_window_2_latest_handle(driver)
        return driver.title
