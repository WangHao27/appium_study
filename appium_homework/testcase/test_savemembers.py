# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/7 16:52
@Auth ： wanghao
@File ：test_savemembers.py
"""
from appium_homework.page.app import App


class TestSaveMembers:
    def test_savemembers(self):
        name = "李武"
        phone = "13626654813"
        App().start().goto_info().goto_address().goto_addmenbers().goto_savemembers().savemembers(name=name, phone=phone)
