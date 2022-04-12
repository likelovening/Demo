#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
#阶乘1
from functools import reduce

input1=int(input("1、输入数字："))
num=1
if input1<=0:
    print("非正整数")
elif input1==1:
    print(num)
else:
    num=reduce(lambda x,y:x*y,range(1,input1+1))
    print("%s的阶乘(reduce)="%input1,num)

#阶乘2
input2=int(input("2、输入数字："))
num2=1
if input2<=0:
    print("非正整数")
elif input2==1:
    print(num2)
else:
    for i in range(1,input2+1):
        num2*=i
    print("%s的阶乘(for)="%input2,num2)

#阶乘3 若是0不能这么玩
input3=int(input("3、输入数字："))
num3=1
while(input3>0):
    num3*=input3
    input3-=1
print("%s的阶乘（while）="%input3,num3)

#阶乘4（递归）
def face(input4):
    if input4==0:
        return "非正整数"
    elif input4==1:
        return 1
    else:
        return(input4*face(input4-1))  #自己调用自己
input4=int(input("4、输入数字："))
print("%s的阶乘(递归)="%input4,face(input4))








