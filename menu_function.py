import os
from stockScrapy import StockScrapy
import tkinter as tk
import tkinter.messagebox
    # 补充一句,import的时候是不能用别名的,比如import tk.messagebox 就是错的
def export(stats):
    """
    将当前信息导出到用户指定的文档之中,采取追加模式
    """
    export_window = tk.Tk()
    export_window.title("导出当前信息")
    export_window.geometry("400x320")
    export_window.mainloop()
    pass

def exit_program(stats):
    """
    退出程序
    """
    os._exit(0)

def get_help(stats):
    """
    新建一个窗口显示使用说明
    """
    string_get_help = ""
    string_get_help += '1. 在主界面的下方选择交易所(目前只支持上海证券交易所和深圳证券交易所)\n'
    string_get_help += '2. 在输入框中输入股票代码\n'
    string_get_help += '3. 点击"查询"按钮进行查询\n'
    string_get_help += '4. 您可以在"操作"->"收藏夹"中管理常用的股票代码\n'
    string_get_help += '5. 若出现错误信息,请按照指示操作'

    tk.messagebox.showinfo(title = "使用帮助", message = string_get_help)
    # pass

def get_authority(stats):
    """
    弹出一个窗口显示作者的信息等
    """
    tk.messagebox.showinfo(title='关于程序', message='作者 : ppka0606\n版本 : 1.0')   # return 'ok'
    # pass

def add_star_stock(stats):
    pass

def manage_star_stock(stats):
    pass