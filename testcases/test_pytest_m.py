# coding=utf-8
# @time: 2023/1/11 16:58
# Author: zjl


from time import sleep

import pytest

from config.driver_config import DriverConfig


class TestPytestMClass:
    @pytest.mark.bing
    def test_open_bing(self):
        driver = DriverConfig().driver_config()
        driver.get("https://cn.bing.com")
        sleep(3)
        driver.quit()

    @pytest.mark.baidu
    def test_open_baidu(self):
        driver = DriverConfig().driver_config()
        driver.get("https://www.baidu.com")
        sleep(3)
        driver.quit()

    @pytest.mark.google
    def test_open_google(self):
        driver = DriverConfig().driver_config()
        driver.get("https://www.google.com")
        sleep(3)
        driver.quit()
