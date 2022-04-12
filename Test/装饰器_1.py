#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
import time
def deco(f):     #装饰器：参数是一个函数，返回值是一个函数。
    def warpper(*args,**kwargs):        #无固定参数的装饰器,使用的函数可带(多个)或不带参数
        print("deco start here")
        start_time=time.time()
        f(*args,**kwargs)
        end_time=time.time()
        execution_time=(end_time-start_time)*1000
        print("time is %d ms"%execution_time)
        print("deco end here")
#        return f(*args,**kwargs)  #返回主函数
    return warpper    #返回已经变成主函数的warpper
def deco1(f):
    def warpper(*args,**kwargs):
        print("deco1 start here")
        f(*args,**kwargs)
        print("deco1 end here")
    return warpper

@deco
def d():
    print("hello")
    time.sleep(1)
    print("world")

if __name__=="__main__":
    d()

@deco
@deco1   #俩个装饰器时，先执行第一个装饰器，再执行第二个装饰器，结果嵌套
def b(a,b):
    print("vicity")
    time.sleep(1)
    print("result is %d"%(a+b))
if __name__=="__main__":
    b(3,4)




