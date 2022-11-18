# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : page_order_search
# Time       ：2022/7/6 9:51
# Author     ：xiaoxia
# version    ：python 3.9
# Description：
"""
import allure
from selenium.webdriver.common.by import By

from page.page_base import PageBase


class PageOrderSearch(PageBase):
    """订单搜索页面"""
    """页面元素"""
    # 关键字输入框
    order_search_keyword_text_loc = By.XPATH, "//input[@placeholder='单位名称、销售、电话、U-Key']"
    # 合同编号输入框
    order_search_contract_text_loc = By.XPATH, "//input[@placeholder='请输入合同号']"
    # 订单状态按钮
    order_search_order_state_button_loc = By.XPATH, "//input[@placeholder='请选择订单状态']"
    # 订单状态下拉列表
    order_search_order_state_ul_loc = By.XPATH, "//li//span[text()='财务待复核']//ancestor::ul"
    # 选择订单状态-财务待审核
    order_search_order_state_li_loc = By.XPATH, "//li//span[text()='财务待复核']"
    # 选择订单状态-销售撤回
    order_search_order_state_li_loc2 = By.XPATH, "//li//span[text()='销售撤回']"
    # 搜索按钮
    order_search_button_loc = By.XPATH, "//span[text()='搜索']"
    # 重置按钮
    order_search_reset_button_loc = By.XPATH, "//span[text()='重置']"

    """页面操作"""
    @allure.step('输入关键字')
    def input_order_search_keyword_text(self, keyword):
        self.base_input(self.order_search_keyword_text_loc, keyword)

    @allure.step('输入合同编号')
    def input_order_search_contract_text(self, contract_no):
        self.base_input(self.order_search_contract_text_loc, contract_no)

    @allure.step('选择订单状态-待审核')
    def select_order_state(self):
        self.base_sleep()
        self.base_click(self.order_search_order_state_button_loc)
        self.base_sleep()
        self.base_ul_selector(self.order_search_order_state_ul_loc, self.order_search_order_state_li_loc)

    @allure.step('选择订单状态-撤回')
    def select_order_state_undo(self):
        self.base_sleep()
        self.base_click(self.order_search_order_state_button_loc)
        self.base_sleep()
        self.base_ul_selector(self.order_search_order_state_ul_loc, self.order_search_order_state_li_loc2)

    @allure.step('点击搜索按钮')
    def click_order_search_button(self):
        self.base_click(self.order_search_button_loc)

    @allure.step('点击重置按钮')
    def click_order_reset_button(self):
        self.base_click(self.order_search_reset_button_loc)

    @allure.story('搜索订单-待审核')
    def search_order(self, contract_no):
        # self.input_order_search_keyword_text(keyword)
        self.input_order_search_contract_text(contract_no)
        # self.select_order_state()
        self.click_order_search_button()
        self.base_sleep()

    @allure.story('搜索订单-待审核')
    def search_order_undo(self, keyword, contract_no):
        self.input_order_search_keyword_text(keyword)
        self.input_order_search_contract_text(contract_no)
        self.select_order_state_undo()
        self.click_order_search_button()
        self.base_sleep()



