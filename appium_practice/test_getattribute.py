# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/25 21:01
@Auth ： wanghao
@File ：test_getattribute.py
"""
from time import sleep

import pytest
from hamcrest import *
from appium import webdriver


class TestAttribute:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6.0"
        caps["deviceName"] = "MIX_2"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["resetKeyboard"] = True  # 将键盘重置为其原始状态
        caps["noReset"] = True  # 保留上一次操作信息
        caps["dontStopAppOnReset"] = True  # 首次启动时，不停止app
        caps["skipDeviceInitialization"] = True  # 跳过设备初始化，如安装，权限等操作
        caps["unicodeKeyboard"] = True  # 解决无法输入中文问题
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_attribute(self):
        """
        通过get_attribute()方法获取元素属性值
        name(返回 content-desc 或 text)
        text(返回 text)
        className(返回 class，只有 API=>18 才能支持)
        resourceId(返回 resource-id，只有 API=>18 才能支持)
        :return:
        """
        sleep(2)
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search_ele.get_attribute("name"))
        print(search_ele.get_attribute("resourceId"))
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute("clickable"))
        # print(search_ele.get_attribute("bounds"))
        assert 'tv_search' in search_ele.get_attribute("resourceId")

    def test_assert(self):
        a = 10
        b = 20
        assert a == b






















