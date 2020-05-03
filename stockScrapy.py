import requests
import re

# 爬虫的接口是参考了https://blog.csdn.net/Zhihua_W/article/details/78908450

class StockScrapy():
    """
    用于爬取信息的类
    """
    def __init__(self, stock_exchange_code, code):
        self.stock_exchange_code = stock_exchange_code
            # 交易所代码
        self.code = code
            # 股票代码,同样按照string传入,因为会有开头为0的状况存在
        self.stock_exchange_map = {0:"sh", 1:"sz"}
            # 用于转换交易所名称缩写
        self.url = 'https://hq.sinajs.cn/?list=' + self.stock_exchange_map[self.stock_exchange_code] + code
        # 见参考博客:新浪实时股票数据接口   http://hq.sinajs.cn/?list=code
        
        self.data={}
        self.data["股票名"] = "NULL"
        self.data["当前每股价格"] = 0.0
        self.data["今日开盘价"] = 0.0
        self.data["昨日收盘价"] = 0.0
        self.data["今日最高价"] = 0.0
        self.data["今日最低价"] = 0.0
        self.data["涨跌幅"] = "0.0%"

    def get_information(self):
        try:
            response = requests.get(self.url)
            data_list = response.text.split(",")
                # 将text内容转化至list,方便提取
            
            if response.status_code == 200 and len(data_list) > 1:
                # 正常
                self.get_data(data_list)
                return self.data
            elif len(data_list) == 1:
                # 股票名称错误
                return {"Error":"未查询到股票代码对应的股票信息"} 
            else:
                # 网络连接错误等其他情况
                return {"Error":"连接异常或其他未知错误"}
        except requests.exceptions.ConnectionError:
            return {"Error":"网络连接异常"}

    def get_data(self, data_list):
        self.data['股票名'] = data_list[0].split('"')[1]
        self.data["当前每股价格"] = float(data_list[3])
        self.data["今日开盘价"] = float(data_list[1])
        self.data["昨日收盘价"] = float(data_list[2])
        self.data["今日最低价"] = float(data_list[5])
        
        try:
            percentage = (self.data["当前每股价格"] - self.data["昨日收盘价"]) / self.data["昨日收盘价"] * 100
            self.data["涨跌幅"] = format(percentage, ".2f") +"%"
        except ZeroDivisionError:
            self.data["涨跌幅"] = "/"

# test
# x = StockScrapy(1, '000001')
# print(x.get_information())