# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : page_order_process
# Time       ：2022/7/5 17:32
# Author     ：xiaoxia
# version    ：python 3.9
# Description：
"""
import allure
from selenium.webdriver.common.by import By

from page.page_base import PageBase


class PageOrderInfo(PageBase):
    """订单流程页面
    -财务审核
    -总经理审核
    -实时部署
    """

    """页面元素"""
    # 订单详情-财务审核提交按钮
    order_info_financial_audit_submit_button_loc = (By.XPATH,
                                                    "//div[text()='财务复核']/following-sibling::"
                                                    "form[1]//span[text()='提交']")
    # 订单详情-总经理审批提交按钮
    order_info_manager_audit_submit_button_loc = (By.XPATH,
                                                  "//div[text()='总经理审批']/following-sibling::"
                                                  "form[1]//span[text()='提交']")
    # 订单详情-实施部署选择Uey按钮
    order_info_deployment_ukey_button_loc = By.XPATH, "//input[@placeholder='请选择U-Key']"
    # 订单详情-实施部署选择Uey的下拉列表
    order_info_deployment_ukey_ul_loc = By.XPATH, "//li/span[text()='GZ006']/ancestor::ul"
    # 订单详情-实施部署选择GZ006
    order_info_deployment_ukey_li_loc = By.XPATH, "//li/span[text()='GZ006']"
    # 订单详情-实施部署提交按钮
    order_info_deployment_submit_button_loc = (By.XPATH,
                                               "//div[text()='实施部署']/following-sibling::"
                                               "form[1]//span[text()='提交']")
    # 订单详情-撤销理由输入框
    order_info_undo_text_loc = (By.XPATH,
                                "//label[text()='撤销理由']/following-sibling::"
                                "div[1]//textarea[@class='el-textarea__inner']")
    # 订单详情-撤销提交按钮
    order_info_undo_submit_button_loc = (By.XPATH, "//div[text()='撤销订单']/following-sibling::"
                                                   "form[1]//span[text()='提交']")

    """一闪而过的弹窗"""
    # 财务审核成功
    order_info_audit_success_alert_loc = By.XPATH, "//span[text()='审核成功']"
    # 撤销成功
    order_info_undo_success_alert_loc = By.XPATH, "//span[text()='撤销成功']"
    # 部署成功
    order_info_deployment_success_alert_loc = By.XPATH, "//span[text()='U-Key绑定完成']"

    """订单列表按钮"""
    # 订单列表-详情按钮
    order_info_button_loc = By.XPATH, "//span[text()=' 详情 '][1]"

    """页面操作"""
    @allure.step('点击订单列表的详情按钮')
    def click_order_info_button(self):
        self.base_click(self.order_info_button_loc)

    @allure.step('点击订单详情-财务审核提交按钮')
    def click_order_info_financial_audit_submit_button(self):
        self.base_click(self.order_info_financial_audit_submit_button_loc)

    @allure.step('点击订单详情-总经理审批提交按钮')
    def click_order_info_manager_audit_submit_button(self):
        self.base_click(self.order_info_manager_audit_submit_button_loc)

    @allure.step('订单详情-实施部署选择Uey并提交')
    def select_order_info_deployment(self):
        self.base_click(self.order_info_deployment_ukey_button_loc)
        self.base_sleep()
        self.base_ul_selector(self.order_info_deployment_ukey_ul_loc, self.order_info_deployment_ukey_li_loc)
        self.base_sleep()
        self.base_click(self.order_info_deployment_submit_button_loc)

    @allure.step('订单详情-输入撤销理由并提交')
    def order_info_undo_order(self, reason):
        self.base_input(self.order_info_undo_text_loc, reason)
        self.base_sleep()
        self.base_click(self.order_info_undo_submit_button_loc)

    def order_normal(self):
        self.base_sleep()
        self.click_order_info_button()
        self.base_sleep()
        self.click_order_info_financial_audit_submit_button()
        self.base_sleep()
        self.click_order_info_button()
        self.base_sleep()
        self.click_order_info_manager_audit_submit_button()
        self.base_sleep()
        self.click_order_info_button()
        self.base_sleep()
        self.select_order_info_deployment()

    def order_info_financial_audit_undo(self):
        self.base_sleep()
        self.click_order_info_button()
        self.order_info_undo_order('财务审批时撤销')

    def order_info_manager_audit_undo(self):
        self.base_sleep()
        self.click_order_info_button()
        self.base_sleep()
        self.click_order_info_financial_audit_submit_button()
        self.base_sleep()
        self.click_order_info_button()
        self.base_sleep()
        self.order_info_undo_order('总经理审批时撤销')


