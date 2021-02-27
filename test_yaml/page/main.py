# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/27 19:32
@Auth ： wanghao
@File ：main.py
"""
from test_yaml.page.base_page import BasePage
from test_yaml.page.market import MarketPage


class Main(BasePage):

    def goto_market(self):
        self.steps("../page/main.yaml")
        return MarketPage(self.driver)