# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/25 22:18
@Auth ： wanghao
@File ：test_hamcrest.py
"""
from hamcrest import *


class TestHamcrest:

    def test_hamcrest(self):
        assert_that(10, equal_to(10))
        # close_to匹配数字接近给定值
        assert_that(12, close_to(10, 2))
        assert_that("contains some string", contains_string("some"))