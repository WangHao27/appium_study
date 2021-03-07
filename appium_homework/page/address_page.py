# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/7 15:14
@Auth ： wanghao
@File ：address_page.py
"""
from appium_homework.page.addmembers_page import AddMembersPage
from appium_homework.page.base_page import BasePage


class AddressPage(BasePage):
    # 进入添加成员界面
    def goto_addmenbers(self):
        self.swip_click("添加成员")
        return AddMembersPage(self.driver)