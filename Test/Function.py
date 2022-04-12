#!/usr/bin/evn python
# -*- encoding: utf-8 -*-

#  1、replace（old,new,num） num指替换的次数
def Replace(souce,key):
    tem=souce.replace(key,"")
    return tem
if __name__=='__main__':
    tem1=Replace("xxssdafasfad","xx")
    print(tem1)


#   2、map（ord,list）  元素逐个进行计算，返回还是list
def Map(souce1):
    tem2=map(lambda x:x*2,souce1)
    return tem2
if __name__=='__main__':
    A=Map([1,2,3,4,5])
    print(list(A))


#   3、reduce(tuple或list进行累计计算)
from functools import reduce
def Reduce(souce2):
    Re=reduce(lambda x,y:x+y,souce2)
    return Re
if __name__=="__main__":
    i=[1,2,3,4,5]
    print(Reduce(i))

#   4、split(key,num1)[num2]   key=分隔符，num1=分割次数,默认num1+1个，num2=选取第几个字符,从0开始
def run(souce,key):
    ret=souce.split(key)[2]
    return ret
if __name__=="__main__":
    ret1=run("xxccvvbbxxccwvvxxbb","xx")
    print(ret1)

#   5、Xpath
def xpath():
    from selenium import webdriver
    driver=webdriver.Firefox()
    driver.find_element_by_xpath("//s[@id='xx']/a/div/input[@name='aa']")  #绝对路径
    driver.find_element_by_xpath("/html/body/div/...")  #绝对路径
    driver.find_element_by_xpath("//a[contain(@href,'com')]")   #包含com的模糊定位
    driver.find_element_by_xpath("//a[starts-with(@href,'url')]")   #以href开始，包含url
    driver.find_element_by_xpath("//a[contain(text(),'退出')]")   #包含文本信息


#   6、ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

driver = webdriver.Firefox()
myld=driver.find_element_by_xpath("//s[@id='xx']/a/div/input[@name='aa']")
Logistics=driver.find_element_by_xpath("/html/body/div/...")

ActionChains(driver).move_to_element(myld).click(Logistics).perform()

















