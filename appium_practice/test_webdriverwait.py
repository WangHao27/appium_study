# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/24 20:34
@Auth ： wanghao
@File ：test_webdriverwait.py
"""
from appium import webdriver
from hamcrest import *
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebDriverWait:

    def setupclass(self):
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

    def teardownclass(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/name")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/title_container").childSelector(text("股票"))'
        ).click()
        # 显示等待
        locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        ele = self.driver.find_element(*locator)
        print(ele.text)
        current_price = float(ele.text)
        except_price = 242.8
        assert current_price == except_price

    def test_wait_lamda(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/name")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/title_container").childSelector(text("股票"))'
        ).click()
        # 显示等待
        locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        ele = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))
        print(ele.text)
        current_price = float(ele.text)
        except_price = 230.8
        # assert current_price == except_price
        assert_that(current_price, close_to(except_price, except_price*0.1))












































