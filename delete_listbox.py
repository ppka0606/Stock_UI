
import tkinter as tk
 
master = tk.Tk()
 
# 创建一个空列表
listbox = tk.Listbox(master)
listbox.pack()
 
# 往列表里添加数据
for item in ["鸡蛋", "鸭蛋", "鹅蛋", "李狗蛋"]:
        listbox.insert("end", item)
        
theButton = tk.Button(master, text="删除", command=lambda x=listbox: x.delete("active"))
theButton.pack()

master.mainloop()