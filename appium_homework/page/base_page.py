# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/7 15:10
@Auth ： wanghao
@File ：base_page.py
"""
import yaml
from typing import Dict, List
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _params = {}
    def __init__(self, driver: WebDriver=None):
        self.driver = driver

    def find(self, by, locator=None):
        return self.driver.find_element(*by) if isinstance(by, tuple) else self.driver.find_element(by, locator)


    def swip_click(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def send(self, value, by, locator):
        self.find(by, locator).click()
        self.find(by, locator).send_keys(value)

    def parse_action(self, path, func_name):
        global element, value
        with open(path, 'r', encoding="utf-8") as f:
            function = yaml.safe_load(f)
            steps: List[Dict] = function[func_name]
        for step in steps:
            if "by" in step.keys():
                element = self.find(step['by'], step['locator'])
            if "action" in step.keys():
                if "click" == step["action"]:
                    element.click()
                if "send" == step["action"]:
                    content: str = step["value"]
                    for param in self._params:
                        content = content.replace("{%s}" % param, self._params[param])
                    self.send(content, step['by'], step['locator'])



