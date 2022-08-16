# -*- coding: utf-8 -*-
# @Author : sheen
# @Time   : 2022-08-15
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

    try:
        #sql1 = 'CREATE TABLE IF NOT EXISTS 91zsw1 {1}'.format(name,sql)
        con.execute(f'CREATE TABLE IF NOT EXISTS {name}{sql} ')

    except Exception as r:
        print(r)
        print("Create table failed")
        return False
    con.commit()
    #con.close()
    print('表格创建成功')
def sql_insert(con,name,value):

    cursorObj = con.cursor()
    t = len(value)
    t = '?,' * t
    t = t[:-1]
    cursorObj.execute(
        f'INSERT INTO {name} VALUES({t})',value)

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
    num1 = (num,)

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

#获取所有数据
def sql_fetchjj(con,name,value): #value 是 字段
    cursorObj = con.cursor()

    cursorObj.execute(f'SELECT {value} FROM {name}')

    rows = cursorObj.fetchall()
    return rows

def sql_update(con,value):
    cursorObj = con.cursor()
    strsql = f"update {nam1e} set name =replace(title, x'0a','')"
    cursorObj.execute(strsql)

if __name__ == '__main__':
    #con = sql_connection('91zsw')
    # t = '(NAMES TEXT, PHONES INT, JYFWS TEXT, CPMS TEXT, SLS TEXT, LXS TEXT, XHS TEXT)'
    # #t = '(name text, salary real, department text)'
    # name = 'classname'
    # create_table(con,name,t)
    # value = ('123','1223','1223')
    # print(value[0])
    # top = 'NAME'
    # if sql_fetch(con,name,top,value[0]):
    #     sql_insert(con,name,value)
    #     pass

    #测试能否导出所有数据
    # name = 'user'
    # value = 'usermail,password'
    # t = sql_fetchjj(con,name,value)
    # print(t)
    # print(t[0][0])
    # t = ('NAMES TEXT', 'PHONES INT', 'JYFWS TEXT', 'CPMS TEXT', 'SLS TEXT', 'LXS TEXT', 'XHS TEXT')
    # bname = '91zsw1'
    # create_table(con,bname,t)
    con = sql_connection('test')
    bname = 'bossdb'
    t = '(id INT, name txt)'
    create_table(con, bname, t)
    str = '职位描述\n工作日期：不限\n工作时间：不限\n结算方式：完工结\n寻找具备个人IP潜质的讲师，我们有专业的课研团队帮你梳理课程体系和卖点，包装和打造讲师ip。\n职责：\n1，参与策划个人IP\n2，参与创作和录制干货短视频\n3，参与直播课\n4，协助布置课程作业和课后服务，答疑。\n要求：\n1，拥有该行业名校或名企背景，参与过重点项目背书。\n2，在某个领域（家育，心理，职场，职教等）深耕5年以上，课题有干货，具备差异化和竞争力；\n3，3年以上授课经验，擅长线上授课，镜头前有个人风格。\n4，热爱教学工作，愿意在教学领域深耕。\n5，学历不限，普通话标准。'
    str = (6,str)
    print(type(str))
    print(len(str))
    t = len(str)
    t = '?,'*t
    t = t[:-1]
    print(t)

    cursor = con.cursor()
    #strSql = "update bossdb set name= ? where id = 2"
    #cursor.execute("update bossdb set name= ? where id = 2",str)
    #cursor.execute(f"INSERT into bossdb values(?,?)",str)

    sql_insert(con,bname,str)
    con.commit()