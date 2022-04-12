#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
import tkinter as tk
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
import pytest
import os
from PIL import Image
from PIL import ImageEnhance
from tkinter.simpledialog import askstring
Log_num=0
class Test_main_tk():
    def __init__(self,master):
        self.init=master
        self.init.title("粮达自动测试系统")  # 设置窗口标题
        self.init.geometry('480x500+10+10')  # 设置窗口大小，默认打开位置
        self.init.attributes("-alpha", 1.0)  # 设置窗口虚化程度
        Test_main_login(self.init)

class Test_main_login():
    def __init__(self,master):
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
        global init_text
        bos=jishou_check()
        box1=seal
        Button_1=tk.Button(self.init,text="创建寄售可行性报告",command=lambda :bos.thread_it(bos.jishou))
        Button_1.place(relx=0.03, rely=0.05)

        Button_2 = tk.Button(self.init, text="创建购销可行性报告")
        Button_2.place(relx=0.03, rely=0.12)

        init_windwon_button = tk.Button(self.init, text="请输入签章认证手机号", command=box1.phone_number)
        init_windwon_button.place(relx=0.3, rely=0.05, height=35, width=160)

        tk.Label(self.init, text="状态信息").place(relx=0.01, rely=0.55)
        init_text = tk.Text(self.init, width=65, height=10)
        init_text.place(relx=0.01, rely=0.6)

