# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/18 22:49
@Auth ： wanghao
@File ：test_dingwei.py
"""
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "6.0"
caps["deviceName"] = "MIX_2"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["resetKeyboard"] = True # 将键盘重置为其原始状态
caps["noReset"] = True  # 保留上一次操作信息
caps["dontStopAppOnReset"] = True  # 首次启动时，不停止app
caps["skipDeviceInitialization"] = True  # 跳过设备初始化，如安装，权限等操作
caps["unicodeKeyboard"] = True  # 解决无法输入中文问题
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
# 隐式等待
driver.implicitly_wait(10)
# 搜索
driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
# ele = WebDriverWait(driver,10,0.2).until("元素")
driver.back()  # 回到上一页
driver.quit()
