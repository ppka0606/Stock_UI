from stockScrapy import StockScrapy
import tkinter as tk
from function import return_string

class Stats():
    """
    定义一个追踪运行时状态的类
    """

    def __init__(self, stock = None):
        self.stock = stock
        self.inf = None
        self.get_inf()

        self.success = False
        self.exchange = None
        self.code = None
        self.name = None

    def change_stock(self, stock = None):
        self.stock = stock
        self.get_inf()
        
        if "股票名" in self.inf:
            self.success = True
            self.code = self.stock.code
            self.exchange = "上证" if self.stock.stock_exchange_code == 0 else "深证"
            self.name = self.stock.data['股票名']
    
    def get_inf(self):
        if not self.stock is None:
            self.inf = return_string(self.stock)
        else:
            self.inf = "未输入需要查找的股票代码"

    