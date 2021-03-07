# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/7 15:17
@Auth ： wanghao
@File ：savemember_page.py
"""
from appium_homework.page.base_page import BasePage


class SaveMembersPage(BasePage):
    def savemembers(self, name, phone):
        self._params['name'] = name
        self._params['phone'] = phone
        self.parse_action("../page/savemember_page.yaml", "savemembers")