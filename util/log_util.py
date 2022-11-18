# 导包
import logging.handlers
from time import strftime


class LogUtil:

    logger = None

    @classmethod
    def get_logger(cls):

        if cls.logger is None:
            # 获取日志器
            cls.logger = logging.getLogger()
            # 获取控制台处理器
            sh = logging.StreamHandler()
            # 设置日志器的级别
            sh.setLevel(logging.ERROR)

            # 获取文件-以时间分隔的处理器
            """
            filename:日志文件保存的目录及文件名
            when：时间单位，参考该方法的底层实现，比如D表示按天存，S按秒存
            interval：时间间隔
            backupCount：保存的日志文件数量

            """

            th = logging.handlers.TimedRotatingFileHandler(filename="./log/logtime.log",
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding='utf-8')
            # 设置日志器的级别
            th.setLevel(logging.INFO)
            # 设置格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d)] - %(message)s"
            # 添加格式器
            formatter = logging.Formatter(fmt)
            # 将格式器添加到 处理器 控制台
            sh.setFormatter(formatter)
            # 将格式器添加到 文件-以时间分隔
            th.setFormatter(formatter)
            # 将处理器添加到 日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)

        return cls.logger



