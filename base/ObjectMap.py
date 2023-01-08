# coding=utf-8
# @time: 2023/1/5 19:53
# Author: zjl

import time

from selenium.common.exceptions import ElementNotVisibleException, WebDriverException, NoSuchElementException, \
    StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

from common.yaml_config import GetConf


class ObjectMap:
    # 获取基础地址
    url = GetConf().get_url()

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

    def element_to_url(self, driver, url, locate_type_disappear=None, locate_expression_disappear=None,
                       locate_type_appear=None, locate_expression_appear=None):
        """
        跳转地址
        :param driver: 浏览器驱动
        :param url: 跳转的地址
        :param locate_type_disappear:等待页面元素消失的定位方式
        :param locate_expression_disappear: 等待页面元素消失的定位表达式
        :param locate_type_appear:等待页面元素出现的定位方式
        :param locate_expression_appear:等待页面元素出现的定位表达式
        :return:
        """
        try:
            driver.get(self.url + url)
            # 等待页面元素加载完成
            self.wait_for_ready_state_complete(driver)
            # 等待页面元素消失
            self.element_disappear(driver, locate_type_disappear, locate_expression_disappear)
            # 等待页面元素出现
            self.element_appear(driver, locate_type_appear, locate_expression_appear)
        except Exception as e:
            print("跳转地址出现异常，异常原因：%s" % e)
            return False
        return True

    def element_is_display(self, driver, locate_type, locate_expression):
        """
        元素是否显示
        :param driver:
        :param locate_type:
        :param locate_expression:
        :return:
        """
        try:
            driver.find_element(by=locate_type, value=locate_expression)
            return True
        except NoSuchElementException:
            # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False

    def element_fill_value(self, driver, locate_type, locate_expression, fill_value, timeout=30):
        """
        元素填值
        :param driver: 浏览器驱动
        :param locate_type: 定位方式
        :param locate_expression: 定位表达式
        :param fill_value: 填入的值
        :param timeout: 超时时间
        :return:
        """
        # 元素必须先出现
        element = self.element_appear(
            driver,
            locate_type=locate_type,
            locate_expression=locate_expression,
            timeout=timeout
        )
        try:
            # 先清除元素中的原有值
            element.clear()
        except StaleElementReferenceException:  # 页面元素没有刷新出来，就对元素进行捕获，从而引发了这个异常
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(driver, locate_type=locate_type, locate_expression=locate_expression,
                                          timeout=timeout)
            try:
                element.clear()
            except Exception:
                pass
        except Exception:
            pass
        try:
            # 填入的值转成字符串
            if type(fill_value) is int or type(fill_value) is float:
                fill_value = str(fill_value)
            # 填入的值不是以\n结尾
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)
            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver=driver)
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(driver, locate_type=locate_type, locate_expression=locate_expression)
            element.clear()
            # 填入的值转成字符串
            if type(fill_value) is int or type(fill_value) is float:
                fill_value = str(fill_value)
            # 填入的值不是以\n结尾
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)
            else:
                fill_value = fill_value[:-1]
                element.send_keys(fill_value)
                element.send_keys(Keys.RETURN)  # 执行回车
                self.wait_for_ready_state_complete(driver=driver)
        except Exception:
            raise Exception("元素填值失败")
        return True

    def element_click(self, driver, locate_type, locate_expression, locate_type_disappear=None,
                      locate_expression_disappear=None,
                      locate_type_appear=None, locate_expression_appear=None, timeout=30):
        """
        元素点击
        :param driver: 浏览器驱动
        :param locate_type: 定位方式类型
        :param locate_expression: 定位表达式
        :param locate_type_disappear: 等待元素消失的定位方式类型
        :param locate_expression_disappear: 等待元素消失的定位表达式
        :param locate_type_appear: 等待元素出现的定位方式类型
        :param locate_expression_appear: 等待元素出现的定位表达式
        :param timeout: 超时时间
        :return:
        """
        # 元素要可见
        element = self.element_appear(driver=driver, locate_type=locate_type, locate_expression=locate_expression,
                                      timeout=timeout)
        try:
            # 点击元素
            element.click()
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element = self.element_appear(driver=driver, locate_type=locate_type, locate_expression=locate_expression,
                                          timeout=timeout)
            element.click()
        except Exception as e:
            print("页面出现异常，元素不可点击", e)
            return False
        try:
            # 点击元素后元素的出现活消失
            self.element_appear(driver, locate_type_appear, locate_expression_appear)
            self.element_disappear(driver, locate_type_disappear, locate_expression_disappear)
        except Exception as e:
            print("等待元素消失活出现失败", e)
            return False
        return True

    def upload(self, driver, locate_type, locate_expression, file_path):
        """
        文件上传
        :param driver:
        :param locate_type:
        :param locate_expression:
        :param file_path:
        :return:
        """
        element = self.element_get(driver, locate_type, locate_expression)
        return element.send_keys(file_path)
