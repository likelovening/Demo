#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
##签章认证
import tkinter as tk
from tkinter.simpledialog import askstring, askinteger, askfloat
from selenium import webdriver
from selenium.webdriver.common.by import By   #导入By模块以便与使用查找使用元素
import time
from selenium.webdriver.common.action_chains import ActionChains   #导入鼠标滑动，点击等库
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from xpinyin import Pinyin
import unittest
import threading
from pytesseract import pytesseract
import os
from PIL import Image
from PIL import ImageEnhance
import logging
class main_tk():
    def __init__(self,master):
        self.init=master
        self.init.title("粮达自动测试系统")  # 设置窗口标题
        self.init.geometry('480x500+10+10')  # 设置窗口大小，默认打开位置
        self.init.attributes("-alpha", 1.0)  # 设置窗口虚化程度
        main_login(self.init)

class main_login():
    def __init__(self,master):
        global init_text
        self.master=master
        self.initwidow=tk.Frame(self.master,height="726", width="1024")
        self.initwidow.pack()
        init_window_label=tk.Label(self.initwidow,text='登录名：',bd=8)  #设置标签
        init_window_label.place(relx=0.24,rely=0.3)          #grid设置标签所在位置

        result_window_label=tk.Label(self.initwidow,text='密码：',bd=6)  #设置标签名称
        result_window_label.place(relx=0.245,rely=0.38)        #设置标签所在位置,sticky设置标签靠近属性

        var_name=tk.StringVar()
        self.init_username=tk.Entry(self.initwidow,textvariable=var_name)       #设置单行输入框:Entry
        self.init_username.place(relx=0.38,rely=0.305,height=30,width=180)

        var_password=tk.StringVar()
        self.init_password=tk.Entry(self.initwidow,textvariable=var_password)
        self.init_password.place(relx=0.38,rely=0.38,height=30,width=180)

        init_windwo_button=tk.Button(self.initwidow,text="    登录     ",command=self.user_login_check)
        init_windwo_button.place(relx=0.48,rely=0.45,height=35,width=60)

        tk.Label(self.initwidow, text="状态信息").place(relx=0.01, rely=0.55)
        self.init_text1 = tk.Text(self.initwidow, width=65, height=10)
        self.init_text1.place(relx=0.01, rely=0.6)

    def user_login_check(self):
        global user_name,user_psw
        user_name = self.init_username.get()
        user_psw = self.init_password.get()
        if user_name == "ldw":
            if user_psw == "ldw123456":
                self.write_log1("登陆中，请稍后...")
                # 跳转界面
                self.initwidow.destroy()
                functions_tab(self.master)
            else:
                self.write_log1("密码错误")
        else:
            self.write_log1("用户名错误")
    def write_log1(self,logmsg):
        global Log_num
        Log_num = 0
        logmsg_ini=str(logmsg) +""+"\n"  #换行
        if Log_num<=9:
            self.init_text1.insert(tk.END,logmsg_ini)
            Log_num=Log_num+1
        else:
            self.init_text1.delete(1.0,2.0)
            self.init_text1.insert(tk.END,logmsg_ini)

class functions_tab():
    def __init__(self,master):
        self.master=master
        self.init=tk.Frame(self.master,height="726", width="1024")
        self.init.pack()
        self.setup()
    def setup(self):
        box2=login_pc()
        Button_1=tk.Button(self.init,text="创建寄售可行性报告",command=lambda :box2.thread_it(box2.login1))
        Button_1.place(relx=0.03, rely=0.05)
        Button_2 = tk.Button(self.init, text="创建购销可行性报告")
        Button_2.place(relx=0.03, rely=0.12)

