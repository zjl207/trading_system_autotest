# coding=utf-8
# @time: 2023/1/10 17:50
# Author: zjl

class AccountBase:
    def basic_info_avatar_input(self):
        """
        个人头像定位表达式
        :return:
        """
        return "//input[@type='file']"

    def basic_info_save_button(self):
        """
        个人资料修改保存按钮定位表达式
        :return:
        """
        return "//span[text()='保存']//parent::button"
