# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : order_upgrade_page
# Time       ：2022/7/11 18:30
# Author     ：xiaoxia
# version    ：python 3.9
# Description：
"""
import allure
from selenium.webdriver.common.by import By

from page.page_base import PageBase


class PageOrderUpgrade(PageBase):
    """ 订单升级页"""
    # 订单列表的升级按钮
    order_upgrade_button_loc = By.XPATH, "//span[text()=' 升级 '][1]"
    # 合同号输入框
    order_upgrade_contract_number_text_loc = (By.XPATH, "//div[text()='基本信息']"
                                                        "//ancestor::div[1]//label[text()='合同号']"
                                                        "/following-sibling::div[1]//input")
    # 销售名称输入框
    order_upgrade_sales_name_text_loc = (By.XPATH, "//div[text()='基本信息']"
                                                   "//ancestor::div[1]//label[text()='销售']"
                                                   "/following-sibling::div[1]//input")
    # 销售电话输入框
    order_upgrade_sales_phone_text_loc = (By.XPATH, "//div[text()='基本信息']"
                                                    "//ancestor::div[1]//label[text()='销售电话']"
                                                    "/following-sibling::div[1]//input")
    # 提交按钮
    order_upgrade_submit_button_loc = By.XPATH, "//div[@aria-label='订单升级']//span[text()='提交']"

    # 合同号重复,创建订单失败
    order_upgrade_duplicate_contract_number_alert_loc = By.XPATH, "//span[text()='合同号重复']"
    # 取消按钮
    order_upgrade_cancel_button_loc = By.XPATH, "//div[@aria-label='订单升级']//span[text()='取消']"

    # 批量定位设备信息的元素，id以tab开头的所有元素
    def order_upgrade_devices_info_loc(self):
        return self.driver.find_elements(By.XPATH, "//div[contains(text(),'设备信息')]/following-sibling::div[1]//div[starts-with(@id,'tab')]")

    # 批量定位所有套餐类型元素，id以tab开头的所有元素
    def order_upgrade_devices_select_loc(self):
        return self.driver.find_elements(By.XPATH,
                                         "//span[text()='选择设备套餐']/ancestor::div[1]/following-sibling::div[1]//div[starts-with(@id,'tab')]")

    """设备信息页中的元素"""
    # PUS设备按钮
    order_upgrade_device_info_PUS_button_loc = By.XPATH, "//div[contains(text(),'设备信息')]/following-sibling::div[1]//div[@id='tab-0']"
    # 点击升级此设备按钮
    order_upgrade_device_info_upgrade_button_loc = By.XPATH, "//span[text()='点击升级此设备'][1]"

    """选择升级套餐页的元素"""
    # PUS S300设备按钮
    order_upgrade_devices_select_PUSS300_button_loc = (By.XPATH,
                                         "//span[text()='选择设备套餐']/ancestor::div[1]/following-sibling::div[1]//div[@id='tab-8']")
    # 确定按钮
    order_upgrade_devices_select_ok_button_loc = By.XPATH, "//div[@aria-label='选择设备套餐']//span[text()='确定']"



    """页面操作"""
    @allure.step('点击订单列表的升级按钮')
    def click_order_upgrade_button(self):
        self.base_click(self.order_upgrade_button_loc)

    @allure.step('输入合同号')
    def input_order_upgrade_contract_number_text(self, contract_number):
        self.base_input(self.order_upgrade_contract_number_text_loc, contract_number)

    @allure.step('输入销售名称')
    def input_order_upgrade_sales_info_text(self, sales_name, sales_phone):
        self.base_input(self.order_upgrade_sales_name_text_loc, sales_name)
        self.base_input(self.order_upgrade_sales_phone_text_loc, sales_phone)

    @allure.step('点击提交按钮')
    def click_order_upgrade_submit_button(self):
        self.base_click(self.order_upgrade_submit_button_loc)

    @allure.step('点击取消按钮')
    def click_order_upgrade_cancel_button(self):
        self.base_click(self.order_upgrade_cancel_button_loc)

    @allure.step('点击设备信息页中的PUS按钮')
    def click_order_upgrade_device_info_PUS_button(self):
        self.base_click(self.order_upgrade_device_info_PUS_button_loc)

    @allure.step('点击升级此设备按钮')
    def click_order_upgrade_device_info_upgrade_button(self):
        self.base_click(self.order_upgrade_device_info_upgrade_button_loc)

    @allure.step('点击选择设备套餐中的PUSS300按钮')
    def click_order_upgrade_devices_select_PUSS300_button(self):
        self.base_click(self.order_upgrade_devices_select_PUSS300_button_loc)

    @allure.step('点击确定按钮')
    def click_order_upgrade_devices_select_ok_button(self):
        self.base_click(self.order_upgrade_devices_select_ok_button_loc)

    # 业务组合
    def order_upgrade_device(self, contract_number, sales_name, sales_phone):
        self.click_order_upgrade_button()
        self.base_sleep()
        self.input_order_upgrade_contract_number_text(contract_number)
        self.input_order_upgrade_sales_info_text(sales_name, sales_phone)
        self.base_sleep()
        self.click_order_upgrade_device_info_PUS_button()
        self.click_order_upgrade_device_info_upgrade_button()
        self.base_sleep()
        self.click_order_upgrade_devices_select_PUSS300_button()
        self.base_sleep()
        self.click_order_upgrade_devices_select_ok_button()
        self.base_sleep()
        self.click_order_upgrade_submit_button()
        if self.base_hover_attribute_exist(self.order_upgrade_duplicate_contract_number_alert_loc, "合同号重复"):
            self.click_order_upgrade_cancel_button()
