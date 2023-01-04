# coding=utf-8
# @time: 2023/1/2 22:24
# Author: zjl
from config.driver_config import DriverConfig

driver = DriverConfig.driver_config()
driver.get("www.baidu.com")