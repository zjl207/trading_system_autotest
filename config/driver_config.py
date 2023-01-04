# coding=utf-8
# @time: 2023/1/3 18:18
# Author: zjl

# from time import sleep  # 系统自带的包

from selenium import webdriver  # 第三方的包
from webdriver_manager.chrome import ChromeDriverManager

from common.tools import get_project_path, sep  # 自定义的包


class DriverConfig:
    def driver_config(self):
        """
        浏览器驱动
        :return:
        """
        # 实例化谷歌浏览器设置方法
        options = webdriver.ChromeOptions()
        # 设置窗口大小，设置为1920*1080
        options.add_argument("window-size=1920,1080")
        # 去除"chrome正受到自动测试软件的控制"的提示
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # 解决selenium无法访问https的问题
        options.add_argument("--ignore-certificate-errors")
        # 允许忽略localhost上的TLS/SSL的错误
        options.add_argument("--allow-insecure-localhost")
        # 设置为无痕模式
        options.add_argument("--incognito")
        # 设置为无头模式(不打开浏览器后台运行)
        # options.add_argument("--headless")
        # 解决卡顿
        options.add_argument("--disable-gpu")  # gpu加速
        options.add_argument("--no-sandbox")  # 进入沙箱
        options.add_argument("--disable-dev-shm-usage")  # 防止测试用例过多内存溢出

        # driver = webdriver.Chrome(
        #     get_project_path() + sep(["driver_files", "chromedriver.exe"], add_sep_before=True),
        #     options=options)  # 获取chromedriver.exe路径
        driver = webdriver.Chrome(ChromeDriverManager(url="https://registry.npmmirror.com/-/binary/chromedriver",
                                                      latest_release_url="https://registry.npmmirror.com/-/binary/chromedriver/LATEST_RELEASE",
                                                      cache_valid_range=365).install(),  # cache_valid_range缓存时间为365
                                  options=options)  # 自动更新最新浏览器版本的ChromeDriver
        # 删除所有cookies
        driver.delete_all_cookies()

        return driver
    # 想要下载的zip链接： https://registry.npmmirror.com/-/binary/chromedriver/108.0.5359.71/chromedriver_win32.zip
    # LATEST_RELEASE链接： https://registry.npmmirror.com/-/binary/chromedriver/LATEST_RELEASE
