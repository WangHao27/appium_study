# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/24 21:38
@Auth ： wanghao
@File ：test_toast.py
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestToast:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6.0"
        caps["deviceName"] = "MIX_2"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = "io.appium.android.apis.view.PopupMenul"
        caps["resetKeyboard"] = True  # 将键盘重置为其原始状态
        caps["noReset"] = True  # 保留上一次操作信息
        caps["dontStopAppOnReset"] = True  # 首次启动时，不停止app
        caps["skipDeviceInitialization"] = True  # 跳过设备初始化，如安装，权限等操作
        caps["unicodeKeyboard"] = True  # 解决无法输入中文问题
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    # 定位消息弹窗
    def test_toast(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Make a Pupup!").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Search']").click()
        print(self.driver.page_source)
        # 方法一：
        print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
        # 方法二(包含某个文本)：
        print(self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, 'Clicked popup')]").text)

























