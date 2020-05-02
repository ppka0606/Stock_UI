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

def check_stock(stats, text, var_text, stock_exchange_code, entry, var_entry):
    """
    响应按钮"check"的事件
    不直接调用stockScrapy,而是在stats中间接构造
    stats:描述主程序状态,用所输入的信息进行初始化,以便于构建当前的股票信息
    text: 将结果传入到text中显示给用户
    var_text: 传入text的VarString对象,**为了程序的统一,从stats获取**
    stock_exchange_code:直接获取app.py中的变量(交易所代码)
    var_entry:从entry中获取信息并保存,提供以构造stockScrapy对象
    """
    pass


