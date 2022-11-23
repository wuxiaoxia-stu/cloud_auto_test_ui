"""
公共方法模块：Base
"""
import time
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from util.log_util import LogUtil


class PageBase:
    """基本方法管理类"""

    # 初始化
    def __init__(self, driver):
        # 虚拟driver
        self.driver = driver

    # 输出日志
    @staticmethod
    def write_log(message, level='info'):
        log = LogUtil.get_logger()  # 由于get_logger()函数是类函数，所以不需要实例化类即可调用
        # 设置控制台日志器的级别
        if level == 'debug':
            log.debug(message)
        elif level == 'info':
            log.info(message)
        elif level == 'warning':
            log.warning(message)
        elif level == 'error':
            log.error(message)
        elif level == 'critical':
            log.critical(message)

    # 打开URL
    def base_open(self, url):
        # 最大化
        self.driver.maximize_window()
        # 打开url
        self.driver.get(url)

    # 查找元素方法（提供：点击，输入，获取文本）使用
    def base_find_element(self, loc, timeout=30, poll=0.5):
        # 使用显示等待
        """
        :param loc: 元素的配置信息，格式为元组，如:password_text_loc = By.name, "password"
        :param timeout:默认超时时间为30，可以通过传入参数进行修改
        :param poll:默认访问频率0.5秒
        :return:查找到的元素
        """
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        # 获取元素并进行点击
        try:
            self.base_find_element(loc).click()
        except:
            pass

    # 输入文本方法
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find_element(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 获取文本方法
    def base_get_text(self, loc):
        # 切记：一定要返回元素的文本信息
        return self.base_find_element(loc).text

    # 判断元素是否存在
    def base_element_is_exist(self, loc):
        try:
            self.base_find_element(loc, timeout=2)
            return True  # 代表元素存在
        except:
            return False  # 代表元素不存在

    # select下拉框
    def base_select(self, loc, text):
        sel = Select(self.base_find_element(loc))
        sel.select_by_visible_text(text)

    # 非select下拉框
    def base_ul_selector(self, ul_loc, li_loc):
        # self.base_click(ul_loc)  # 定位到下拉列表
        self.base_click(li_loc)  # 定位到下拉列表选项

    # 判断闪退提示窗体新是否含有属性attribute,值value
    def base_hover_attribute_exist(self, loc, value):
        try:
            el = self.base_find_element(loc, timeout=1)  # 定位闪退窗口
            ActionChains(self.driver).move_to_element(el).perform()  # 鼠标悬浮在该窗口
            val = el.text  # 获取弹窗文本值
            # print(val)
            if val == value:
                return True
            else:
                return False
        except:
            # print('expect')
            return False

    # 截图方法
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d_%H_%M_%S")))

    # sleep
    @staticmethod
    def base_sleep(s_time=1):
        sleep(s_time)

