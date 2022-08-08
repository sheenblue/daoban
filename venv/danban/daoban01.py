# -*- coding: utf-8 -*-
# @Author : sheen
# @Time   : 2022-08-04
# @FILE   : daoban01.py

import requests
from bs4 import BeautifulSoup

def html(url):
  #url = "https://chenwenb.com/new"

  payload = {}
  headers = {
    'authority': 'chenwenb.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,ru;q=0.5',
    'cache-control': 'max-age=0',
    'cookie': 'wordpress_logged_in_24ebd2da04faaf68d8e7cf9039382428=u7091927861188255%7C1660013931%7CcJiWZ76RK7UqB9c29ExebaBChaDbSuTkGtVuzrFSPBt%7Cf9c611979ac4e149932f369da01cfe3463594c34c34c4843aebbcda778ba7a5a',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  response.encoding='utf-8'
  #return response.text

  soup = BeautifulSoup(response.text,'lxml')

  return soup



if __name__ == '__main__':
    num = 10
    url = f"https://chenwenb.com/new/page/{num}"
    soup = html(url)

    # 获取视频分类
    class3 = soup.find_all(class_='cat')

    class1  =  soup.find(id = 'posts')

    class1 = class1.find_all('h3')
    for i in range(len(class1)):
      class2 = class1[i].find('a')
      print(class2.string)
      print(class2['href'])
      class4 = class3[i].string
      print(class4)



