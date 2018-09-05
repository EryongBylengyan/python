# encoding:utf-8
__author__ = 'admin'
import mysql.connector

conn =mysql.connector.connect(host="localhost",user="root",password="123456",database="test")
cursor = conn.cursor()
print cursor.statement

"""
cursor.execute("create table user (id VARCHAR (20) PRIMARY KEY ,"
               "NAME VARCHAR (20))")
#创建用户表
cursor.execute("insert into user(id,NAME) VALUE (%s,%s)",["1","Jack"])
print cursor.rowcount

#提交事务
conn.commit()
cursor.close()

#运行查询
cursor=conn.cursor()
cursor.execute("select * from user where id = %s",("1"))
values = cursor.fetchall()
print values
"""
print cursor.close()
print conn.close()