# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/7 15:18
@Auth ： wanghao
@File ：app.py
"""
from appium import webdriver
from appium_homework.page.base_page import BasePage
from appium_homework.page.info_page import InfoPage


class App(BasePage):
    def start(self):
        _package = "com.tencent.wework"
        _activity = ".launch.WwMainActivity"
        if self.driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["platformVersion"] = "6.0"
            caps["deviceName"] = "MIX_2"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps["noReset"] = True  # 保留上一次操作信息
            caps["autoGrantPermissions"] = True  # Appium自动授权app权限
            caps["unicodeKeyboard"] = True  # 解决无法输入中文问题
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            # 复用之前的app服务，不用每次重启
            self.driver.start_activity(_package, _activity)
        self.driver.implicitly_wait(10)
        return self

    def goto_info(self):
        return InfoPage(self.driver)