class jishou_check(unittest.TestCase):
        #添加线程
        def thread_it(self,func,):
            t=threading.Thread(target=func)
            t.setDaemon(True)
            t.start()
        #寄售主操作函数
        def jishou(self):
            global G_name,driver
            bss=log_input()   #调用log函数
            bss.write_log("开始创建寄售可行性报告....")
            self.driver = webdriver.Chrome()
            driver = self.driver
            # 设置全局响应时间
            driver.implicitly_wait(10)
            # 设置最大屏幕尺寸打开
            driver.maximize_window()
            driver.get("http://test.liangdawang.com:8085/portal/")
            bss.write_log("业务员登陆中....")
            # xpath寻找“请登录”按钮
            driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/div/div[1]/span/span[2]/a[1]").click()
            time.sleep(1)
            # xpath寻找账户框，并输入
            driver.find_element_by_class_name("ant-input").send_keys("ldwywy")
            time.sleep(1)
            # xpath寻找密码框，并输入
            driver.find_element_by_xpath("//input[contains(@placeholder,'密码')]").send_keys("123456")
            # xpath点击登陆按钮
            driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]/button").click()
            time.sleep(1)
            bss.write_log("业务员登陆成功")
            # 点击我得粮达
            driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div/div[2]/ul/li[2]/a').click()
            time.sleep(1)
            new_window = driver.window_handles
            driver.switch_to.window(new_window[1])
            # 选择我得粮达
            driver.find_element_by_xpath('/html/body/div[3]/div/ul/li[1]/a').click()
            # 选择寄售报告填写
            driver.find_element_by_xpath('//*[@id="MENU0105"]').click()
            bss.write_log("寄售可行性报告填写中...")
            # 点击委托方信息公司并选择
            driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[2]/form/div[1]/div[2]/div[1]/a/span[1]').click()
            # 选择某一家公司
            elem = driver.find_element_by_xpath('/html/body/div[9]/ul/li[17]/div')
            G_name=elem.text
            Title1 = ("%s：自动化可行性报告" % elem.text)
            #bss.write_log("客户名称：%s"%elem)
            ActionChains(driver).move_to_element(elem).click().perform()
            # 选择品名
            chose_yumi = driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[4]/div[2]/ul/li[1]')
            chose_yumi1 = driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[4]/div[2]/ul/li[1]/p/a')
            ActionChains(driver).move_to_element(chose_yumi).click(chose_yumi1).perform()
            # 填写数量
            driver.find_element_by_xpath(
                "/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[6]/input").send_keys("2000")
            # 滚动滑动条
            ActionChains(driver).key_down(Keys.DOWN).perform()
            # 选择年份
            driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[8]/select').click()
            time.sleep(0.5)
            driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[8]/select/option[2]').click()
            # 滚动滑动条
            ActionChains(driver).key_down(Keys.DOWN).perform()
            # 填写产地
            driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[11]/div[1]/div[1]/div').click()
            time.sleep(0.5)
            Chandi = driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[11]/div[1]/div[2]/div/div[2]/ul/li[10]/a')
            ActionChains(driver).move_to_element(Chandi).click().perform()
            # 滚动滑动条
            ActionChains(driver).key_down(Keys.DOWN).perform()
            # 填写单价
            driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[13]/input').send_keys('1400')
            # 价格类型
            driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[14]/select').click()
            time.sleep(0.5)
            driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[14]/select/option[2]').click()
            # 滚动滑动条
            ActionChains(driver).key_down(Keys.DOWN).perform()
            # 自办理完毕
            driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[16]/select').click()
            time.sleep(0.5)
            Huoquan = driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[16]/select/option[1]')
            ActionChains(driver).move_to_element(Huoquan).click().perform()
            # 滚动滑动条到填写交易信息界面
            elem1 = driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[2]/form/div[2]/div[6]/div[25]/textarea')
            driver.execute_script("arguments[0].scrollIntoView();", elem1)
            # 选择交易类型
            driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[3]/p/span/input[2]').click()
            # 选择天数
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[5]/select[1]').click()
            time.sleep(0.5)
            driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[5]/select[1]/option[3]').click()
            # 选择操作服务费
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[8]/input').clear()
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[8]/input').send_keys(2)
            # 滚动滑动条
            ActionChains(driver).key_down(Keys.DOWN).perform()
            # 确认标题
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[2]/input[3]').click()
            time.sleep(0.5)
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[2]/input[1]').clear()
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[2]/input[1]').send_keys(
                Title1)
            # 保证金比例
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[11]/input').send_keys(10)
            # 选择运输方式
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[12]/select').click()
            driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[2]/form/div[3]/div[12]/select/option[2]').click()
            # 滚动滑动条
            ActionChains(driver).key_down(Keys.DOWN).perform()
            # 选择大区
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[5]/div[4]/select').click()
            time.sleep(0.5)
            driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[2]/form/div[5]/div[4]/select/option[4]').click()
            # 发起人大区
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[5]/div[3]/select').click()
            time.sleep(0.5)
            driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[2]/form/div[5]/div[3]/select/option[4]').click()
            # 滚动滑动条
            time.sleep(0.5)
            ActionChains(driver).key_down(Keys.DOWN).perform()
            # 到达大区
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[5]/div[5]/select').click()
            time.sleep(0.5)
            driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[2]/form/div[5]/div[5]/select/option[4]').click()
            # 发布&确认
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[6]/input[2]').click()
            time.sleep(2)
            # 点击提交
            driver.find_element_by_class_name('szBut').click()
            time.sleep(2)
            # 点击确认
            driver.find_element_by_class_name('ui-dialog-button-orange').click()
            # assert "可行性报告操作成功" in driver.page_source
            record1 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/h1')
            Equal1 = record1.text
            self.assertEqual(Equal1, "可行性报告操作成功", '可行性报告创建失败')
            bss.write_log("可行性报告创建成功")
            # 返回可行性报告管理
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/h3/a').click()
            # 查看审批人
            time.sleep(3)
            bss.write_log("获取审批人中...")
            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[1]/span[4]/span').click()
            BpmRen = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[1]/span[4]/div/table/tbody/tr/td[2]')
            self.BpmMZ = BpmRen.text
            bss.write_log("审批人:%s"% self.BpmMZ)
            p = Pinyin()
            useN = p.get_pinyin(self.BpmMZ, '')
            pws = "123456"
            # 打开Bpm审批界面,新界面
            js = "window.open('https://test.bas.liangdawang.com:8086/bas/page/login/login.html?url=aHR0cHM6Ly90ZXN0LmJhcy5saWFuZ2Rhd2FuZy5jb206ODA4Ni9iYXMvcGFnZS9pbmRleC9pbmRleC5odG1sP2ZpcnN0PWY=')"
            driver.execute_script(js)
            # 记录当前句柄
            bpm_windows = driver.window_handles
            driver.switch_to.window(bpm_windows[-1])
            # 输入审批人账户密码并登陆
            bss.write_log("进入BPM审批界面中...")
            driver.find_element_by_xpath('/html/body/div/form/div/p[1]/input').clear()
            driver.find_element_by_xpath('/html/body/div/form/div/p[1]/input').send_keys(useN)
            driver.find_element_by_xpath('/html/body/div/form/div/p[2]/input').clear()
            driver.find_element_by_xpath('/html/body/div/form/div/p[2]/input').send_keys(pws)
            driver.find_element_by_xpath('/html/body/div/form/div/div[1]/a').click()
            # 选择审批项
            #driver.find_element_by_xpath('/html/body/div/div[3]/ul/li[1]/a/div/div').click()
            driver.execute_script("arguments[0].click();",driver.find_element_by_xpath('/html/body/div/div[3]/ul/li[1]/a/div/div'))
            driver.find_element_by_xpath('/html/body/div/div[3]/ul/li[1]/div[2]/a[1]/div').click()
            # 确认标题是否一致
            BpmTitle = driver.find_element_by_xpath('/html/body/ul[1]/a/li/span/p[1]/span').text
            if BpmTitle == Title1:
                bss.write_log("寻找审批项成功")
            else:
                bss.write_log("审批项有误")

            # 选择需审批项
            driver.find_element_by_xpath('/html/body/ul[1]/a').click()
            time.sleep(0.5)
            # 提交审批
            driver.find_element_by_xpath('//*[@id="checkOpt"]/span').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="beYes"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="checkSubmit"]').click()
            # 审批弹窗处理
            alert1 = driver.switch_to.alert
            alert1.accept()
            bss.write_log('可行性报告审批完成')
            # 确认是这个报告
            driver.switch_to.window(bpm_windows[1])
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/a[1]').click()  # 刷新报告状态
            time.sleep(1)
            self.Title2 = driver.find_element_by_xpath(
                "/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[1]/div/div[1]/a[1]").text
            bss.write_log("可行性报告名称：%s"%self.Title2)
            self.assertEqual(self.Title2, Title1, '不是这个可行性报告')
            # 确认报告状态
            BaogaoZT = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[4]/span').text
            self.assertEqual(BaogaoZT, '物流方案待补充', '报告状态有误')
            bss.write_log("确认可行性报告审批成功")
            # 切换账户
            time.sleep(1)
            wuliuyuan = driver.find_element_by_xpath('/html/body/div[1]/div/div/ul[2]/li/a/span')
            out1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/ul[2]/li/div/p/a')
            ActionChains(driver).move_to_element(wuliuyuan).click(out1).perform()
            # 登陆物流员
            bss.write_log("切换物流员登陆中....")
            driver.find_element_by_class_name("ant-input").clear()
            driver.find_element_by_class_name("ant-input").send_keys("ldwwly")
            time.sleep(1)
            # xpath寻找密码框，并输入
            driver.find_element_by_xpath("//input[contains(@placeholder,'密码')]").clear()
            driver.find_element_by_xpath("//input[contains(@placeholder,'密码')]").send_keys("123456")
            # xpath点击登陆按钮
            driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]/button").click()
            # 点击我得粮达
            time.sleep(0.5)
            driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div/div[2]/ul/li[2]/a').click()
            time.sleep(1)
            new_window2 = driver.window_handles
            driver.switch_to.window(new_window2[-1])
            bss.write_log("物流员登陆完成")
            # 选择我得粮达
            driver.find_element_by_xpath('/html/body/div[3]/div/ul/li[1]/a').click()
            # 选择可行性报告管理
            time.sleep(0.5)
            driver.find_element_by_xpath('//*[@id="MENU0107"]').click()
            # 核对报告名称
            time.sleep(1)
            WLMC = driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[1]/div/div[1]/a[1]').text
            self.assertEqual(WLMC, Title1, "物流：可行性报告选择有误")
            # 补充物流信息
            bss.write_log("寻找可行性报告并添加物流信息中....")
            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[5]/div/a').click()
            new_window3 = driver.window_handles
            driver.switch_to.window(new_window3[-1])
            # 物流方案填写
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[1]/div[2]/select').click()
            driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[2]/form/div[1]/div[2]/select/option[3]').click()
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[1]/div[3]/input').send_keys(
                '测试1')
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[1]/div[5]/input').send_keys(
                '测试2')
            # 物流方案保存
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/form/div[2]/input[2]').click()
            time.sleep(0.5)
            driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div/div/div/div[2]/a').click()
            time.sleep(0.5)
            driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[2]/div[2]/div[1]/a').click()
            # 校验是否物流方案是否提交成功
            WLFA = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/h1').text
            self.assertEqual(WLFA, "物流信息操作成功", "物流信息填写有误")
            bss.write_log("物流方案填写成功")
            # 返回可行性报告列表界面
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/h3/a').click()
            # 查看物流信息审批人
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[1]/span[4]/span').click()
            self.WLBpmRY = driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div[5]/div[1]/div[1]/span[4]/div/table/tbody/tr[1]/td[2]').text
            useW = p.get_pinyin(self.WLBpmRY, '')
            bss.write_log('物流审批人为：%s' % self.WLBpmRY)
            # 跳转BPM界面
            bss.write_log("跳转BPM审批中....")
            driver.switch_to.window(bpm_windows[-1])
            time.sleep(0.5)
            driver.find_element_by_xpath('/html/body/div/div[1]/span[1]/a/img').click()
            time.sleep(0.5)
            driver.find_element_by_xpath('/html/body/div/div[1]/span[1]/a/img').click()
            # 弹框确认
            alert2 = driver.switch_to.alert
            alert2.accept()
            # BPM账户输入切换
            driver.find_element_by_xpath('/html/body/div/form/div/p[1]/input').clear()
            driver.find_element_by_xpath('/html/body/div/form/div/p[1]/input').send_keys(useW)
            driver.find_element_by_xpath('/html/body/div/form/div/p[2]/input').clear()
            driver.find_element_by_xpath('/html/body/div/form/div/p[2]/input').send_keys(pws)
            # 点击登陆
            driver.find_element_by_xpath('/html/body/div/form/div/div[1]/a').click()
            bss.write_log("BPM切换用户登陆完成")
            # 选择审批项
            driver.find_element_by_xpath('/html/body/div/div[3]/ul/li[1]/a/div/div').click()
            time.sleep(0.5)
            driver.find_element_by_xpath('/html/body/div/div[3]/ul/li[2]/div[2]/a[1]/div').click()
            # 确认标题是否一致
            BpmTitle2 = driver.find_element_by_xpath('/html/body/ul[1]/a[1]/li/span/p[1]/span').text
            if BpmTitle2 == Title1:
                pass
            else:
                bss.write_log("审批项有误")
            bss.write_log("确认审批项....")
            # 选择需审批项
            driver.find_element_by_xpath('/html/body/ul[1]/a[1]/li/span/p[3]').click()
            time.sleep(0.5)
            # 提交审批
            driver.find_element_by_xpath('/html/body/div/div[4]/div[3]/a[2]/span').click()
            driver.find_element_by_xpath('/html/body/div/div[2]/button[1]').click()
            driver.find_element_by_xpath('/html/body/div/div[4]/button').click()
            # 审批弹窗处理
            alert3 = driver.switch_to.alert
            alert3.accept()
            bss.write_log('物理方案审批完成')
            # 切换界面
            new_window4 = driver.window_handles
            driver.switch_to.window(new_window4[-1])
            # 刷新可行性报告状态
            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/a[1]').click()
            time.sleep(1)
            WLZT = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[4]/span').text
            self.assertEqual(WLZT, "可行性报告待提交", "物流审批有误")
            bss.write_log("确认物流方案审批成功")
            # 切换交易员账户
            time.sleep(1)
            JYY = driver.find_element_by_xpath('/html/body/div[1]/div/div/ul[2]/li/a/span')
            out1 = driver.find_element_by_xpath('/html/body/div[1]/div/div/ul[2]/li/div/p/a')
            ActionChains(driver).move_to_element(JYY).click(out1).perform()
            # 登陆交易员
            bss.write_log("切换交易员登陆中....")
            driver.find_element_by_class_name("ant-input").clear()
            driver.find_element_by_class_name("ant-input").send_keys("ldwjyy")
            time.sleep(1)
            # xpath寻找密码框，并输入
            driver.find_element_by_xpath("//input[contains(@placeholder,'密码')]").clear()
            driver.find_element_by_xpath("//input[contains(@placeholder,'密码')]").send_keys(pws)
            # xpath点击登陆按钮
            driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]/button").click()
            # 点击我得粮达
            time.sleep(0.5)
            driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div/div[2]/ul/li[2]/a').click()
            time.sleep(1)
            new_window5 = driver.window_handles
            driver.switch_to.window(new_window5[-1])
            bss.write_log("交易员登陆完成")
            # 进入可行性报告列表界面
            #driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/dl/dd[1]/ul/li[6]/a').click()
            driver.execute_script("arguments[0].click();",driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/dl/dd[2]/ul/li[6]/a'))
            new_window6 = driver.window_handles
            driver.switch_to.window(new_window6[-1])
            time.sleep(1)
            # 选择全部可行性报告
            bss.write_log("可行性报告查询中...")
            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[1]/a/span[1]').click()
            driver.find_element_by_xpath('/html/body/div[8]/ul/li[2]/div').click()
            time.sleep(0.5)
            # 确认可行性报告名称
            JYname = driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[1]/div/div[1]/a[1]').text
            self.assertEqual(JYname, Title1, "可行性报告选择错误")
            bss.write_log("可行性报告选择成功")
            # 签署框架协议
            bss.write_log("签章框架协议中....")
            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[5]/div/a[1]').click()
            time.sleep(0.5)
            #选择新增合同
            driver.find_element_by_xpath('/html/body/div[9]/div/table/tbody/tr[2]/td/div/div/div[1]/label[2]/input').click()
            #选择新增合同类型
            driver.find_element_by_xpath('/html/body/div[9]/div/table/tbody/tr[2]/td/div/div/div[3]/select').click()
            #选择固定合同模板
            driver.find_element_by_xpath("/html/body/div[9]/div/table/tbody/tr[2]/td/div/div/div[3]/select/option[2]").click()
            #点击合同模板
            driver.find_element_by_xpath('/html/body/div[9]/div/table/tbody/tr[2]/td/div/div/div[4]/div/a/span[1]').click()
            time.sleep(0.5)
            #选择合同
            driver.find_element_by_xpath('//*[@id="select2-result-label-14"]').click()
            time.sleep(0.5)
            #driver.execute_script("arguments[0].click();",self.jsxx)
            #确定按钮
            self.js_enter=driver.find_element_by_xpath("/html/body/div[8]/div/table/tbody/tr[2]/td/div/div/div[6]/a")
            driver.execute_script("arguments[0].click();",self.js_enter)
            # 弹框确认
            driver.find_element_by_xpath('/html/body/div[12]/div[2]/div/div[2]/div[2]/div[1]/a').click()
            bss.write_log('框架协助签署完成')
            # 提交审批
            bss.write_log('提交审批中....')
            time.sleep(0.5)
            js_tijiao = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[5]/div/a[2]')
            driver.execute_script("arguments[0].click();", js_tijiao)
            # 弹框确认
            time.sleep(0.5)
            driver.find_element_by_xpath('//*[@id="ok"]').click()
            driver.find_element_by_xpath("/html/body/div[12]/div[2]/div/div[2]/div[2]/div[1]/a").click()
            time.sleep(0.5)
            JYZT = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[4]/span').text
            self.assertEqual(JYZT, "领导待审", '可行性报告状态有误，未提交审批')
            bss.write_log('提交审批成功')
            # 查询审批人
            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[1]/span[4]/span').click()
            self.JYSP = driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div[5]/div[1]/div[1]/span[4]/div/table/tbody/tr/td[2]').text
            useJ = p.get_pinyin(self.JYSP, '')
            bss.write_log("获取审批人为：%s" % self.JYSP)
            # 切换BPM审批界面
            bss.write_log("跳转BPM审批中....")
            driver.switch_to.window(bpm_windows[-1])
            time.sleep(0.5)
            driver.find_element_by_xpath('/html/body/div/div[1]/span[1]/a/img').click()
            time.sleep(0.5)
            driver.find_element_by_xpath('/html/body/div/div[1]/span[1]/a/img').click()
            # 弹框确认
            alert2 = driver.switch_to.alert
            alert2.accept()
            # BPM账户输入切换
            driver.find_element_by_xpath('/html/body/div/form/div/p[1]/input').clear()
            driver.find_element_by_xpath('/html/body/div/form/div/p[1]/input').send_keys(useJ)
            driver.find_element_by_xpath('/html/body/div/form/div/p[2]/input').clear()
            driver.find_element_by_xpath('/html/body/div/form/div/p[2]/input').send_keys(pws)
            # 点击登陆
            driver.find_element_by_xpath('/html/body/div/form/div/div[1]/a').click()
            bss.write_log("BPM切换用户登陆完成")
            # 选择审批项
            driver.find_element_by_xpath('/html/body/div/div[3]/ul/li[1]/a/div/div').click()
            time.sleep(0.5)
            driver.find_element_by_xpath('/html/body/div/div[3]/ul/li[3]/div[2]/a[1]/div').click()
            # 确认标题是否一致
            BpmTitle3 = driver.find_element_by_xpath('/html/body/ul[1]/a/li/span/p[1]/span').text
            if BpmTitle3 == Title1:
                pass
            else:
                bss.write_log("审批项有误")
            bss.write_log("确认审批项完成")
            # 进入审批项
            driver.find_element_by_xpath('/html/body/ul[1]/a/li/span/p[2]/span[1]').click()
            # 审批处理
            driver.find_element_by_xpath('//*[@id="checkOpt"]/span').click()
            # 弹框确认
            driver.find_element_by_xpath('/html/body/div/div[2]/button[1]').click()
            driver.find_element_by_xpath('/html/body/div/div[4]/button').click()
            time.sleep(0.5)
            alert4 = driver.switch_to.alert
            alert4.accept()
            bss.write_log("BPM审批完成")
            # 刷新可行性报告状态
            driver.switch_to.window(new_window6[-1])
            time.sleep(2)
            #选择全部可行性报告
            try:
                driver.find_element_by_xpath('//*[@id="s2id_about"]/a/span[2]/b').click()
                time.sleep(1)
                driver.find_element_by_xpath('/html/body/div[9]/ul/li[2]/div').click()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/a[1]').click()
                #driver.execute_script("arguments[0].click();", search_s)
                # 确认可行性报告标题
                KXMZ = driver.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[1]/div/div[1]/a[1]').text
                self.assertEqual(KXMZ, Title1, "可行性报告查找有误")
                # 状态确认
                KXZT = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[5]/div[1]/div[2]/div[4]/span').text
                self.assertEqual(KXZT, "可行性报告审批通过", "领导待审")
                bss.write_log("可行性报告审批通过；客户开始签署框架合同")
            except:
                bss.write_log("搜索按钮没有点击到")
            #开始EOMS寻找签章员
            Eoms_login()

        def tearDown(self):
            time.sleep(100)
            self.driver.quit()

class Eoms_login(unittest.TestCase):
    def __init__(self):
        global bosy
        bosy= log_input()
        self._type_equality_funcs={}
        self.driver=driver
        # 客户签章,跳转EOMS界面
        self.js_eoms = "window.open('http://test.eoms.liangdawang.com:8087/eoms/page/portalManage/login.jsp')"
        driver.execute_script(self.js_eoms)
        # 记录目前所有句柄
        self.Eoms_windows = driver.window_handles
        driver.switch_to.window(self.Eoms_windows[-1])
        #输入账户密码
        driver.find_element_by_xpath("//*[@id='userName']").send_keys("admin")
        driver.find_element_by_xpath("//*[@id='pwdzone']").send_keys("dajidali")
        #刷新验证码
        driver.find_element_by_xpath('//*[@id="changeCode"]').click()
        Eoms_login.mkdir(self)
        time.sleep(3)
        self.Yzm()
    def Yzm(self):
        path = 'D://taoler/pic'
        code1 = driver.find_element_by_xpath('//*[@id="codeInput"]')  # 定位验证码输入框
        try:
            # 清空该文件夹内容
            for i in os.listdir(path):
                path_file = os.path.join(path, i)
                if os.path.isfile(path_file):
                    os.remove(path_file)
                else:
                    for f in os.listdir(path_file):
                        path_file2 = os.path.join(path_file, f)
                        if os.path.isfile(path_file2):
                            os.remove(path_file2)
            driver.save_screenshot("D://taoler/pic/01.png")  # 截取屏幕内容，保存到本地
            ran = Image.open("D://taoler/pic/01.png")  # 打开截图，获取验证码位置，截取保存验证码
            box = (985, 400, 1070, 450)  # 获取验证码位置,自动定位不是很明白，就使用了手动定位，代表（左，上，右，下）
            ran.crop(box).save("D://taoler/pic/02.png")  # 把获取的验证码保存
            # 获取验证码图片，读取验证码
            imageCode = Image.open("D://taoler/pic/02.png")  # 打开保存的验证码图片
            imageCode.load()
            # 图像增强，二值化
            sharp_img = ImageEnhance.Contrast(imageCode).enhance(2.0)
            sharp_img.save("D://taoler/pic/03.png")  # 保存图像增强，二值化之后的验证码图片
            sharp_img.load()  # 对比度增强
            #bosy.write_log("获取EOMS登陆验证信息%s" % sharp_img)  # 打印图片的信息
            code = pytesseract.image_to_string(sharp_img).strip()  # 读取验证码
            bosy.write_log("EOMS登陆验证码为：%s" % code)  # 输出验证码
            code1.send_keys(code)
            # 点击确定按钮
            driver.find_element_by_xpath('//*[@id="form1"]/div[4]/a').click()
            # 确认是否登陆成功
            dengluscuess = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]").text
            self.assertEqual(dengluscuess, "欢迎您 : 管理员！", '登陆失败')
            bosy.write_log("EOMS登陆成功")
        except:
            driver.find_element_by_xpath('//*[@id="changeCode"]').click()
            code1.clear()
            self.Yzm()
        self.get_GZY()
    def get_GZY(self):
        global GZName
        #确认客户信息管理是否展开
        tuest=driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[1]/div[2]/div/ul/li[1]/div/span[3]").text
        if tuest=="基本信息管理":
            bosy.write_log("客户信息管理已展开")
        else:
            bosy.write_log("客户信息管理未展开")
            driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/a").click()
            bosy.write_log("客户信息管理已展开")
        #直接判断客户信息管理是否展开
        #self.assertEqual(tuest,"基本信息管理","需点击展开客户信息管理")
        # 点击左侧基本信息管理菜单
        driver.find_element_by_xpath("//*[@id='A1000']/li[1]/div/span[1]").click()
        #点击交易商员工管理
        driver.find_element_by_xpath('//*[@id="A1000"]/li[1]/ul/li[2]/div/span[4]').click()
        time.sleep(3)
        #跳到右侧frame界面
        driver.switch_to.frame(1)
        #输入交易商名称
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/form/div[1]/div[2]/table/tbody/tr/td[2]/input').send_keys(G_name)
        #选择角色名称
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[1]/div[1]/form/div[2]/div[2]/table/tbody/tr/td[1]/span/span/span').click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div[8]').click()
        #点击查询
        driver.find_element_by_xpath('//*[@id="btn"]/span/span').click()
        driver.switch_to.default_content()
        # 点击用户信息
        driver.switch_to.frame(driver.find_element_by_name("WinA1301"))
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[3]/div').click()
        # 点击修改
        driver.find_element_by_xpath('//*[@id="sysParamEdit"]/span/span').click()
        # 获取登陆名
        driver.switch_to.default_content()
        frame_name = driver.find_element_by_xpath('//*[@id="easyui_dial_iframe"]')
        driver.switch_to.frame(frame_name)
        time.sleep(1)
        GZName = driver.find_element_by_xpath('//*[@id="userId"]').get_attribute("value")
        bosy.write_log("盖章员登陆名称：%s" % GZName)
        seal()
    def mkdir(self):
        global path
        bosx=log_input()
        self.path="D://taoler/pic"
        path=self.path.strip()
        path=path.rstrip("\\")
        isExist=os.path.exists(path)
        if not isExist:
            os.makedirs(path)
            bosx.write_log("创建临时目录成功")
        else:
            bosx.write_log("目录已存在")
            return False
