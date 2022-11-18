from selenium import webdriver


class Base:
    """基类"""
    driver = webdriver.Chrome()  # 实例化浏览器对象