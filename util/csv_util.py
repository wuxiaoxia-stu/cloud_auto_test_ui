import csv
import os


# 用于读取csv格式的数据文件，返回数组列表，数组的元素是字典格式
class CsvUtil:

    @staticmethod
    def dict_reader_csv(filename):
        """
        用于读取csv格式的数据文件，返回数组列表，数组的元素是字典格式
        1、路径，如果是执行run文件，filename路径为os.getcwd() + "/data/" + filename
        2、如果是单独执行某个test.py文件，路径为"../../data/" + filename
        :param args: 表头名，目前仅能支持2个参数
        :param filename: 文件名
        """
        info_list = []  # 定义空数组
        with open(os.getcwd() + "/data/" + filename, 'r', encoding='utf-8') as f:
            data = csv.DictReader(f)  # 以字典格式读取，第一行作为key
            for row in data:
                info_list.append(row)   # 追加数组元素
            print(info_list)
            return info_list

    @staticmethod
    def read_csv(filename):
        """
        用于读取csv格式的数据文件，返回数组数据
        :param filename:
        :return:
        """
        info_list = []  # 定义空数组
        # with open(os.getcwd() + "../../data/" + filename, 'r', encoding='utf-8') as f:
        with open(os.getcwd() + "/data/" + filename, 'r', encoding='utf-8') as f:
            data = csv.reader(f)
            for row in data:
                info_list.append(row)  # 追加数组元素
            # print(info_list)
            print(info_list)
            return info_list


if __name__ == '__main__':
    CsvUtil.read_csv('order_info.csv')
