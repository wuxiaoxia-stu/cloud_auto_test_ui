from util.yaml_util import YamlUtil
import pytest


@pytest.fixture(name="login_data")
def get_login_data():
    """获取url，登录账号和密码"""
    data_login = YamlUtil.read_yaml('config.yaml')['login']  # 读取登录的配置文件
    yield data_login
    # print(data_login)


@pytest.fixture(scope='function', name="new_user_data")
def get_new_user_data():
    """获取新增用户的信息"""
    new_user_data = YamlUtil.read_yaml('config.yaml')['userinfo']  # 读取登录的配置文件
    yield new_user_data
    # print(new_user_data)


# @pytest.fixture(scope='function', name="new_order_data")
# def get_new_order_data():
#     """获取新增用户的信息"""
#     new_order_data = YamlUtil.read_yaml('config.yaml')['orderinfo']  # 读取登录的配置文件
#     yield new_order_data
#     # print(new_order_data)
