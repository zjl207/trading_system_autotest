# coding=utf-8
# @time: 2023/1/10 20:27
# Author: zjl

class TopRightCornerProfilePicture:
    def profile_picture_base(self):
        """
        右上角个人头像定位表达式
        :return:
        """
        return "//img[@style='object-fit: fill;']/parent::span"

    def log_out(self):
        """
        右上角个人头像定悬浮之退出定位表达式
        :return:
        """
        return "//li[@class='el-dropdown-menu__item']/parent::ul//li[last()]"
