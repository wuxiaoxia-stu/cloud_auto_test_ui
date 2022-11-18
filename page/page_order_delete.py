# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : page_order_delete
# Time       ：2022/7/12 16:14
# Author     ：xiaoxia
# version    ：python 3.9
# Description：
"""
import allure
from selenium.webdriver.common.by import By

from page.page_base import PageBase


class PageOrderDelete(PageBase):
    """删除订单页面"""

    # 页面元素
    # 删除订单按钮
    order_delete_button_loc = By.XPATH, "//span[text()=' 删除 '][1]"
    # 确定按钮
    order_delete_ok_button_loc = By.XPATH, "//div[text()=' 是否确认删除?']/following-sibling::div//span[text()='确定']"
    # 取消按钮
    order_delete_cancel_button_loc = By, "//div[text()=' 是否确认删除?']/following-sibling::div//span[text()='取消']"
    # 删除成功弹窗提示
    order_delete_success_alert_loc = By.XPATH, "//span[text()='删除成功']"

    # 页面操作
    @allure.step('点击订单列表的删除按钮')
    def click_order_delete_button(self):
        self.base_click(self.order_delete_button_loc)

    @allure.step('点击确定删除')
    def click_order_delete_ok_button(self):
        self.base_click(self.order_delete_ok_button_loc)

    def order_delete(self):
        self.base_sleep()
        self.click_order_delete_button()
        self.base_sleep()
        self.click_order_delete_ok_button()
