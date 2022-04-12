#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
from tkinter import *
import  time
def get_time():
    current_time=time.strftime("%Y-%m-%d %H-%M-%S")
    c_time.configure(text=current_time)     #更新标签中内容
    init_window.after(1000, get_time)       #每隔1秒，调用一次原函数

init_window=Tk()
init_window.title("时钟")
#init_window.geometry("240x240")
c_time=Label(init_window,text="",fg="green",font=("黑体，12"))
c_time.pack()
get_time()
init_window.mainloop()







