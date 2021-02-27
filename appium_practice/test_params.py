# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/25 22:32
@Auth ： wanghao
@File ：test_params.py
"""
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *


class TestParams:

    def setup(self):
        caps = {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "MIX_2",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "resetKeyboard": 'true',
            "unicodeKeyboard": 'true',
            "noReset": True,
            "dontStopAppOnReset": 'true',
            "skipServerInstallation": True
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/action_close").click()
        # self.driver.quit()

    @pytest.mark.parametrize('searchKey, type, except_price', [
        ('小米', '01810', 25),
        ('阿里巴巴', '09988', 230.5),
    ])
    def test_search(self, searchKey, type, except_price):
        """
        1、打开雪球
        2、点击 搜索框
        3、输入 搜索词 如“阿里巴巴  小米”
        4、点击第一个搜索结果
        5、判断 股票价格
        :return:
        """
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(searchKey)
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/name").click()
        current_price = self.driver.find_element(MobileBy.XPATH, f"//*[@text={type}]/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(f"当前价格为{current_price}")
        assert_that(float(current_price), close_to(except_price, except_price * 0.1))













