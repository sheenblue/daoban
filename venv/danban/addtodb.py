# -*- coding: utf-8 -*-
# @Author : sheen
# @Time   : 2022-08-09
# @FILE   : addtodb.py



import sqlite3
import time

from sqlite3 import Error


def sql_connection(name):
    try:

        con = sqlite3.connect(f'{name}.db')

        return con

    except Error:

        print(Error)

def create_table(con,name,sql):
    classname = name

    try:

        con.execute(f'CREATE TABLE IF NOT EXISTS classname{sql}')
    except Exception as r:
        print(r)
        print("Create table failed")
        return False
    con.commit()
    #con.close()
    print('表格创建成功')
def sql_insert(con,name,value):
    #num = int(num)
    #t2 = time.strftime("%Y-%m-%d %X", time.localtime())
    cursorObj = con.cursor()
    #num1 = (num,)
    cursorObj.execute(
        f'INSERT INTO {name} VALUES{value}')

    con.commit()
    print('数据插入成功！！！')
    #print(f'===============================插入=={num}==手机号成功')


def sql_fetch(con,name,top,value):
    #num = int(num)
    cursorObj = con.cursor()
    value = (value,)
    cursorObj.execute(f'SELECT *  FROM {name} WHERE {top} = ?',value)

    rows = cursorObj.fetchall()

    if rows == []:
        print('---------------------教程未入库')
        return True
    else:
        print('----------------------------------------教程已入库')
        return False


def sql_del(con,num):
    num = int(num)

    cursorObj = con.cursor()
    num1 = (num,t2)

    cursorObj.execute(
        "delete from employees where phone = ?", num1)

    con.commit()
    print(f'===============================删除=={num}==手机号成功')


#修改表字段
def midsql_table(con):

    cursorObj = con.cursor()


    cursorObj.execute(
        "alter table employees add time text")

    con.commit()
    print('添加表字段成功')




if __name__ == '__main__':
    con = sql_connection('class')
    t = ('NAME TEXT','URL TEXT','CLASS TEXT')
    #t = '(name text, salary real, department text)'
    name = 'classname'
    create_table(con,name,t)
    value = ('123','1223','1223')
    print(value[0])
    top = 'NAME'
    if sql_fetch(con,name,top,value[0]):
        sql_insert(con,name,value)
        pass
