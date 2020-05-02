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

    def change_stock(stock = None):
        self.stock = stock
        self.get_inf()

    def get_inf(self):
        if not self.stock is None:
            self.inf = return_string(stock)
        else:
            self.inf = "未输入需要查找的股票代码"

    