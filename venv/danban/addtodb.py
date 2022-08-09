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
    con.close()
    print(表格创建成功)
def sql_insert(con, num):
    num = int(num)
    t2 = time.strftime("%Y-%m-%d %X", time.localtime())
    cursorObj = con.cursor()
    num1 = (num,t2,)
    cursorObj.execute(
        'INSERT INTO employees(phone,time) VALUES(?,?)', num1)

    con.commit()
    print(f'===============================插入=={num}==手机号成功')
def sql_fetch(con,num):
    num = int(num)
    cursorObj = con.cursor()
    num1 = (num,)
    cursorObj.execute('SELECT *  FROM employees WHERE phone = ?',num1)

    rows = cursorObj.fetchall()

    if rows == []:
        print('---------------------手机号未注册了')
        return 1
    else:
        print('----------------------------------------手机号已注册')
        return 0


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
    t = '(NAME TEXT,URL TEXT,CLASS,TEXT)'
    #t = '(name text, salary real, department text)'
    name = 'classname'
    create_table(con,name,t)
