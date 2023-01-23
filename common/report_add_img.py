# coding=utf-8
# @time: 2023/1/16 0:05
# Author: zjl

from time import sleep

import allure


def add_img_2_report(driver, step_name, need_sleep=True):
    """
    截图并插入allure报告
    :param driver: 浏览器驱动
    :param step_name: 步骤名称
    :param need_sleep: 
    :return: 
    """
    if need_sleep:
        sleep(2)
    allure.attach(driver.get_screenshot_as_png(), step_name + ".png", allure.attachment_type.PNG)


def add_img_path_2_report(img_path, step_name):
    """
    将图片插入allure报告
    :param img_path: 图片路径
    :param step_name: 步骤名称
    :return:
    """
    allure.attach.file(img_path, step_name, allure.attachment_type.PNG)
