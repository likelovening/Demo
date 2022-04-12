#!/usr/bin/evn python
# -*- encoding: utf-8 -*-
import pymysql
#连接数据库
db=pymysql.connect("localhost_3306","root","123456","mysql")  #数据库地址，账户，密码，数据库名称
#使用cursor()方法获取操作游标
cursor=db.cursor()
#使用execute方法执行SQL语句
cursor.execute("SELECT * FROM db where Db='sys' ")
#使用fetchone()方法获取一条数据
data=cursor.fetchone()
print(data)
#关闭数据库
db.close()




















