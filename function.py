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

def check_stock(stats, text, var_text, stock_exchange_code, entry, var_entry, listbox, radio_sh, radio_sz):
    """
    响应按钮"check"的事件
    不直接调用stockScrapy,而是在stats中间接构造
    stats:描述主程序状态,用所输入的信息进行初始化,以便于构建当前的股票信息
    text: 将结果传入到text中显示给用户
    var_text: 传入text的VarString对象,**为了程序的统一,从stats获取**
    stock_exchange_code:直接获取app.py中的变量(交易所代码)
    var_entry:从entry中获取信息并保存,提供以构造stockScrapy对象

    如果选择了listbox中的某个选项,显然就会导致,会以选项为准;当然为了好看也会将entry等中的内容更新
    """
    # print("output test")

    # print("test check")
    try:
        # 没有抛出tk.TclError则说明在listbox中有勾选选项,否则没有
        value = listbox.get(listbox.curselection())
        # 从<class 'str'> value中解析出stock_exchange_code 和 code,新建查询
        this_code = value[2:8]
        this_stock_exchange_code = 0 if value[:2] =="上证" else 1
        if this_stock_exchange_code == 0:
            radio_sh.select()
        else:
            radio_sz.select()

        temp = StockScrapy(this_stock_exchange_code, this_code)
        stats.change_stock(temp)
        entry.delete(0,"end")
        entry.insert("end", this_code)

        var_text.set(stats.inf)
        text.delete('1.0', 'end')
        text.insert("end", stats.inf)
        # text.delete('1.0', 'end')
        # text.insert("end", value + str(type(value)))
    except tk.TclError:
        var_entry = entry.get()
        code = var_entry

        temp = StockScrapy(stock_exchange_code, code)
        stats.change_stock(temp)
        
        var_text.set(stats.inf)
        text.delete('1.0', 'end')
        text.insert("end", stats.inf)


def add_star(stats, listbox, star_dict):
    """
    直接将stats中的信息导入收藏夹
    因此需要先点击"查询"更新当前的stats
    但是考虑到用户可能不知道,所以先弹窗提醒一下
    """
    # print("test add_star")
    if stats.success and tk.messagebox.askyesno(title = "提示", message = "将当前显示于消息框中的股票所对应的的代码\n添加入收藏夹"):
        star_dict[stats.exchange + str(stats.code)] = stats.name
        listbox.delete(0,"end")
        for key, value in star_dict.items():
            listbox.insert("end", key + " " + str(value))

        with open("star.json", "w") as f:
            f.write(json.dumps(star_dict, ensure_ascii=False))

    elif not stats.success:
        tk.messagebox.showwarning(title = "warning", message = "当前股票信息未查询到结果,\n无法导入收藏夹")

def refresh(listbox, star_dict):
    listbox.delete(0,"end")
    for key, value in star_dict.items():
        listbox.insert("end",key+" "+value)