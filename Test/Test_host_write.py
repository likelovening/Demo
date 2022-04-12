#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
import os
def file_modify(filename,old,new):
    with open(filename,'r') as old_file:
        old_modify=old_file.read()   #先把文件读取出来
        new_modify=old_modify.replace(old,new)  #使用new替换old全部文件内容
    with open(filename,'w')as new_file:   #打开写权限
        new_file.write(new_modify)      #将new写入文件中
    new_file.close()

old="00000"
new="11111"
file_modify('D:\host.txt',old,new)



f=open("",'r')

import time
def fo(func):
    def foo():
        start_time=time.time()
        func()
        time.sleep(0.01)
        end_time=time.time()
        print("花费的时间：%s"%(end_time-start_time))
#        return func()
    return foo
@fo
def f1():
    sum=1
    for i in range(1,10):
        sum=i*sum
    print(sum)
if __name__=="__main__":
    f1()





