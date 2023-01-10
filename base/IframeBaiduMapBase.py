# coding=utf-8
# @time: 2023/1/10 19:28
# Author: zjl

class IframeBaiduMapBase:
    def serch_button(self):
        return "//button[@id='search-button']"

    def baidu_map_iframe(self):
        return "//iframe[@src='https://map.baidu.com/']"
