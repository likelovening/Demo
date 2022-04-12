#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
#斐波那契数列是指0、1、1、2、3、5、8、13、21.....每一项都是前俩项之和
                #for循环实现
from functools import reduce
enput=int(input('输入月份：'))
a=0
b=1
count=2
if enput<0:
    print("非正整数")
elif enput==1:
    print(a)
else:
    print(a," ",b,end=' ')
    while enput>count:
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        count+=1
print('\n')
"----------------------------------------------------------------------------------"
                #while循环实现
def face1(n1):
    i1,num1,num2=0,1,1
    ret=[]
    while i1<n1:
        ret.append(num1)
        num1,num2=num2,num1+num2
        i1+=1
    return ret
if __name__=="__main__":
    print(face1(8))
"----------------------------------------------------------------------------------"
                #递归实现(1)
def face(n):
    ret=[]
    for i in range(n+1):
        if i==1 or i==0:
            ret.append(1)
        else:
            ret.append(ret[i-2]+ret[i-1])
    return ret
if __name__=="__main__":
    print(face(8))















