"""
用户管理页面
"""
from time import sleep

import allure

from page.page_base import PageBase
from selenium.webdriver.common.by import By


class UserManagementPage(PageBase):
    """页面元素"""

    """页面元素 参数值"""
    role = '超级管理员'  # 角色
    department = '产品研发中心'  # 部门
    job = '测试工程师'  # 职位

    """侧栏界面"""
    system_management_button_loc = By.XPATH, "//span[text()='系统管理']"  # 系统管理按钮
    user_management_button_loc = By.XPATH, "//span[text()='用户管理']"  # 用户管理按钮

    """添加用户弹窗元素"""
    new_user_button_loc = By.XPATH, "//span[text()='新增用户']"  # 新增用户按钮
    username_text_loc = By.XPATH, "//label[text()='用户名']/following-sibling::div[1]//input"  # 用户名输入框,通过哥哥定位弟弟,再取当前节点中的input元素
    password_text_loc = By.XPATH, "//label[text()='密码']/following-sibling::div[1]//input"  # 密码输入框,通过哥哥定位弟弟
    role_button_loc = By.XPATH,  "//input[@placeholder='请选择角色']"  # 角色按钮
    # role_selector_ul_loc = By.XPATH, "//span[text()='管理员']/ancestor::ul"  # 角色选择下拉列表，通过子元素定位父辈元素
    role_selector_ul_loc = By.XPATH, "//span[text()='" + role + "']" + '/ancestor::ul'  # 角色选择下拉列表，通过子元素定位父辈元素
    role_admin_li_loc = By.XPATH, "//span[text()='" + role + "']"  # 角色选项，选择管理员
    department_button_loc = By.XPATH, "//label[text() ='部门']/following-sibling::div[1]//input"   # 部门选择按钮，通过哥哥定位弟弟
    # department_ul_selector_loc = By.XPATH, "//span[text()='产品研发中心']/ancestor::ul"  # 部门下拉列表，通过子元素定位父辈元素
    department_ul_selector_loc = By.XPATH, "//span[text()='" + department + "']" + '/ancestor::ul'  # 部门下拉列表，通过子元素定位父辈元素
    department_product_li_loc = By.XPATH, "//span[text()='" + department + "']"   # 部门选项，选择产品研发中心
    # department_product_li_loc = By.XPATH, "//li[@id ='cascader-menu-520-0-1119']"   # 部门选项，选择产品研发中心
    department_job_selector_ul_loc = By.XPATH, "//span[text()='" + job + "']" + '/ancestor::ul'  # 职位下拉列表，通过子元素定位父辈元素
    department_job_li_loc = By.XPATH, "//span[text()='" + job + "']"  # 职位选项，选择测试工程师
    email_text_loc = By.XPATH, "//label[text()='邮箱']/following-sibling::div[1]//input"  # 邮箱输入框，通过哥哥定位弟弟
    phone_text_loc = By.XPATH, "//label[text()='手机号']/following-sibling::div[1]//input"  # 手机号输入框，通过哥哥定位弟弟
    submit_button_loc = By.XPATH, "//span[text()='提交']"  # 提交按钮
    adduser_success_alert_loc = By.XPATH, "//span[text()='添加成功']"  # 添加用户成功提示弹窗

    """搜索相关元素"""
    search_username_text_loc = By.XPATH, "//input[@placeholder='请输入用户名称']"  # 搜索条件---用户名输入框
    search_state_button_loc = By.XPATH, "//input[@placeholder='请选择状态']"  # 搜索条件--状态按钮
    search_state_selector_ul_loc = By.XPATH, "//li/span[text()='已开启']/ancestor::ul"  # 通过状态下拉选项（子元素）定位父辈元素ul
    search_state_open_li_loc = By.XPATH, "//li/span[text()='已开启']"  # 状态下拉选项--已开启
    search_button_loc = By.XPATH, "//span[text()='搜索']"  # 搜索按钮
    reset_button_loc = By.XPATH, "//span[text()='重置']"  # 重置按钮

    """编辑界面元素"""
    edit_button_loc = By.XPATH, "//span[text()=' 修改 ']['0']"  # 修改按钮
    edit_password_text_loc = By.XPATH, "//label[text()='密码']/following-sibling::div//input"  # 密码输入框
    edit_role_button_loc = By.XPATH, "//input[@placeholder='请选择角色']"  # 请选择角色按钮
    edit_role_selector_ul_loc = By.XPATH, "//span[text()='管理员']/ancestor::ul"  # 角色选择下拉列表，通过子元素定位父辈元素
    edit_role_admin_li_loc = By.XPATH, "//span[text()='管理员']"  # 角色选项，选择管理员
    edit_submit_button_loc = By.XPATH, "//span[text()='提交']"  # 提交按钮
    edit_user_success_alert_loc = By.XPATH, "//span[text()='编辑成功']"  # 编辑用户成功的提示弹窗

    """删除界面元素"""
    delete_button_loc = By.XPATH, "//span[text()=' 删除 ']"  # 删除按钮
    delete_ok_button_loc = By.XPATH,  "//span[text()='确定']"  # 确定按钮
    delete_success_alert_loc = By.XPATH, "//span[text()='删除成功']"  # 删除成功弹窗提示

    """页面操作--新增用户"""
    @allure.step('点击系统管理按钮')
    def click_system_management_button(self):
        self.base_click(self.system_management_button_loc)  # 点击系统管理按钮

    @allure.step('点击用户管理按钮')
    def click_user_management_button(self):
        self.base_click(self.user_management_button_loc)  # 点击用户管理按钮

    @allure.step('点击新增用户按钮')
    def click_new_user_button(self):
        self.base_click(self.new_user_button_loc)  # 点击新增用户按钮

    @allure.step('输入用户名')
    def input_username(self, username):
        self.base_input(self.username_text_loc, username)  # 输入用户名

    @allure.step('输入密码')
    def input_password(self, password):
        self.base_input(self.password_text_loc, password)  # 输入密码

    @allure.step('选择角色')
    def select_role(self):
        self.base_click(self.role_button_loc)  # 点击请选择角色按钮
        sleep(1)
        self.base_ul_selector(self.role_selector_ul_loc, self.role_admin_li_loc)  # 选择管理员角色

    @allure.step('选择部门')
    def select_department(self):
        self.base_click(self.department_button_loc)  # 点击部门按钮
        sleep(1)
        self.base_ul_selector(self.department_ul_selector_loc, self.department_product_li_loc)  # 选择部门--研发中心
        sleep(1)
        self.base_ul_selector(self.department_job_selector_ul_loc, self.department_job_li_loc)  # 选择职位--测试工程师

    @allure.step('输入邮箱')
    def input_email(self, email):
        self.base_input(self.email_text_loc, email)  # 输入邮箱

    @allure.step('输入手机号')
    def input_phone(self, phone):
        self.base_input(self.password_text_loc, phone)  # 输入手机号

    @allure.step('点击提交按钮')
    def click_submit_button(self):
        self.base_click(self.submit_button_loc)  # 点击提交按钮

    """页面操作--编辑用户"""
    @allure.step('点击修改按钮')
    def click_edit_button(self):
        self.base_click(self.edit_button_loc)  # 点击修改按钮

    @allure.step('输入密码')
    def input_edit_password(self, password):
        self.base_input(self.edit_password_text_loc, password)  # 输入密码

    @allure.step('选择角色')
    def select_role_edit(self):
        self.base_click(self.edit_role_button_loc)  # 点击角色按钮
        sleep(2)
        self.base_ul_selector(self.edit_role_selector_ul_loc, self.edit_role_admin_li_loc)  # 选择角色-管理员

    @allure.step('点击提交')
    def click_edit_submit_button(self):
        self.base_click(self.edit_submit_button_loc)  # 点击提交

    """页面操作--查询用户"""
    @allure.step('输入用户名')
    def input_search_username(self, text):
        self.base_input(self.search_username_text_loc, value=text)  # 输入用户名

    @allure.step('选择用户状态')
    def select_state(self):
        self.base_click(self.search_state_button_loc)  # 点击状态按钮，弹出下拉列表
        sleep(2)
        self.base_ul_selector(self.search_state_selector_ul_loc, self.search_state_open_li_loc)  # 选择状态

    @allure.step('点击搜索按钮')
    def click_search_button(self):
        self.base_click(self.search_button_loc)  # 点击搜索按钮

    @allure.step('点击重置按钮')
    def click_reset_button(self):
        self.base_click(self.reset_button_loc)  # 点击重置按钮

    """业务操作--删除用户"""
    @allure.step('点击删除按钮')
    def click_delete_button(self):
        self.base_click(self.delete_button_loc)     # 点击删除按钮

    @allure.step('点击确定按钮')
    def click_delete_ok_button(self):
        self.base_click(self.delete_ok_button_loc)      # 点击确定按钮

    # 业务组合
    # 新增用户
    def add_user(self, username, password, email, phone):
        self.click_system_management_button()
        sleep(1)
        self.click_user_management_button()
        self.click_new_user_button()
        sleep(1)
        self.input_username(username=username)
        self.input_password(password=password)
        sleep(2)
        self.select_role()
        self.select_department()
        self.input_email(email=email)
        self.input_phone(phone=phone)
        self.click_submit_button()

    # 查询用户
    @allure.story('查询用户')
    def search_user(self, username):
        self.input_search_username(username)
        self.select_state()
        self.click_search_button()
        sleep(1)
        # self.click_reset_button()

    # 编辑用户信息
    @allure.story('编辑用户信息')
    def edit_user(self, password):
        self.click_edit_button()
        self.input_edit_password(password)
        self.select_role_edit()
        self.click_edit_submit_button()

    # 删除用户
    @allure.story('删除用户')
    def delete_user(self):
        self.click_delete_button()
        self.click_delete_ok_button()



