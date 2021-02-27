# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/22 19:54
@Auth ： wanghao
@File ：test_touchaction.py
"""

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction



class TestTouchAction:
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

    def test_touchaction(self):
        action = TouchAction(self.driver)
        # 获取当前屏幕的尺寸
        window_size = self.driver.get_window_size()
        width = window_size['width']
        height = window_size['height']
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        # 在当前屏幕滑动
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()


class TestTouchAction2:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "6.0"
        caps["deviceName"] = "MIX_2"
        caps["appPackage"] = "cn.kmob.screenfingermovelock"
        caps["appActivity"] = "com.samsung.ui.MainActivity"
        caps["resetKeyboard"] = True  # 将键盘重置为其原始状态
        caps["noReset"] = True  # 保留上一次操作信息
        caps["dontStopAppOnReset"] = True  # 首次启动时，不停止app
        caps["skipDeviceInitialization"] = True  # 跳过设备初始化，如安装，权限等操作
        caps["unicodeKeyboard"] = True  # 解决无法输入中文问题
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    # 手势密码解锁
    def test_touchaction_unlock(self):
        """
        1.press方法中的坐标为绝对坐标，move_to方法中的坐标都是相对坐标，
            具体来说第一个move_to中的坐标相对于press方法中的坐标，
            第二个move_to方法中的坐标相对于第一个move_to方法中的坐标。
        2.wait是必须的：这里ms表示为毫秒，ms=100就是等待100毫秒。不用的话太快会出错
        """
        action = TouchAction(self.driver)
        action.press(x=120, y=175).wait(200)\
            .move_to(x=240, y=0).wait(200)\
            .move_to(x=240, y=0).wait(200)\
            .move_to(x=-240, y=245).wait(200)\
            .move_to(x=-240, y=245).wait(200)\
            .release().wait(200).perform()




















