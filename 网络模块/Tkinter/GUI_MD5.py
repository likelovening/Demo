#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
from tkinter import *
import hashlib
import time
Log_num=0
class MD55:
    def __init__(self,init_window_name):
        self.init_window_name=init_window_name
    def set_init_window(self):
        init_name=self.init_window_name
        init_name.title("MD5转换")
        init_name.geometry("1068x680+10+10")
        #标签类（Label）
        self.init_data_label=Label(init_name,text="待处理数据",font=("黑体",12))
        self.init_data_label.grid(row=0,column=0,sticky='W')

        self.result_data_label=Label(init_name,text="已处理数据",font=("黑体",12))
        self.result_data_label.grid(row=0,column=12,sticky='W')

        self.init_log_label=Label(init_name,text="日志",font=("黑体",12))
        self.init_log_label.grid(row=11,column=0,sticky='W')

        #多行文本输入（Text）
        self.init_text=Text(init_name,width=67,height=35)
        self.init_text.grid(row=1,column=0,rowspan=10,columnspan=10)

        self.result_text=Text(init_name,width=70,height=49)
        self.result_text.grid(row=1,column=12,rowspan=15,columnspan=10)

        self.log_text=Text(init_name,width=67,height=9)
        self.log_text.grid(row=12,column=0,columnspan=10,sticky='W')

        #按钮（Button）：定义按钮时，使用command=functionname这个函数指定；
        #当按钮被点击时，调用command后的方法，从而完成事件的触发。
        self.init_button=Button(init_name,text="字符串转MD5",width=10,bg="green",command=self.str_trans_to_md5)
        self.init_button.grid(row=1,column=10)

#MD5转换函数：从文本框中读取待处理数据--逻辑处理--界面结果文本结果
    def str_trans_to_md5(self):
        src=self.init_text.get(1.0,END).strip().replace("/n","").encode()
        if src:
            try:
                mgMD5=hashlib.md5()
                mgMD5.update(src)
                mgMD5_Digest=mgMD5.hexdigest()
                #输出
                self.result_text.delete(1.0,END)  #输入前清理框内所有数据
                self.result_text.insert(1.0,mgMD5_Digest)  #insert插入结果文本框，从第一行开始
                self.write_log("INFO:MD5 转换成功")
            except:
                self.result_text.delete(1.0,END)
                self.result_text.insert(1.0,"字符串转换失败")
        else:
            self.write_log("Error")
#获取即时时间
    def get_current_time(self):
        current_time=time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(time.time()))
        return current_time
#获取日志
    def write_log(self,logmsg):
        global Log_num
        current_time=self.get_current_time()
        logmsg_in=str(current_time)+""+str(logmsg) +""+"\n"  #换行
        if Log_num<=9:
            self.log_text.insert(END,logmsg_in)
            Log_num=Log_num+1
        else:
            self.log_text.delete(1.0,2.0)
            self.log_text.insert(END,logmsg_in)

def gui_start():
    init_window=Tk()
    Get_start=MD55(init_window)
    Get_start.set_init_window()
    init_window.mainloop()

gui_start()

