from stockScrapy import StockScrapy
import tkinter as tk
import json

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
    # print("output test")
    print("test check")
    var_entry = entry.get()
    code = var_entry

    temp = StockScrapy(stock_exchange_code, code)
    stats.change_stock(temp)
    
    var_text.set(stats.inf)
    text.delete('1.0', 'end')
    text.insert("end", stats.inf)

def add_star(stats, set_listbox, listbox, star_dict):
    """
    直接将stats中的信息导入收藏夹
    因此需要先点击"查询"更新当前的stats
    但是考虑到用户可能不知道,所以先弹窗提醒一下
    """
    print("test add_star")
    if stats.success and tk.messagebox.askyesno(title = "提示", message = "将当前显示于消息框中的股票所对应的的代码\n添加入收藏夹"):
        set_listbox.add(stats.exchange + str(stats.code) + " " + stats.name)
        star_dict[stats.exchange + str(stats.code)] = stats.name
        listbox.delete(0,"end")
        for i in set_listbox:
            listbox.insert("end", i)

        with open("star.json", "w") as f:
            f.write(json.dumps(star_dict))