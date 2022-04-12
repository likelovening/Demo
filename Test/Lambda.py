#!/usr/bin/evn python
# -*- encoding: utf-8 -*-

# 1、赋值给变量
add=lambda x,y:x+y
add(1,2)

# 2、赋值给其他函数，改变其他函数的作用
import time
time.sleep=lambda x:None

# 3、作为其他函数的返回值
#  return lambda x,y:x*y

# 4、作为参数传递给其他函数

#   filter函数：过滤掉列表元素的条件，留下符合条件的元素
filter(ord,[1,2,3,4,5,6])  #判断条件，可迭代元素

a=filter(lambda x:x%4==1,[4,5,6])
print(a)

#   sort,sorted函数：对元素进行排序
b=[1,2,3,4]
b.sort(key=ord)  #sort只能针对list

sorted(b,key=lambda x:abs(2-x))  #可迭代元素，排序条件
#对2的距离进行排序
b=[2,1,3,4,5]

#   map函数：逐个对元素进行操作
map(ord,[1,2,3])   #条件，可迭代条件

map(lambda x:x*2,[1,2,3])  #如果有x,y，则后面有俩个list
Result=[2,4,6]
#对元素逐个乘2

#   reduce函数：对元素进行累积(3.0把reduce放在functools中)
from functools import reduce
reduce(lambda x,y:x*2+y*2,[1,2,3,4,5])
print(reduce)
# lambda计算方式，x=x*2+y*2,逐个元素计算







