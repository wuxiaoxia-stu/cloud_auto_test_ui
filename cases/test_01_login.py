# 导包
from cases.base import Base
from page.page_login import PageLogin
import allure


@allure.epic('云端服务管理系统')
@allure.feature('登录模块')
@allure.severity(allure.severity_level.CRITICAL)
class TestLogin(Base):

    @classmethod
    def setup_class(cls):

        # 实例化获取页面对象 PageLogin
        cls.page_login = PageLogin(cls.driver)
        # cls.data_login = YamlUtil().read_yaml('config.yaml')['login']  # 读取登录的配置文件

    # 用例：管理员登录
    # @pytest.mark.parametrize('url, username, password', get_data())
    # @pytest.mark.parametrize('data_login',data_login)
    @allure.story('用户登录')
    @allure.title('01用例-用户正常登录')
    def test_login(self, login_data):
        """01-管理员登录用例"""
        url = login_data['url']
        username = login_data['username']
        password = login_data['password']
        self.page_login.login(url, username, password)
        assert self.page_login.base_hover_attribute_exist(self.page_login.login_success_alert_loc, '登陆成功')

    def teardown_class(self):
        # self.driver.quit()
        pass

# if __name__ == '__main__':
#
#     pytest.main(['-s', 'test_01_login.py'])
