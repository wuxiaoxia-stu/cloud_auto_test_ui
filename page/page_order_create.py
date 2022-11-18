# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : page_order_create.py
# Time       ：2022/6/30 16:03
# Author     ：xiaoxia
# version    ：python 3.9
# Description：
"""

# 创建订单页
from time import sleep

import allure
from selenium.webdriver.common.by import By
from page.page_base import PageBase


class PageOrderCreate(PageBase):

    """页面元素参数值"""
    hospital = '北京医院'  # 单位名称

    """侧栏元素"""
    authorization_management_button_loc = By.XPATH, "//span[text()='授权管理']"  # 授权管理按钮
    order_management_button_loc = By.XPATH, "//span[text()='订单管理']"  # 订单管理按钮

    """创建订单界面元素"""
    # 创建订单按钮
    create_order_button_loc = By.XPATH, "//span[text()='创建订单']"
    # 合同号输入框
    create_order_contract_number_text_loc = By.XPATH, "//label[text()='合同号']/following-sibling::div[1]//input"
    # 选择区域按钮, 通过哥哥定位弟弟
    create_order_area_button_loc = By.XPATH, "//label[text()='选择区域']/following-sibling::div//input"
    # 省份下拉列表，通过子元素定位父辈元素
    create_order_area_selector_ul_loc = By.XPATH, "(//span[text()='北京']/ancestor::ul)[2]"
    # 省份下拉列表
    create_order_area_li_loc = By.XPATH, "(//span[text()='北京'])[2]"
    # 市级下拉列表，通过子元素定位父辈元素
    create_order_area2_selector_ul_loc = By.XPATH, "//span[text()='北京市']/ancestor::ul"
    # 市级下拉列表，选择广州市
    create_order_area2_li_loc = By.XPATH, "//span[text()='北京市']"
    # 选择绑定单位按钮
    create_order_binding_hospital_button_loc = (By.XPATH,
                                                "//div[@class='el-dialog__body']//input[@placeholder='请选择授权单位']")
    # 单位下拉列表，通过子元素定位父辈
    create_order_binding_hospital_selector_ul_loc = (By.XPATH,
                                                     "(//span[text()='北京医院']/ancestor::ul)[2]")
    # 选择单位名称
    create_order_binding_hospital_li_loc = By.XPATH, "(//span[text()='北京医院'])[2]"
    # create_order_binding_hospital_li_loc = By.XPATH, "//div[14]//span[text()='" + hospital + "']"
    # 销售名称输入框
    create_order_sales_name_text_loc = By.XPATH, "//label[text()='销售']/following-sibling::div[1]//input"
    # 销售电话输入框
    create_order_sales_phone_text_loc = By.XPATH, "//label[text()='销售电话']/following-sibling::div[1]//input"
    # 单位负责人输入框
    create_order_head_name_text_loc = By.XPATH, "//label[text()='单位负责人']/following-sibling::div[1]//input"
    # 负责人电话输入框
    create_order_head_phone_text_loc = By.XPATH, "//label[text()='负责人电话']/following-sibling::div[1]//input"
    # 单位联系人输入框
    create_order_contact_name_text_loc = By.XPATH, "//label[text()='单位联系人']/following-sibling::div[1]//input"
    # 联系人电话输入框
    create_order_contact_phone_text_loc = By.XPATH, "//label[text()='联系人电话']/following-sibling::div[1]//input"
    # 收货人输入框
    create_order_consignee_text_loc = By.XPATH, "//label[text()='收货人']/following-sibling::div[1]//input"
    # 收货人电话输入框
    create_order_consignee_phone_text_loc = By.XPATH, "//label[text()='收货人电话']/following-sibling::div[1]//input"
    # 收货地址按钮
    create_order_consignee_area_button_loc = By.XPATH, "//label[text()='收货地址']/following-sibling::div//input"
    # 省份下拉列表，通过子元素定位父辈元素
    create_order_consignee_area_selector_ul_loc = By.XPATH, "(//span[text()='北京']/ancestor::ul)[3]"
    # 省份下拉列表
    create_order_consignee_area_li_loc = By.XPATH, "(//span[text()='北京'])[3]"
    # 市级下拉列表，通过子元素定位父辈元素
    create_order_consignee_area2_selector_ul_loc = By.XPATH, "(//span[text()='北京市']/ancestor::ul)[2]"
    # 市级下拉列表，选择广州市
    create_order_consignee_area2_li_loc = By.XPATH, "(//span[text()='北京市'])[2]"
    # 详细地址输入框
    create_order_consignee_address_text_loc = By.XPATH, "//label[text()='详细地址']/following-sibling::div[1]//input"
    # 提交订单按钮
    create_order_submit_button_loc = By.XPATH, "//span[text()='提交']"
    # 创建成功提示
    create_order_success_alert_loc = By.XPATH, "//span[text()='创建成功']"
    # 合同号重复,创建订单失败
    create_order_duplicate_contract_number_alert_loc = By.XPATH, "//span[text()='合同号重复']"
    # 取消按钮
    create_order_cancel_button_loc = By.XPATH, "//div[@aria-label='创建订单']//span[text()='取消']"

    """添加设备界面"""
    # 添加设备按钮
    create_order_add_device_button_loc = By.XPATH, "//i[@class ='el-icon is-icon-plus']"
    # 试用版套餐
    create_order_device_trial_button_loc = By.XPATH, "//span[text()='选择设备套餐']/ancestor::div[1]/following-sibling::div[1]//div[text()='试用版']"

    # 批量定位所有套餐类型元素，id以tab开头的所有元素
    def devices_all_loc(self):
        return self.driver.find_elements(By.XPATH, "//span[text()='选择设备套餐']/ancestor::div[1]/following-sibling::div[1]//div[starts-with(@id,'tab')]")
    # 确定按钮
    create_order_devices_ok_button_loc = By.XPATH, "//div[@aria-label='选择设备套餐']//span[text()='确定']"
    # 取消按钮
    create_order_devices_cancel_button_loc = By.XPATH, "//div[@aria-label='选择设备套餐']//span[text()='取消']"
    # 试用版套餐日期选择列表按钮
    create_order_devices_trial_date_button_loc = By.XPATH, "//div[@id='pane-9']//label[text()='选择默认月份:'][1]/following-sibling::div[1]//input"
    # 试用版套餐下拉列表
    create_order_devices_trial_date_ul_loc = By.XPATH, "//span[text()='1个月'][1]/ancestor::ul"
    # 试用版套餐日期选择1个月
    create_order_devices_trial_date_li_loc = By.XPATH, "//span[text()='1个月'][1]"
    # 试用版套餐未选择日期提示  弹窗出来的时候，按下ctrl+\键，就会暂停。
    create_order_devices_trial_fail_alert_loc = By.XPATH, "//span[text()='请至少选择一个有效期产品']"

    """页面操作-创建订单"""
    @allure.step('点击授权管理按钮')
    def click_authorization_management_button(self):
        self.base_click(self.authorization_management_button_loc)

    @allure.step('点击订单管理按钮')
    def click_order_management_button(self):
        self.base_click(self.order_management_button_loc)

    @allure.step('点击创建订单')
    def click_create_order_button(self):
        self.base_click(self.create_order_button_loc)

    @allure.step('输入合同号')
    def input_create_order_contract_number(self, contract_number):
        self.base_input(self.create_order_contract_number_text_loc, contract_number)

    @allure.step('选择区域')
    def select_create_order_area(self):
        self.base_click(self.create_order_area_button_loc)
        self.base_sleep()
        self.base_ul_selector(self.create_order_area_selector_ul_loc, self.create_order_area_li_loc)
        self.base_sleep()
        self.base_ul_selector(self.create_order_area2_selector_ul_loc, self.create_order_area2_li_loc)

    @allure.step('选择绑定单位')
    def select_create_order_binding_hospital(self):
        self.base_click(self.create_order_binding_hospital_button_loc)
        self.base_sleep()
        self.base_ul_selector(self.create_order_binding_hospital_selector_ul_loc,
                              self.create_order_binding_hospital_li_loc)

    @allure.step('输入销售姓名和销售电话')
    def input_create_order_sales_info(self, sales_name, sales_phone):
        self.base_input(self.create_order_sales_name_text_loc, sales_name)
        self.base_input(self.create_order_sales_phone_text_loc, sales_phone)

    @allure.step('输入单位负责人姓名和电话')
    def input_create_order_head_name_info(self, head_name, head_phone):
        self.base_input(self.create_order_head_name_text_loc, head_name)
        self.base_input(self.create_order_head_phone_text_loc, head_phone)

    @allure.step('输入单位联系人姓名和电话')
    def input_create_order_contact_info(self, contact_name, contact_phone):
        self.base_input(self.create_order_contact_name_text_loc, contact_name)
        self.base_input(self.create_order_contact_phone_text_loc, contact_phone)

    @allure.step('输入收货人姓名和电话')
    def input_create_order_consignee_info(self, consignee_name, consignee_phone):
        self.base_input(self.create_order_consignee_text_loc, consignee_name)
        self.base_input(self.create_order_consignee_phone_text_loc, consignee_phone)

    @allure.step('选择收货地址和输入详细地址')
    def select_create_order_consignee_area(self, consignee_address):
        self.base_click(self.create_order_consignee_area_button_loc)
        self.base_sleep()
        self.base_ul_selector(self.create_order_consignee_area_selector_ul_loc,
                              self.create_order_consignee_area_li_loc)
        self.base_sleep()
        self.base_ul_selector(self.create_order_consignee_area2_selector_ul_loc,
                              self.create_order_consignee_area2_li_loc)
        self.base_sleep()
        self.base_input(self.create_order_consignee_address_text_loc, consignee_address)

    @allure.step('点击提交按钮')
    def click_create_submit_button(self):
        self.base_click(self.create_order_submit_button_loc)

    @allure.step('点击取消按钮')
    def click_create_order_cancel_button(self):
        self.base_click(self.create_order_cancel_button_loc)

    @allure.step('添加6种不同类型的设备')
    def click_add_devices(self):
        self.base_click(self.create_order_add_device_button_loc)  # 点击添加设备+按钮
        # print(self.base_find_element(self.create_order_device_trial_button_loc))
        # print(len(self.devices_all_loc()))
        for device in self.devices_all_loc():
            self.base_sleep()
            device.click()  # 点击套餐类型按钮
            if device == self.base_find_element(self.create_order_device_trial_button_loc):
                self.base_click(self.create_order_devices_cancel_button_loc)
            else:
                # print(device)
                self.base_click(self.create_order_devices_ok_button_loc)  # 点击确定按钮
                self.base_click(self.create_order_add_device_button_loc)  # 点击添加设备+按钮

    """业务组合"""
    @allure.story('创建订单')
    def create_order(self, contract_number, sales_name, sales_phone, head_name, head_phone, contact_name, contact_phone,
                     consignee_name, consignee_phone, consignee_address):
        self.base_sleep()
        self.click_create_order_button()
        self.input_create_order_contract_number(contract_number)
        self.select_create_order_area()
        self.select_create_order_binding_hospital()
        self.input_create_order_sales_info(sales_name, sales_phone)
        self.input_create_order_head_name_info(head_name, head_phone)
        self.input_create_order_contact_info(contact_name, contact_phone)
        self.input_create_order_consignee_info(consignee_name, consignee_phone)
        self.select_create_order_consignee_area(consignee_address)
        self.click_add_devices()
        self.click_create_submit_button()
        if self.base_hover_attribute_exist(self.create_order_duplicate_contract_number_alert_loc, "合同号重复"):
            self.click_create_order_cancel_button()

