#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
from selenium import webdriver
from time import *
from selenium.webdriver.common.action_chains import ActionChains
begin_time=time()
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://test.liangdawang.com:8085/portal/")
driver.find_element_by_xpath("//span[@class='_3xBql6BA5xe4GM7139erx0']/span[2]/a[1]").click()
driver.find_element_by_xpath("//input[contains(@placeholder,'账户名/手机号码')]").send_keys('101')
driver.find_element_by_xpath("//input[contains(@placeholder,'密码')]").send_keys('123456')
driver.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary ant-btn-block']").click()
driver.find_element_by_xpath("//a[contains(@href,'auctionList')]").click()  #竞价交易

newwindows=driver.window_handles
driver.switch_to.window(newwindows[0])
driver.find_element_by_xpath("//a[contains(@href,'tenderTradeInfoList')]").click()  #招投标交易

def new(a,b):
    for i in b:
        if i not in a:
            return b.index(i)

#找到最新界面得句柄，并跳转
newwindows1=driver.window_handles
i=new(newwindows,newwindows1)
driver.switch_to.window(newwindows1[i])
Mld=driver.find_element_by_xpath("//a[contains(@href,'MENU1200')]")
Mld1=driver.find_element_by_xpath("/html/body/div/div/div[1]/div/div/div/div[2]/ul/li[2]/ul/li[3]/a")
ActionChains(driver).move_to_element(Mld).click(Mld1).perform()
#以下为错误界面定位
driver.find_element_by_id("enableTls10Button").click()
high=driver.find_element_by_id("advancedButton")
contine=driver.find_element_by_id("exceptionDialogButton")
ActionChains(driver).move_to_element(high).click(contine).perform()


end_time=time()
run_time=end_time-begin_time
print(run_time)





