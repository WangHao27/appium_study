# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/27 19:36
@Auth ： wanghao
@File ：market.py
"""
from test_yaml.page.base_page import BasePage
from test_yaml.page.search import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return SearchPage(self.driver)