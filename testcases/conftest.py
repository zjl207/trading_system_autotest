# coding=utf-8
# @time: 2023/1/13 16:38
# Author: zjl


import pytest

from config.driver_config import DriverConfig


@pytest.fixture()
def driver():
    get_driver = DriverConfig().driver_config()
    yield get_driver
    get_driver.quit()
