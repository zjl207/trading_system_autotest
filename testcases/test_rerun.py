# coding=utf-8
# @time: 2023/1/13 17:36
# Author: zjl
import random

import pytest


class TestRerun:
    # @pytest.mark.flaky(reruns=5, reruns_delay=1)
    def test_rerun(self):
        # 随机生成1到3的整数
        num = random.randint(1, 3)
        print("num:", num)
        if num != 1:
            print("失败")
            raise Exception("出错了")
        else:
            print("成功")
