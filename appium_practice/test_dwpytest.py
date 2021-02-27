# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/19 21:25
@Auth ： wanghao
@File ：test_dwpytest.py
"""
from time import sleep

from appium import webdriver


class TestDW:

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

    def test_search(self):
        """
        1．打开雪球app
        2．点击搜索输入框
        3．向搜索输入框里面输入“阿里巴巴"
        4．在搜索结果里面选择“阿里巴巴"”，然后进行点击
        5．获取这只阿里巴巴的股价，并判断这只股价的价格>260
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price > 260

    def test_attr(self):
        """
        打开【雪球】应用首页定位首页的搜索框
        判断搜索框的是否可用,并查看搜索框name属性值
        打印搜索框这个元素的左上角坐标和它的宽高
        向搜索框输入: alibaba
        判断【阿里巴巴】是否可见
        如果可见，打印“搜索成功"点击，如果不可见，打印“搜索失败”
        :return:
        """
        ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        # 元素是否可用
        search = ele.is_enabled()
        print(ele.text)
        print(ele.location)
        print(ele.size)
        if search is True:
            ele.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
            ali = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            display = ali.get_attribute("displayed") # 判断元素是否可见
            if display == 'true':
                print("搜索成功")
            else:
                print("搜索失败")

    def test_xpath(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = self.driver.find_element_by_xpath\
            ("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(f"当前09988 的股票价格为：{current_price}")
        assert float(current_price) < 255

    def test_myinfo(self):
        """
        1、点击我的，进入到个人信息页面
        2、点击登录，进入到登陆页面
        3、输入用户名，输入密码
        4、点击登录
        :return:
        """
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("帐号密码登录")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("wanghao")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("123456")
        # 点击登录
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

        # 组合定位
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")')

        # 父子节点定位
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/title_container").childSelector(text("股票"))'
        )

        # 兄弟节点定位
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/stock_layout")'
            '.fromParent(resourceId("com.xueqiu.android:id/add_attention"))'
        )

    # 实现滚动页面查找元素
    def test_scroll(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("推荐")').click()
        user_scroll = 'new UiScrollable(new UiSelector().scrollable(true).' + \
                      'instance(0)).scrollIntoView(new UiSelector().text("胜利咖啡").instance(0))'
        self.driver.find_element_by_android_uiautomator(user_scroll)












