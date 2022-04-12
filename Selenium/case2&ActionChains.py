#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
option=webdriver.ChromeOptions()
option.add_argument('headless')  #无界面启动
#option.add_argument('--start-maximized')  #最大化运行
# driver=webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe',
# chrome_options=option)  #设置环境变量地址
driver=webdriver.Chrome()
begin_url='http://test.liangdawang.com:8085/portal/'  #设置网址
timeout=5
search_key='python'
driver.get(begin_url)
print(driver.title)
search_input=WebDriverWait(driver,timeout).until(lambda d:d.find_element_by_xpath('//a[contains(@href,"aHR0cDovL3Rlc3QubGlhbmdkYXdhbmcuY29tOjgwODUvcG9ydGFsLw")]'))
search_input.click()
name_input=driver.find_element_by_xpath("//img[contains(@src,'')]").send_keys("100")

from selenium.webdriver.common.action_chains import ActionChains
Action=ActionChains(driver)
Action.move_to_element(search_input).click().perform()
Action.click_and_hold()  #点击鼠标左键，不松开
Action.context_click()   #点击鼠标右键
Action.double_click()    #双击鼠标左键
Action.drag_and_drop()   #拖拽到某个元素然后松开
Action.drag_and_drop_by_offset()    #拖拽到某个坐标然后松开
Action.key_down()    #按下某个键盘上的键
Action.key_up()      #松开某个按键
Action.move_to_offset()          #鼠标移动到某个坐标
Action.move_to_element()         #鼠标移动到某个元素
Action.move_to_elemeng_with_offset()    #移动到距某个元素（左上角坐标）多少距离的位置
Action.perform()    #执行链中的所有操作
Action.release()    #在某个元素位置松开鼠标左键
Action.send_keys()  #发送某个键到当前焦点的元素
Action.send_keys_to_element()   #发送某个键到指定元素






















