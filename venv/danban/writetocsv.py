import csv

import csv

def creatcsv(n,t):  #输入表名，和数据组
    with open(f'{n}.csv','w') as f:
        writer = csv.writer(f)
        writer.writerow(t)
    print('创建成功')


def xieru(n,t): #输入表名，和数据组
    with open(f'{n}.csv','a',errors='ignore',newline='') as f:
        fieldnames = t
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