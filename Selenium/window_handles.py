#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver=webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()
driver.get('http://www.baidu.com')
#获取当前窗口得句柄
now1=driver.current_window_handle
print(now1)
windows=driver.window_handles
driver.find_element_by_id('kw').send_keys('天气')
driver.find_element_by_id('su').click()
#获取所有窗口得句柄
windows1=driver.window_handles
#切换原来的窗口
driver.switch_to.window(windows1[-1])
#当上面选择当前句柄时，找到最新的句柄：
for i in windows1:
    if i!=now1:
        driver.switch_to.window(i)


#当保存句柄顺序与打开页面顺序不一致。去除重复，找到最新界面：
def choose(windows,windows1):
    for i in windows1:
        if i not in windows:
            return windows1.index(i)

b=choose(windows,windows1)
driver.switch_to.window(windows1[b])
print(driver.title)






