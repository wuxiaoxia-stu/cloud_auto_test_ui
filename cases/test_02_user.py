import time

import allure
import pytest

from cases.base import Base
from page.page_user_management import UserManagementPage


@allure.epic('云端服务管理系统')
@allure.feature('系统管理-用户管理模块')
@allure.severity(allure.severity_level.CRITICAL)
class TestUserManagement(Base):

    current_time = time.strftime('%y%m%d%H%M%S')  # 获取当前时间

    @classmethod
    def setup_class(cls):
        cls.page = UserManagementPage(cls.driver)  # 实例化

    @allure.story('添加用户')
    @allure.title('01-添加用户')
    def test_01_adduser(self, new_user_data):
        """01-新增用户用例"""
        username = new_user_data['username'] + self.current_time
        password = new_user_data['password'] + self.current_time
        email = new_user_data['email']
        phone = new_user_data['phone']
        self.page.add_user(username, password, email, phone)
        assert self.page.base_hover_attribute_exist(self.page.adduser_success_alert_loc, '添加成功')

    @allure.story('搜索用户')
    @allure.title('02-搜索用户')
    def test_02_search_user(self, new_user_data):
        """02-搜索用户用例"""
        username = new_user_data['username']
        self.page.search_user(username)

    @allure.story('编辑用户')
    @allure.title('03-编辑用户')
    def test_03_edit_user(self, new_user_data):
        """03-编辑用户用例"""
        password = new_user_data['password'] + self.current_time
        self.page.edit_user(password)
        assert self.page.base_hover_attribute_exist(self.page.edit_user_success_alert_loc, '编辑成功')

    @allure.story('删除用户')
    @allure.title('04-删除用户')
    def test_04_delete_user(self):
        """04-删除用户用例"""
        self.page.delete_user()
        assert self.page.base_hover_attribute_exist(self.page.delete_success_alert_loc, '删除成功')

    @classmethod
    def teardown_class(cls):
        # cls.driver.close()
        pass
