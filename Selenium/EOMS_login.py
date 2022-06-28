#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
import os
from PIL import Image
from PIL import ImageEnhance
from pytesseract import pytesseract
from selenium import webdriver
import unittest, time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sys
driver = webdriver.Chrome()
driver.implicitly_wait(15)  # 隐性等待时间为30秒
driver.maximize_window()
base_url = "http://test.eoms.liangdawang.com:8087/eoms/page/portalManage/login.jsp"
driver.get(base_url)
driver.find_element_by_xpath("//*[@id='userName']").send_keys("admin")
driver.find_element_by_xpath("//*[@id='pwdzone']").send_keys("dajidali")
time.sleep(3)
path = 'D://taoler/pic'  # 清空该文件夹内容
for i in os.listdir(path):
    path_file = os.path.join(path, i)
    if os.path.isfile(path_file):
        os.remove(path_file)
    else:
        for f in os.listdir(path_file):
            path_file2 = os.path.join(path_file, f)
            if os.path.isfile(path_file2):
                os.remove(path_file2)
code1=driver.find_element_by_xpath('//*[@id="codeInput"]')  # 定位验证码输入框
driver.save_screenshot("D://taoler/pic/01.png")  # 截取屏幕内容，保存到本地
#time.sleep(5)
ran = Image.open("D://taoler/pic/01.png")  # 打开截图，获取验证码位置，截取保存验证码
#time.sleep(5)
box = (985, 400, 1070, 450)  # 获取验证码位置,自动定位不是很明白，就使用了手动定位，代表（左，上，右，下）
ran.crop(box).save("D://taoler/pic/02.png")  # 把获取的验证码保存
#time.sleep(5)
# 获取验证码图片，读取验证码
imageCode = Image.open("D://taoler/pic/02.png")  # 打开保存的验证码图片
imageCode.load()
# 图像增强，二值化
sharp_img = ImageEnhance.Contrast(imageCode).enhance(2.0)
sharp_img.save("D://taoler/pic/03.png")  # 保存图像增强，二值化之后的验证码图片
sharp_img.load()  # 对比度增强
#time.sleep(5)
print(sharp_img)  # 打印图片的信息
code = pytesseract.image_to_string(sharp_img).strip()  # 读取验证码
# 5、收到验证码，进行输入验证
print(code)  # 输出验证码
code1.send_keys(code)
driver.find_element_by_xpath('//*[@id="form1"]/div[4]/a').click()
driver.find_element_by_xpath("//*[@id='aa']/div[3]/div[1]/div[1]").click()
driver.find_element_by_xpath('//*[@id="A23000"]/li[1]/div/span[1]').click()
driver.find_element_by_xpath('//*[@id="A23000"]/li[1]/ul/li[1]/div/span[4]').click()

time.sleep(3)
window_hands=driver.window_handles
print(window_hands)
driver.switch_to.window(window_hands[-1])
driver.switch_to.frame(1)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/table/tbody/tr/td[1]/a/span/span').click()






















