# coding=utf-8
# @time: 2023/1/5 19:53
# Author: zjl

import time

from selenium.common.exceptions import ElementNotVisibleException, WebDriverException


class ObjectMap:
    def element_get(self, driver, locate_type, locate_expression, timeout=10, must_be_visible=False):
        """
        单个元素获取selenium的二次封装
        :param driver:浏览器驱动
        :param locate_type:定位方式类型
        :param locate_expression:定位表达式
        :param timeout:超时时间
        :param must_be_visible:元素是否必须可见，True是必须可见，False是默认值
        :return:返回的元素
        """
        # 开始时间
        start_ms = time.time() * 1000
        # 设置结束时间
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            # 查找元素
            try:
                element = driver.find_element(by=locate_type, value=locate_expression)
                # 如果元素不是必须可见的，就直接返回元素
                if not must_be_visible:
                    return element
                # 如果元素必须是可见的，则需要判断元素是否可见
                else:
                    # is_displayed()元素可见，直接返回元素
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
            except Exception:
                now_ms = time.time() * 1000
                if now_ms >= stop_ms:
                    break
                pass
            time.sleep(0.1)
        raise ElementNotVisibleException("元素定位失败，定位方式：" + locate_type + "定位表达式" + locate_expression)

    def wait_for_ready_state_complete(self, driver, timeout=30):
        """
        等待页面完全加载完成
        :param driver: 浏览器驱动
        :param timeout: 超时时间
        :return:
        """
        # 开始时间
        start_ms = time.time() * 1000
        # 设置的结束时间
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            try:
                # driver.execute_script执行浏览器控制台js语句;
                # document.readyState判断页面是否加载完成，是：complete,否：loading
                ready_state = driver.execute_script("return document.readyState")
            except WebDriverException:
                # 如果有driver的错误，执行js会失败，就直接跳过
                time.sleep(0.03)
                return True
            # 如果页面全部加载完成就返回True
            if ready_state == "complete":
                time.sleep(0.01)
                return True
            else:
                now_ms = time.time() * 1000
                # 如果超时了就break
                if now_ms >= stop_ms:
                    break
                time.sleep(0.1)
        raise Exception("打开网页时,页面元素在%s秒后任然没有完全加载" % timeout)

    def element_disappear(self, driver, locate_type, locate_expression, timeout=30):
        """
        等待页面元素消失
        :param driver:浏览器驱动
        :param locate_type: 定位方式类型
        :param locate_expression: 定位表达式
        :param timeout: 超时时间
        :return:
        """
        if locate_type:
            # 开始时间
            start_ms = time.time()
            # 设置结束时间
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locate_expression)
                    if element.is_displayed():
                        now_ms = time.time() * 1000
                        if now_ms >= stop_ms:
                            break
                        time.sleep(0.1)
                except Exception:
                    return True
            raise Exception("元素没有消失，定位方式：" + locate_type + "\n定位表达式" + locate_expression)
        else:
            pass

    def element_appear(self, driver, locate_type, locate_expression, timeout=30):
        """
        等待页面元素出现
        :param driver:浏览器驱动
        :param locate_type:定位方式
        :param locate_expression:定位表达式
        :param timeout:超时时间
        :return:
        """
        if locate_type:
            # 开始时间
            start_ms = time.time() * 1000
            # 设置结束时间
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locate_expression)
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
                except Exception:
                    now_ms = time.time() * 1000
                    if now_ms >= stop_ms:
                        break
                    time.sleep(0.1)
                    pass
            raise ElementNotVisibleException(
                "元素没有出现，定位方式：" + locate_type + "\n定位表达式" + locate_expression)
        else:
            pass
