# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/7 15:16
@Auth ： wanghao
@File ：addmembers_page.py
"""
from appium_homework.page.base_page import BasePage
from appium_homework.page.savemember_page import SaveMembersPage


class AddMembersPage(BasePage):
    # 进入保存成员界面
    def goto_savemembers(self):
        self.parse_action("../page/addmembers_page.yaml", "goto_savemembers")
        return SaveMembersPage(self.driver)
