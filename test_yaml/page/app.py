# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/27 19:23
@Auth ： wanghao
@File ：app.py
"""
from appium import webdriver

from test_yaml.page.base_page import BasePage
from test_yaml.page.main import Main


class App(BasePage):
    def start(self):
        _package = "com.xueqiu.android"
        _activity = ".view.WelcomeActivityAlias"
        if self.driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["platformVersion"] = "6.0"
            caps["deviceName"] = "MIX_2"
            caps["appPackage"] = _package
            caps["appActivity"] = _activity
            caps["autoGrantPermissions"] = True  # Appium自动授权app权限
            caps["unicodeKeyboard"] = True  # 解决无法输入中文问题
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
        else:
            # 复用之前的app服务，不用每次重启
            self.driver.start_activity(_package, _activity)
        return self

    def main(self):
        # 传入driver 防止每次从0开始创建app
        return Main(self.driver)
























