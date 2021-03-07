# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/27 18:10
@Auth ： wanghao
@File ：base_page.py
"""
from typing import List, Dict

import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _black_list = [(By.ID, "image_cancel")]
    _error_cont = 0
    _error_max = 10
    _params = {}
    # 指定driver类型，后续可直接调用相关方法
    def __init__(self, driver: WebDriver=None):
        self.driver = driver

    def find(self, by, locator=None):
        try:
            # 如果by为元组则采用*by,否则（by, loccator）
            ele = self.driver.find_element(*by) if isinstance(by, tuple) else self.driver.find_element(by, locator)
            self.error_cont = 0
            return ele
        # 在查找元素时对弹窗进行处理，出现弹窗时遍历元素进行点击消除
        except Exception as e:
            self.error_cont += 1
            # 设定最大查找次数，防止死循环
            if self.error_cont >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self.driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(by, locator)
            raise e

    def send(self, value, by, locator=None):
        try:
            self.find(by, locator).send_keys(value)
            self.error_cont = 0
        except Exception as e:
            self.error_cont += 1
            # 设定最大查找次数，防止死循环
            if self.error_cont >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self.driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.send(value, by, locator)
            raise e


    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            # 指定参数类型，便于后续调用相关方法
            steps: List[Dict] = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step['by'], step['locator'])
                if "action" in step.keys():
                    if "click" == step["action"]:
                        element.click()
                    if "send" == step["action"]:
                        # {value}
                        content:str = step["value"]
                        """
                        遍历_params字典，如果字典中的key值命中yaml中的value,
                        则将_params字典中key为value对应的值替换yaml中的value
                        """
                        for param in self._params:
                            content = content.replace("{%s}" % param, self._params[param])
                        self.send(content, step['by'], step['locator'])

















