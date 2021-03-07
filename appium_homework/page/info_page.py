# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/7 15:14
@Auth ： wanghao
@File ：info_page.py
"""
from appium_homework.page.address_page import AddressPage
from appium_homework.page.base_page import BasePage


class InfoPage(BasePage):
    # 进入通讯录页面
    def goto_address(self):
        self.parse_action("../page/info_page.yaml", "goto_address")
        return AddressPage(self.driver)
