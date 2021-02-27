# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/27 19:46
@Auth ： wanghao
@File ：test_search.py
"""
import yaml

from test_yaml.page.app import App


class TestSearch:
    def test_search(self):
        App().start().main().goto_market().goto_search().search("jd")
