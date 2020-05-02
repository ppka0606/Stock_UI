from stockScrapy import StockScrapy
from stats import Stats
import tkinter as tk

import function as f
import menu_function as mf


window = tk.Tk()
stats = Stats()

# 标题栏
window.title("股票查询")
window.resizable(0,0) #防止用户调整尺寸
# window.geometry("500x400")


# label_welcome = tk.Label(window, text = "欢迎使用股票信息查询工具", font=('Arial', 12), width = 40, height = 2)
# label_welcome.pack()

# 导航栏

menubar = tk.Menu(window)

opreation_menu = tk.Menu(menubar, tearoff = 0)
help_menu = tk.Menu(menubar, tearoff = 0)

menubar.add_cascade(label = "操作", menu = opreation_menu)
menubar.add_cascade(label = "帮助", menu = help_menu)

# 统一形式起见,command均采用lambda表达式传递
opreation_menu.add_command(label = "导出", command = lambda : mf.export(stats))
    # 添加一个处理收藏夹的子菜单
star_stock_menu = tk.Menu(opreation_menu, tearoff = 0)
opreation_menu.add_cascade(label = "收藏夹", menu = star_stock_menu)
star_stock_menu.add_command(label = "添加当前股票进收藏夹", command = lambda : mf.add_star_stock(stats))
star_stock_menu.add_command(label = "管理收藏夹", command = lambda : mf.manage_star_stock(stats))
opreation_menu.add_command(label = "退出", command = lambda : mf.exit_program(stats))


help_menu.add_command(label = "使用说明", command = lambda : mf.get_help(stats))
help_menu.add_command(label = "关于程序", command = lambda : mf.get_authority(stats))

window.config(menu = menubar)

# 先做右下角和左上角定位,以及空白部分的填充
label_author = tk.Label(window, text = "  @ppka0606")
label_author.grid(row = 11, column = 7)

label_version = tk.Label(window, text = "          ")
label_version.grid(row = 0, column = 0)

# 输入序号栏
var_entry = tk.StringVar()
entry = tk.Entry(window, width = 40, textvariable = var_entry)
entry.insert("end","(在此输入股票代码)")
entry.grid(row = 1, column = 2, columnspan = 4)

# 下拉菜单
set_listbox = set()
var_listbox = tk.StringVar()
listbox = tk.Listbox(window, height = 3, width = 40, listvariable = var_listbox)
listbox.insert("end", "暂无收藏股票序号     ")
listbox.grid(row = 3, column = 2, columnspan = 4)

# 插入一个空行显得好看一点
empty = tk.Label(window, height = 1)
empty.grid(row = 4)

# 文本框
text = tk.Text(window, height = 7, width = 40)
var_text = tk.StringVar()
text.insert("end",r'输入股票代码并选择交易所后点击"查询"按钮开始查询')
text.configure(state = 'disabled')
text.grid(row = 5, rowspan = 2, column = 2, columnspan = 4)

# 选择项
stock_exchange_code = -1
radio_sh = tk.Radiobutton(window, text = "上证", variable = stock_exchange_code, value = 0)
radio_sz = tk.Radiobutton(window, text = "深证", variable = stock_exchange_code, value = 1)
radio_sh.grid(row = 8, column = 1)
radio_sz.grid(row = 9, column = 1)

# "查询"按钮
button_check = tk.Button(window, text = "查询", width = 10, height = 2)
button_check.grid(row = 8, rowspan = 2,column = 3)
button_check.bind(lambda : f.check_stock(stats, text, var_text, stock_exchange_code, entry, var_entry))

# "收藏"按钮
button_star = tk.Button(window, text = "收藏", width = 10, height = 2)
button_star.grid(row = 8, rowspan = 2, column = 5)

window.mainloop()