# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : test_03_order
# Time       ：2022/7/1 11:37
# Author     ：xiaoxia
# version    ：python 3.9
# Description：
"""
import allure
import pytest

from cases.base import Base
from page.page_order_create import PageOrderCreate
from page.page_order_delete import PageOrderDelete
from page.page_order_info import PageOrderInfo
from page.page_order_search import PageOrderSearch
from page.page_order_upgrade import PageOrderUpgrade
from util.csv_util import CsvUtil
from util.yaml_util import YamlUtil


@allure.epic('云端服务管理系统')
@allure.feature('授权管理-订单管理模块')
@allure.severity(allure.severity_level.CRITICAL)
class TestOrder(Base):

    @classmethod
    def setup_class(cls):
        cls.order_create_page = PageOrderCreate(cls.driver)   # 实例化PageOrderCreate
        cls.order_info_page = PageOrderInfo(cls.driver)  # 实例化PageOrderProcess
        cls.order_search_page = PageOrderSearch(cls.driver)  # 实例化PageOrderSearch
        cls.order_upgrade_page = PageOrderUpgrade(cls.driver)
        cls.order_delete_page = PageOrderDelete(cls.driver)
        cls.order_create_page.click_authorization_management_button()  # 点击授权管理按钮
        cls.order_create_page.base_sleep()
        cls.order_create_page.click_order_management_button()  # 点击订单管理按钮

    # @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.parametrize('order_info', CsvUtil.read_csv('order_info.csv'))
    @pytest.mark.parametrize('order_info', CsvUtil.dict_reader_csv('order_info_1.csv'))
    @allure.story('创建订单')
    @allure.title('01用例-创建订单-财务审批前撤销-删除订单')
    def test_01_order_financial_audit_undo(self, order_info):
        """01用例-创建订单-搜索订单-财务审批前撤销-删除订单"""
        # self.order_create_page.create_order(*order_info)
        self.order_create_page.create_order(order_info['contract_number'], order_info['sales_name'],
                                            order_info['sales_name'], order_info['head_name'],
                                            order_info['head_phone'], order_info['contact_name'],
                                            order_info['contact_phone'], order_info['consignee_name'],
                                            order_info['consignee_phone'], order_info['consignee_address'])
        self.order_search_page.search_order(order_info['contract_number'])
        self.order_info_page.order_info_financial_audit_undo()
        self.order_delete_page.order_delete()
        self.order_search_page.click_order_reset_button()
        assert self.order_info_page.base_hover_attribute_exist(self.order_info_page.order_info_undo_success_alert_loc, '撤销成功')

    # @allure.severity(allure.severity_level.NORMAL)
    @allure.story('创建订单')
    @allure.title('02用例-创建订单-总经理审批时撤销-删除订单')
    @pytest.mark.parametrize('order_info', CsvUtil.dict_reader_csv('order_info_1.csv'))
    def test_02_order_manager_audit_undo(self, order_info):
        """02用例-创建订单-搜索订单-总经理审核前撤销-删除订单"""
        # self.order_create_page.create_order(*order_info)
        self.order_create_page.create_order(order_info['contract_number'], order_info['sales_name'],
                                            order_info['sales_name'], order_info['head_name'],
                                            order_info['head_phone'], order_info['contact_name'],
                                            order_info['contact_phone'], order_info['consignee_name'],
                                            order_info['consignee_phone'], order_info['consignee_address'])
        self.order_search_page.search_order(order_info['contract_number'])
        self.order_info_page.order_info_manager_audit_undo()
        self.order_delete_page.order_delete()
        self.order_search_page.click_order_reset_button()
        assert self.order_info_page.base_hover_attribute_exist(self.order_info_page.order_info_undo_success_alert_loc,
                                                                  '撤销成功')

    # @allure.severity(allure.severity_level.NORMAL)
    @allure.story('创建订单')
    @allure.title('03用例-创建订单-正常订单流程')
    @pytest.mark.parametrize('order_info', CsvUtil.read_csv('order_info.csv'))
    def test_03_order_normal(self, order_info):
        """03用例-创建订单-搜索订单-财务审核通过-总经理审核通过-实时部署"""
        # print(order_info)
        # print(*order_info)
        self.order_create_page.create_order(*order_info)
        # self.order_create_page.create_order(order_info['contract_number'], order_info['sales_name'],
        #                                     order_info['sales_name'], order_info['head_name'],
        #                                     order_info['head_phone'], order_info['contact_name'],
        #                                     order_info['contact_phone'], order_info['consignee_name'],
        #                                     order_info['consignee_phone'], order_info['consignee_address'])
        self.order_search_page.search_order(order_info[0])
        self.order_info_page.order_normal()
        assert self.order_info_page.base_hover_attribute_exist(self.order_info_page.
                                                               order_info_deployment_success_alert_loc, 'U-Key绑定完成')

    @allure.story('升级订单')
    @allure.title('04用例-升级订单')
    @pytest.mark.parametrize('order_info', CsvUtil.dict_reader_csv('order_upgrade.csv'))
    def test_04_order_upgrade(self, order_info):
        """04用例-搜索订单-升级订单-搜索订单-审核订单"""
        self.order_search_page.input_order_search_contract_text(order_info['search_contract_number'])
        self.order_search_page.click_order_search_button()
        self.order_search_page.base_sleep()
        self.order_upgrade_page.order_upgrade_device(order_info['contract_number'], order_info['sales_name'], order_info['sales_phone'])
        self.order_search_page.base_sleep()
        self.order_search_page.input_order_search_contract_text(order_info['contract_number'])
        self.order_search_page.click_order_search_button()
        self.order_info_page.order_normal()
        self.order_search_page.base_sleep()
        assert self.order_info_page.base_hover_attribute_exist(self.order_info_page.
                                                               order_info_deployment_success_alert_loc, 'U-Key绑定完成')

    @allure.story('删除订单')
    @allure.title('05用例-删除订单-合同编号为{order_info}')
    @pytest.mark.parametrize('order_info', CsvUtil.read_csv('order_delete.csv'))
    def test_05_order_delete(self, order_info):
        """
        05用例-搜索订单-删除订单
        """
        self.order_search_page.input_order_search_contract_text(order_info)
        self.order_search_page.click_order_search_button()
        self.order_delete_page.order_delete()
        assert self.order_delete_page.base_hover_attribute_exist(self.order_delete_page.order_delete_success_alert_loc, '删除成功')

    @classmethod
    def teardown_class(cls):
        # cls.driver.quit()
        pass

