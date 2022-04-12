#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By   #导入By模块以便与使用查找使用元素
import time
from selenium.webdriver.common.action_chains import ActionChains   #导入鼠标滑动，点击等库
#driver=webdriver.Chrome()
driver=webdriver.Firefox()
#设置全局响应时间
driver.implicitly_wait(5)
#设置最大屏幕尺寸打开
driver.maximize_window()
driver.get("http://test.liangdawang.com:8085/portal/")
#xpath寻找“请登录”按钮
driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/div/div[1]/span/span[2]/a[1]").click()

#正式环境中
#driver.find_element_by_xpath("//a[contains(@href,'FuZ2')]").click()

#xpath寻找账户框，并输入
driver.find_element_by_class_name("ant-input").send_keys("Logistics_F")

#xpath寻找密码框，并输入
driver.find_element_by_xpath("//input[contains(@placeholder,'密码')]").send_keys("123456")

#xpath点击登陆按钮
driver.find_element_by_class_name("ant-btn.ant-btn-primary.ant-btn-block").click()

#找到一级菜单“我的粮达”
Myld=driver.find_element_by_xpath("//a[contains(@href,'MENU1101')]")
#找到物流菜单
logistics=driver.find_element_by_xpath("//a[contains(@href,'logisticsUserCenter')]")
#鼠标放菜单上并点击
ActionChains(driver).move_to_element(Myld).click(logistics).perform()

# 获取打开的多个窗口句柄
newwindows = driver.window_handles   #windows是一个数组，windows=[窗口1，窗口2...]
# 切换到当前最新打开的窗口
driver.switch_to.window(newwindows[-1])   #windows[0]是第一个界面
#点击物流定向报价
driver.find_element_by_xpath("//a[@attid='MENU30010']/span").click()



















#driver.close()