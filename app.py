from stockScrapy import StockScrapy
import tkinter as tk

import function as f
import menu_function as mf

window = tk.Tk()

window.title("股票查询")
window.geometry("800x640")

label_welcome = tk.Label(window, text = "欢迎使用股票信息查询工具", font=('Arial', 12), width = 30, height = 2)
label_welcome.pack()

menubar = tk.Menu(window)

opreation_menu = tk.Menu(menubar, tearoff = 0)
help_menu = tk.Menu(menubar, tearoff = 0)

menubar.add_cascade(label = "操作", menu = opreation_menu)
menubar.add_cascade(label = "帮助", menu = help_menu)

# 统一形式起见,command均采用lambda表达式传递
opreation_menu.add_command(label = "导出", command = lambda : mf.export())
    # 添加一个处理收藏夹的子菜单
star_stock_menu = tk.Menu(opreation_menu, tearoff = 0)
opreation_menu.add_cascade(label = "收藏夹", menu = star_stock_menu)
star_stock_menu.add_command(label = "添加当前股票进收藏夹",command = lambda : mf.add_star_stock())
star_stock_menu.add_command(label = "管理收藏夹", command = lambda : mf.manage_star_stock())
opreation_menu.add_command(label = "退出", command = lambda : mf.exit_program())


help_menu.add_command(label = "使用说明", command = lambda : mf.get_help())
help_menu.add_command(label = "关于程序", command = lambda : mf.get_authority())

window.config(menu = menubar)

window.mainloop()