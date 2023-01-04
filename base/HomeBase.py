# coding=utf-8
# @time: 2023/1/4 20:53
# Author: zjl

class HomeBase:
    def wallet_switch(self):
        """
        首页的钱包开关
        :return:
        """
        return "//span[contains(@class,'switch')]"

    def logo(self):
        """
        进入系统后，首页左上角的logo
        :return:
        """
        return "//div[contains(text(),'二手')]"

    def welcome(self):
        """
        首页欢迎您回来
        :return:
        """
        return "//span[starts-with(text(),'欢迎您回来')]"

    def show_date(self):
        """
        首页显示日期
        :return:
        """
        return "//div[text()='我的日历']/following-sibling::div"

    def home_user_avatar(self):
        """
        首页用户头像大图
        :return:
        """
        return "//span[contains(text(),'欢迎您回来')]/parent::div/preceding-sibling::div//img"

    def home_user_avatar_2(self):
        """
        首页用户头像大图二
        :return:
        """
        return "//span[text()='我的地址']/ancestor::div[@class='first_card']/div[contains(@class,'user_avatar')]//img"



# //aside[@class='el-aside']//span[text()='首页']/ancestor::li
# //aside[@class='el-aside']//span[text()='已卖出的宝贝']/parent::li