class login_pc():
    def thread_it(self, func):
        t = threading.Thread(target=func)
        t.setDaemon(True)
        t.start()
    def QZ_phonenumber(self):
        global phone_numbers
        try:
        # 获取签章手机号
            t_phone_number=tk.Tk()
        #创建的窗口在点击后就消失
            t_phone_number.withdraw()
        #使用askstring方法创建临时窗口
            phone_numbers = askstring(parent=t_phone_number,title='标题', prompt="请输入签章手机号")
            print("签章认证手机号为：%s" % phone_numbers)
        #将窗口销毁
            t_phone_number.destroy()
        except:
            print("手机号码获取失败，请重试")
            self.QZ_phonenumber()
        return int(phone_numbers)
    # 输入验证码
    def QZ_phoneYZM(self):
        global phone_YZM
        try:
            t_phone_check = tk.Tk()
            t_phone_check.withdraw()
            phone_YZM = askstring(parent=t_phone_check, title='标题', prompt="请输入签章验证码")
            print("签章验证码为：%s" % phone_YZM)
            t_phone_check.destroy()
        except:
            print("签章验证码输入错误")
            self.QZ_phoneYZM()
        return int(phone_YZM)

    def login1(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        # 设置全局响应时间
        driver.implicitly_wait(10)
        # 设置最大屏幕尺寸打开
        driver.maximize_window()
        driver.get("http://test.liangdawang.com:8085/portal/")
        driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/div/div[1]/span/span[2]/a[1]").click()
        time.sleep(1)
        driver.find_element_by_class_name("ant-input").send_keys("1020")
        time.sleep(1)
        # xpath寻找密码框，并输入
        driver.find_element_by_xpath("//input[contains(@placeholder,'密码')]").clear()
        driver.find_element_by_xpath("//input[contains(@placeholder,'密码')]").send_keys("123456")
        # xpath点击登陆按钮
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]/button").click()
        # 点击我得粮达
        time.sleep(0.5)
        # 点击弹框去认证
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]").click()
        # 点击跳转签章认证界面
        driver.find_element_by_xpath('/html/body/div[7]/div/table/tbody/tr[2]/td/div/div/div/div/div[2]/a[1]').click()
        # 滑动进度条
        renzheng_window = driver.window_handles
        driver.switch_to.window(renzheng_window[-1])
        time.sleep(20)
        agree_xy = driver.find_element_by_xpath('/html/body/div[1]/div[3]/p[43]')
        driver.execute_script("arguments[0].scrollIntoView();", agree_xy)
        # 点击同意并继续
        driver.find_element_by_xpath('/html/body/div[1]/div[4]/span').click()
        # 同意协议并开始认证
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[5]/a').click()
        except:
            # 点击同意协议
            driver.find_element_by_xpath('//*[@id="readAgree"]').click()
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[5]/a').click()
        # 进入签章选择界面
        QZ_XZ = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/p').text
        if QZ_XZ == "以下方式通过一种即可":
            print("进入签章选择界面成功")
        else:
            print("进入签章界面失败")
            driver.find_element_by_xpath('//*[@id="readAgree"]').click()
            driver.find_element_by_xpath('//*[@id="startCert"]').click()
        # 选择手机认证
        driver.find_element_by_xpath('//*[@id="phoneVerification"]').click()
        #输入签章手机号码
        driver.find_element_by_xpath('/html/body/div[1]/div/div/form/ul/li/div[3]/div/input').send_keys(
            login_pc.QZ_phoneYZM)
        #点击验证码
        driver.find_element_by_xpath('/html/body/div[1]/div/div/form/ul/li/div[3]/div/a').click()
        time.sleep(10)
        #输入验证码
        driver.find_element_by_xpath('/html/body/div[1]/div/div/form/ul/li/div[4]/div/input').send_keys(phone_YZM)
        # 点击提交
        driver.find_element_by_xpath('/html/body/div[1]/div/div/form/ul/div/a').click()





if __name__=="__main__":
    ini=tk.Tk()   #实例化一个父窗口
    main_tk(ini)
    ini.mainloop()                  #父窗口事件循环，即保持窗口运行



