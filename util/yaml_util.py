#!usr/bin.env/ python3

import os
import yaml


class YamlUtil:
    __instance = None  # 实例对象

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            print("YamlUtil first init")
            cls.__instance = super(YamlUtil, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    @staticmethod
    def read_yaml(filename):
        """
        读取yaml文件
        """
        with open(os.getcwd() + '/data/' + filename, 'r', encoding='utf-8') as f:
            r_data = yaml.load(f, Loader=yaml.FullLoader)
            # print(data)
        return r_data

    @staticmethod
    def write_yaml(filename, w_data):
        """存储数据到YAML的方法"""
        with open(os.getcwd() + '/data/' + filename, 'w', encoding='utf-8') as f:
            yaml.dump(w_data, f, Dumper=yaml.SafeDumper)  # 可选BaseDumper、SafeDumper

#
# if __name__ == '__main__':
#     data = YamlUtil().read_yaml('xxxx.yml')
#     print(data)
