# coding=utf-8
# @time: 2023/1/11 16:58
# Author: zjl


from time import sleep

import pytest

from config.driver_config import DriverConfig


class TestPytestMClass:
    @pytest.fixture(scope="class")
    def scope_class(self):
        print("我是class级别，我只执行一次")

    @pytest.fixture(scope="function")
    def driver(self):
        get_driver = DriverConfig().driver_config()
        return get_driver

    @pytest.mark.bing
    def test_open_bing(self, driver, scope_class):
        # driver = DriverConfig().driver_config()
        driver.get("https://cn.bing.com")
        sleep(3)
        driver.quit()

    @pytest.mark.baidu
    def test_open_baidu(self, driver, scope_class):
        # driver = DriverConfig().driver_config()
        driver.get("https://www.baidu.com")
        sleep(3)
        driver.quit()

    @pytest.mark.taobao
    def test_open_taobao(self, driver, scope_class):
        # driver = DriverConfig().driver_config()
        driver.get("https://www.taobao.com")
        sleep(3)
        driver.quit()
