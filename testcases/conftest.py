# coding=utf-8
# @time: 2023/1/13 16:38
# Author: zjl


import pytest

from config.driver_config import DriverConfig
from common.report_add_img import add_img_2_report


@pytest.fixture()
def driver():
    # 定义为全局变量
    global get_driver
    get_driver = DriverConfig().driver_config()
    yield get_driver
    get_driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    失败后截图加入测试报告
    pytest内置钩子函数,名称不能变更
    :param item:
    :param call:
    :return:
    """
    # 获取钩子方法的调用结果
    out = yield
    # 从钩子方法的调用结果中获取测试报告
    report = out.get_result()
    report.description = str(item.function.__doc__)  # 测试用例函数里的文档（注释）
    if report.when == "call":
        if report.failed:
            # 失败了截图
            add_img_2_report(get_driver, "失败截图", need_sleep=False)
