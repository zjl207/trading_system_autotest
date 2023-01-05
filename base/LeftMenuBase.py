# coding=utf-8
# @time: 2023/1/4 22:04
# Author: zjl

class LeftMenuBase:
    def lever_one_menu(self, menu_name):
        """
        一级菜单栏名称git
        :param menu_name:
        :return:
        """
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/ancestor::li"

    def lever_two_menu(self, menu_name):
        """
        二级菜单栏名称
        :param menu_name:
        :return:
        """
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/parent::li"

    def order_details(self, menu_name):
        """
        订单详情
        :param menu_name:
        :return:
        """
        return "//main[@class='el-main']//div[text()='" + menu_name + "']"
