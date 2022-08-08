import csv

import csv
import os

def creatcsv(n,t):  #输入表名，和数据头
    if os.path.isfile(f'{n}.csv'):
        print(f'{n}.csv已创建')
    else:
        with open(f'{n}.csv','w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(t)
        print(f'{n}.csv创建成功')


def xieru(n,t,y): #输入表名，和数据组（记得是JSON格式），数据头
    with open(f'{n}.csv','a',errors='ignore',newline='') as f:
        fieldnames = y
        writer =csv.DictWriter(f,fieldnames=fieldnames)
        writer.writerow(t)
    print(f'{n}.csv,写入成功')

if __name__ == '__main__':
    #creatcsv('book')
    t = {"书名":"1",
         "作者":"2",
        "出版社":"3",
        "简介":"4"}
    xieru(t)