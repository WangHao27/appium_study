# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/27 19:39
@Auth ： wanghao
@File ：search.py
"""
from test_yaml.page.base_page import BasePage



class SearchPage(BasePage):
    def search(self, value):
        self._params["search"] = value
        self.steps("../page/search.yaml")
