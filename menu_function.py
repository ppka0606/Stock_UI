import os
from stockScrapy import StockScrapy
import tkinter as tk
import tkinter.messagebox
import json

import function as f
    # 补充一句,import的时候是不能用别名的,比如import tk.messagebox 就是错的


def export(stats):

    """
    将当前信息导出到用户指定的文档之中,采取追加模式
    """
    def export_to(stats, filepath):
        """
        导出到特定文件中
        """
        if not stats.success:
            tk.messagebox.showwarning("错误","未查询到有效信息,无法导出")
        else:
            try:
                with open(filepath,"a") as export_file:
                    export_file.write(stats.inf)
                    tk.messagebox.showinfo("提示","导出成功")
            except FileNotFoundError:
                tk.messagebox.showwarning("错误","未找到指定文件路径,无法导出")

    export_window = tk.Tk()
    export_window.title("导出到")
    export_window.title("导出当前信息")

    var_entry_export = tk.StringVar()
    entry_export = tk.Entry(export_window)
    entry_export.insert("end", "(在此输入导出路径:)")
    entry_export.pack()

    filepath = entry_export.get()
    export_button = tk.Button(export_window, text = "导出", width = 20, height = 2, command = lambda : export_to(stats, 
    entry_export.get()))
    export_button.pack()
    export_window.mainloop()

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
    string_get_help += '3. 您也可以在下拉菜单中选择已收藏的代码,再次使用手动输入代码查询时请取消选择下拉菜单\n'
    string_get_help += '4. 点击"查询"按钮进行查询\n'
    string_get_help += '5. 您可以在"操作"->"收藏夹"中管理常用的股票代码\n'
    string_get_help += '6. 若出现错误信息,请按照指示操作'

    tk.messagebox.showinfo(title = "使用帮助", message = string_get_help)
    # pass

def get_authority(stats):
    """
    弹出一个窗口显示作者的信息等
    """
    tk.messagebox.showinfo(title='关于程序', message='作者 : ppka0606\n版本 : 1.0')   # return 'ok'
    # pass

def add_star_stock(stats, box, listbox, star_dict):
    f.add_star(stats, listbox, star_dict)
    # pass

def manage_star_stock(stats, star_dict):
    def delete_stock(manage_listbox,star_dict):
        if tk.messagebox.askyesno(message = "确认删除?"):
            serial = manage_listbox.curselection()
            del(star_dict[manage_listbox.get(serial)[0:8]])
            manage_listbox.delete(serial)

            with open("star.json","w") as starfile:
                starfile.write(json.dumps(star_dict, indent = 1))

            tk.messagebox.showinfo(title="提示", message="删除成功,在主界面刷新后生效")
        # pass

    manage_window = tk.Tk()
    manage_window.title("收藏夹")

    manage_listbox = tk.Listbox(manage_window, height = 5, width = 25)
    manage_listbox.pack()
    for key, value in star_dict.items():
        manage_listbox.insert("end", str(key) + " " + str(value))

    manage_button = tk.Button(manage_window, text = "删除", command = lambda : delete_stock(manage_listbox, star_dict))
    manage_button.pack()

    

    manage_window.mainloop()