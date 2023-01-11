# coding=utf-8
# @time: 2023/1/11 18:05
# Author: zjl

class TestAssert:
    def test_assert(self):
        # ==, !=, <, >, <=, >=
        assert "zjl" == "zjl"
        assert "zjl-a" != "zjl-b"
        assert 0 < 1
        assert 2 > 1
        assert 3 <= 7 - 2
        assert 4 >= 1 + 2
        # 包含和不包含
        assert "zjl" in "zjl UI自动化测试"
        assert "zjl" not in "UI自动化测试"
        # true和false
        assert 1
        assert (9 < 10) is True
        assert not False

