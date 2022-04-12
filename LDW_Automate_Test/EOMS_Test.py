#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
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
import os
from PIL import Image
from PIL import ImageEnhance
class y:
    def __init__(self):
        global driver
        self.driver= webdriver.Chrome()
        driver=self.driver
        driver.implicitly_wait(30)  # 隐性等待时间为30秒
        driver.maximize_window()
        base_url = "https://test.liangdawang.com:8086/portal/"
        driver.get(base_url)
        Eoms_login()

class Eoms_login(unittest.TestCase):
    def __init__(self):
        self.driver=driver
        self._type_equality_funcs={}
        self.js_eoms = "window.open('http://test.eoms.liangdawang.com:8087/eoms/page/portalManage/login.jsp')"
        driver.execute_script(self.js_eoms)
        self.new_window8 = driver.window_handles
        driver.switch_to.window(self.new_window8[-1])
        self.input1=driver.find_element_by_xpath("/html/body/div[2]/div/form/div[1]/input")
        self.input1.send_keys("admin")
        driver.find_element_by_xpath("//*[@id='pwdzone']").send_keys("dajidali")
        driver.find_element_by_xpath('//*[@id="changeCode"]').click()
        Eoms_login.mkdir(self)
        time.sleep(3)
        self.YZM()
    def YZM(self):
        path = 'D://taoler/pic'
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
            code1 = driver.find_element_by_xpath('//*[@id="codeInput"]')  # 定位验证码输入框
            driver.save_screenshot("D://taoler/pic/01.png")  # 截取屏幕内容，保存到本地
            # time.sleep(5)
            ran = Image.open("D://taoler/pic/01.png")  # 打开截图，获取验证码位置，截取保存验证码
            # time.sleep(5)
            box = (985, 400, 1070, 450)  # 获取验证码位置,自动定位不是很明白，就使用了手动定位，代表（左，上，右，下）
            ran.crop(box).save("D://taoler/pic/02.png")  # 把获取的验证码保存
            # time.sleep(5)
            # 获取验证码图片，读取验证码
            imageCode = Image.open("D://taoler/pic/02.png")  # 打开保存的验证码图片
            imageCode.load()
            # 图像增强，二值化
            sharp_img = ImageEnhance.Contrast(imageCode).enhance(2.0)
            sharp_img.save("D://taoler/pic/03.png")  # 保存图像增强，二值化之后的验证码图片
            sharp_img.load()  # 对比度增强
            print(sharp_img)  # 打印图片的信息
            code = pytesseract.image_to_string(sharp_img).strip()  # 读取验证码
            # 收到验证码，进行输入验证
            print("验证码是：%s"%code)  # 输出验证码
            code1.send_keys(code)
            # 点击确定按钮
            driver.find_element_by_xpath('//*[@id="form1"]/div[4]/a').click()
            # 点击左侧菜单
            dengluscuess = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]").text
            self.assertEqual(dengluscuess, "欢迎您 : 管理员！", '登陆失败')
            print("登陆成功")
        except:
            driver.find_element_by_xpath('//*[@id="changeCode"]').click()
            code1.clear()
            self.YZM()
        self.get_GZY()
    def get_GZY(self):
        #确认客户信息管理是否展开
        tuest=driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[1]/div[2]/div/ul/li[1]/div/span[3]").text
        if tuest=="基本信息管理":
            print("客户信息管理已展开")
        else:
            print("客户信息管理未展开")
            driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/a").click()
            print("客户信息管理已展开")
        # 点击左侧基本信息管理菜单
        driver.find_element_by_xpath("//*[@id='A1000']/li[1]/div/span[1]").click()
        #点击交易商员工管理
        driver.find_element_by_xpath('//*[@id="A1000"]/li[1]/ul/li[2]/div/span[4]').click()
        time.sleep(3)
        #跳到右侧frame界面
        driver.switch_to.frame(1)
        #输入交易商名称
        x="深圳市小"
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/form/div[1]/div[2]/table/tbody/tr/td[2]/input').send_keys(x)
        #选择角色名称
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/form/div[2]/div[2]/table/tbody/tr/td[1]/span/span/span').click()
        driver.find_element_by_xpath('/html/body/div[3]/div/div[8]').click()
        #点击查询
        driver.find_element_by_xpath('//*[@id="btn"]/span/span').click()
        driver.switch_to.default_content()
        #点击用户信息
        driver.switch_to.frame(driver.find_element_by_name("WinA1301"))
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[3]/div').click()
        #driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-1-0']/td[2]/div").click()
        #点击修改
        driver.find_element_by_xpath('//*[@id="sysParamEdit"]/span/span').click()
        #获取登陆名
        driver.switch_to.default_content()
        frame_name=driver.find_element_by_xpath('//*[@id="easyui_dial_iframe"]')
        driver.switch_to.frame(frame_name)
        time.sleep(1)
        self.GZName=driver.find_element_by_xpath('//*[@id="userId"]').get_attribute("value")
        print("盖章员名字：%s"% self.GZName)
        self.login_gzy()
    def login_gzy(self):
        # 切换主页登陆角色
        driver.switch_to.window(self.new_window8[-2])
        print("交易商盖章员登陆中....")
        # xpath寻找“请登录”按钮
        driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/div/div[1]/span/span[2]/a[1]").click()
        time.sleep(1)
        # xpath寻找账户框，并输入
        driver.find_element_by_class_name("ant-input").send_keys(self.GZName)
        time.sleep(1)
        # xpath寻找密码框，并输入
        driver.find_element_by_xpath("//input[contains(@placeholder,'密码')]").send_keys("123456")
        # xpath点击登陆按钮
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[5]/button").click()
        time.sleep(1)
        print("交易商盖章员登陆成功")
        try:
            rz_change=driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/p[1]").text
            if "请前往认证" in rz_change:
                print("盖章员需要进行签章认证")
                QZ_RZ()
            else:
                print("该账户已通过签章认证，需进行可行性报告签章")
        except:
            QZ_RZ()
    def mkdir(self):
        global path
        #bosx=log_input()
        self.path="D://taoler/pic"
        path=self.path.strip()
        path=path.rstrip("\\")
        isExist=os.path.exists(path)
        if not isExist:
            os.makedirs(path)
            print("创建临时目录成功")
        else:
            print("目录已存在")
            return False
#签章认证
class QZ_RZ():
    def __init__(self):
        self.driver=driver
        time.sleep(2)
        #点击弹框去认证
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/button[2]").click()
        # 点击跳转签章认证界面
        driver.find_element_by_xpath('/html/body/div[7]/div/table/tbody/tr[2]/td/div/div/div/div/div[2]/a[1]').click()
        #滑动进度条
        renzheng_window = driver.window_handles
        driver.switch_to.window(renzheng_window[-1])
        time.sleep(20)
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
            print("进入签章选择界面成功")
        else:
            print("进入签章界面失败")
            driver.find_element_by_xpath('//*[@id="readAgree"]').click()
            driver.find_element_by_xpath('//*[@id="startCert"]').click()
        # 选择手机认证
        driver.find_element_by_xpath('//*[@id="phoneVerification"]').click()

if __name__=="__main__":
    y()