class seal():
    def __init__(self):
        # 切换主页登陆角色
        self.bssy=log_input()
        self.new_window=driver.window_handles
        driver.switch_to.window(self.new_window[-2])
        JYS_GZY=driver.find_element_by_xpath('/html/body/div[1]/div/div/ul[2]/li/a/span')
        out2 = driver.find_element_by_xpath('/html/body/div[1]/div/div/ul[2]/li/div/p/a')
        ActionChains(driver).move_to_element(JYS_GZY).click(out2).perform()
        # 登陆交易员
        self.bssy.write_log("切换交易商盖章员登陆中....")
        driver.find_element_by_class_name("ant-input").clear()
        driver.find_element_by_class_name("ant-input").send_keys(GZName)
        time.sleep(1)
        # xpath寻找密码框，并输入
        driver.find_element_by_xpath("//input[contains(@placeholder,'密码')]").clear()
        driver.find_element_by_xpath("//input[contains(@placeholder,'密码')]").send_keys("123456")
        # xpath点击登陆按钮
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]/button").click()
        time.sleep(1)
        self.bssy.write_log("交易商盖章员登陆成功")
        try:
            rz_change=driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/p[1]").text
            if "请前往认证" in rz_change:
                self.bssy.write_log("盖章员需要进行签章认证")
                self.QZ_RZ()
            else:
                self.bssy.write_log("该账户已通过签章认证，需进行可行性报告签章")
        except:
            self.QZ_RZ()
    def phone_number(self):
        global phone_numbers
        self.phone_numbers = askstring("Spam", "请输入签章手机号")
        self.bssy.write_log("签章认证手机号为：%s"%self.phone_numbers)
    def phone_YZM(self):
        global phone_YZM
        self.phone_YZM = askstring("Spam", "请输入签章手机号")
        self.bssy.write_log("签章认证手机号为：%s" % self.phone_YZM)
    def QZ_RZ(self):
        self.driver = driver
        bssz=log_input()
        # 点击弹框去认证
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]").click()
        # 点击跳转签章认证界面
        driver.find_element_by_xpath('/html/body/div[7]/div/table/tbody/tr[2]/td/div/div/div/div/div[2]/a[1]').click()
        # 滑动进度条
        renzheng_window = driver.window_handles
        driver.switch_to.window(renzheng_window[-1])
        time.sleep(12)
        agree_xy = driver.find_element_by_xpath('/html/body/div[1]/div[3]/p[43]')
        driver.execute_script("arguments[0].scrollIntoView();", agree_xy)
        # 点击同意并继续
        driver.find_element_by_xpath('/html/body/div[1]/div[4]/span').click()
        # 同意协议并开始认证
        try:
            driver.find_element_by_xpath('//*[@id="startCert"]').click()
        except:
            # 点击同意协议
            driver.find_element_by_xpath('//*[@id="readAgree"]').click()
            driver.find_element_by_xpath('//*[@id="startCert"]').click()
        # 进入签章选择界面
        QZ_XZ = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/p').text
        if QZ_XZ == "以下方式通过一种即可":
            bssz.write_log("进入签章选择界面成功")
        else:
            bssz.write_log("进入签章界面失败")
            driver.find_element_by_xpath('//*[@id="readAgree"]').click()
            driver.find_element_by_xpath('//*[@id="startCert"]').click()
        # 选择手机认证
        driver.find_element_by_xpath('//*[@id="phoneVerification"]').click()
        qz_windowhandles=driver.window_handles
        driver.switch_to.window(qz_windowhandles[-1])
        # 获取签章手机号
        driver.find_element_by_xpath('/html/body/div[1]/div/div/form/ul/li/div[3]/div/input').send_keys(self.phone_numbers)
        # 点击发送验证码
        driver.find_element_by_xpath('/html/body/div[1]/div/div/form/ul/li/div[3]/div/a').click()
        # 输入验证码
        driver.find_element_by_xpath('/html/body/div[1]/div/div/form/ul/li/div[4]/div/input').send_keys(self.phone_YZM)
        # 点击提交
        driver.find_element_by_xpath('/html/body/div[1]/div/div/form/ul/div/a').click()














class log_input():
#获取当前时间
    def get_current_time(self):
        current_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        return current_time
#获取日志
    def write_log(self,logmsg):
        global Log_num
        current_time=self.get_current_time()
        logmsg_in=str(current_time)+"   "+str(logmsg) +""+"\n"  #换行
        if Log_num<=9:
            init_text.insert(tk.END,logmsg_in)
            Log_num=Log_num+1
        else:
            init_text.delete(1.0,2.0)
            init_text.insert(tk.END,logmsg_in)

if __name__=="__main__":
    ini = tk.Tk()
    Test_main_tk(ini)
    ini.mainloop()