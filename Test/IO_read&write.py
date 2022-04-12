#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
def Z_read(func):
    def A_read(*args,**kwargs):
        func(*args,**kwargs)
        with open(r"C:\Users\Administrator\Desktop\IO.txt", "r", encoding="GB2312") as fo:
            for i in fo:
                print(i.strip())
            return func(*args,**kwargs)
    return A_read
#装饰器作用在主代码执行之后。替换完对应得字符后打印出该文件内容
@Z_read
def r_read(old_wrod,new_wrod):
    with open(r"C:\Users\Administrator\Desktop\IO.txt","r",encoding="GB2312") as R:
        old_title=R.read()
        new_title=old_title.replace(old_wrod,new_wrod)
    with open(r"C:\Users\Administrator\Desktop\IO.txt","w",encoding="GB2312") as RR:
        RR.write(new_title)
    return RR
if __name__=="__main__":
    old="11111"
    new="00000"
    r_read(old,new)