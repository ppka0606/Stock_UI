from stockScrapy import StockScrapy
import tkinter as tk

def return_string(stock):
    """
    按照字符串形式返回信息
    """
    diction = stock.get_information()
    s = ""
    for key,value in diction.items():
        s += (key + ":" + str(value) +" ")
        s += "\n"
    return s


