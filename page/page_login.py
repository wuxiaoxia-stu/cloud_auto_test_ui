"""
登录页面
"""
import allure
from selenium.webdriver.common.by import By
from page.page_base import PageBase


# 登录页面的方法
class PageLogin(PageBase):

    """以下为登录页面的元素"""
    # 用户名输入框
    username_text_loc = By.XPATH, "//input[@placeholder='账号']"
    # 密码输入框
    password_text_loc = By.XPATH, "//input[@type='password']"
    # 登录按钮
    login_btn_loc = By.XPATH, "//button[contains(@class,' w-full mt-4')]"
    # 登录成功提示
    login_success_alert_loc = By.XPATH, "//span[text()='登陆成功']"
    # 管理员图像按钮
    administrator_image_btn_loc = By.XPATH, "//p[text()='admin']"

    # 输入账号
    @allure.step('输入账号')
    def page_input_username(self, username):
        self.base_input(self.username_text_loc, username)

    # 输入密码
    @allure.step('输入密码')
    def page_input_password(self, password):
        self.base_input(self.password_text_loc, password)

    # 点击登录
    @allure.step('点击登录')
    def page_click_login_btn(self):
        self.base_click(self.login_btn_loc)

    # 截图
    def page_get_screenshot(self):
        self.base_get_image()

    # 组装
    @allure.story('用户登录')
    def login(self, url, username, password):
        self.base_open(url)
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()
