# coding=utf-8
# @time: 2023/1/13 17:55
# Author: zjl

import pytest
from pytest_assume.plugin import assume


class TestAssume:
    def test_assume(self):
        # 三种方式 1：使用插件  2：包  3：assert
        with assume: assert "zjl" in "UI autotest"
        pytest.assume(1 + 1 == 3)
        assert 1 + 1 == 2
        print("over")
