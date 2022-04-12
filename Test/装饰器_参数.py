#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
#1、普通三层带参数装饰器+固定主函数名称
import functools
def demo(unitt):
    print("one_111")
    def warpper(func):
        print("two_222")
        @functools.wraps(func)
        def warp(*args,**kwargs):
            print("three_333")
            for i in range(unitt):
                func(*args,**kwargs)
            print("four_444")
        return warp
    print('five_555')
    return warpper

@demo(2)
def demo1():
    'xxxx'
    print("oK")


if __name__=="__main__":
    demo1()
print(demo1.__name__)  #获取demo1函数名称，当没有functools.wraps(func)时，主函数名称被带入装饰改变。
print(demo1.__doc__)  #获取demo1函数注释内容

#2、带参数的装饰器，通过参数决定是否执行装饰器。
import time
import functools
flags=False
def dec(flag):
    def dec1(func):
        @functools.wraps(func)
        def warpss(*args,**kwargs):
            if flag:
                start_time=time.time()
                re=func(*args,**kwargs)
                end_time=time.time()
                print('代码执行时间为:%s'%(end_time-start_time))
                return re
            else:
                re=func(*args,**kwargs)
                return re
        return warpss
    return dec1
@dec(flags)  #只有当参数为false时，才不执行==flags或者直接False；
def demos():
    time.sleep(0.5)
    print("执行完毕")

if __name__=="__main__":
    demos()

