# coding=utf-8
# @time: 2023/1/26 18:14
# Author: zjl

from common.tools import get_now_time
from common.redis_operation import RedisOperation


class Process:

    def __init__(self):
        self.redis_client = RedisOperation().redis_client
        self.UI_AUTOTEST_PROCESS = "ui_autotest_process"
        self.FAILED_TESTCASE_NAMES = "failed_testcase_names"
        self.RUNNING_STATUS = "running_status"

    def reset_all(self):
        # 删除所有进度
        self.redis_client.delete(self.UI_AUTOTEST_PROCESS)
        # 删除所有失败用例的名称
        self.redis_client.delete(self.FAILED_TESTCASE_NAMES)

    def init_process(self, total):
        """
        初始化进度，包括总数、成功数、失败数、开始时间，运行状态
        :param total:测试用例总数
        :return:
        """
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "total", total)
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "success", 0)
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "fail", 0)
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "start_time", get_now_time())
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "end_time", "")
        self.redis_client.set(self.RUNNING_STATUS, 1)

    def update_success(self):
        """
        成功用例个数+1
        Returns:

        """
        self.redis_client.hincrby(self.UI_AUTOTEST_PROCESS, "success")

    def update_fail(self):
        """
        失败用例个数+1
        Returns:

        """
        self.redis_client.hincrby(self.UI_AUTOTEST_PROCESS, "fail")

    def insert_into_fail_testcase_names(self, fail_testcase_name):
        """
        增加失败用例名称
        Returns:

        """
        self.redis_client.lpush(self.FAILED_TESTCASE_NAMES, fail_testcase_name)

    def get_process(self):
        """
        获取进度，计算百分比
        Returns:

        """
        total, success, fail, _ = self.get_result()
        if total == 0:
            return 0
        else:
            result = "%.1f" % ((int(success) + int(fail)) / int(total) * 100) + "%"
            return result

    def get_result(self):
        """
        获取测试结果
        Returns:

        """
        total = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "total")
        if total is None:
            total = 0
        success = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "success")
        if success is None:
            success = 0
        fail = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "fail")
        if fail is None:
            fail = 0
        start_time = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "start_time")
        if start_time is None:
            start_time = '-'
        return total, success, fail, start_time

    def get_fail_testcase_names(self):
        """
        获取所有失败的用例名称
        Returns:

        """
        fail_testcase_names = self.redis_client.lrange(self.FAILED_TESTCASE_NAMES, 0, -1)
        return fail_testcase_names

    def write_end_time(self):
        """
        把测试结束时间写入redis
        Returns:

        """
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "end_time", get_now_time())

    def write_jenkins_build_number(self, build_number):
        """
        把jenkins执行的build_number写入redis
        Args:
            build_number:

        Returns:

        """
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "build_number", build_number)

    def write_allure_report(self, report_url):
        """
        把jenkins执行的allure_report写入redis
        Args:
            report_url:

        Returns:

        """
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "report_url", report_url)

    def modify_running_status(self, status):
        """
        修改jenkins执行状态
        Args:
            status: 0为不在运行，1为正在运行

        Returns:

        """
        self.redis_client.set(self.RUNNING_STATUS, status)
