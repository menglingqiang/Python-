# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import bs4
import re
import sys
def getHTML(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("url下载出现问题")
        return ""    
def html2List(ulist,html):
    #soup = BeautifulSoup(html,'html.parser')
    #links = soup.find('div',id='page').find_all('div')#
    try:
        #print('parser begin')
        nlist = re.findall(r'\"raw_title\":\".*?\"', html)
        plist = re.findall(r'\"view_price\":\"[\d\.]*\"',html)#可以
        slist = re.findall(r'\"view_sales\":\".*?\"', html)
        #print(nlist)
        #print(plist)
        #print(slist)
        #print(len(nlist))
        for i in range(len(nlist)):
            n = eval(nlist[i].split(':')[1])
            p = eval(plist[i].split(':')[1])
            s = eval(slist[i].split(':')[1])
            ulist.append([n,p,s])
    except:
        print('')
       
    #
def printList(ulist):
    tplt = "{:4}\t{:8}\t{:16}\t{:8}"
    print(tplt.format("序号", "商品名称", "价格","销量"))
    count = 0
    for g in ulist:
        count = count + 1
        print(tplt.format(count, g[0], g[1],g[2]))
def main():
    goods = input("Please input goods you want to search:\n")
    print("正在搜索"+goods)
    url = "https://s.taobao.com/search?q="+goods#中文搜索没有解决
    ulist = []
    deep = 3
    for i in range(deep):
        try:
            temp = url+"&s="+str(i*44)
            #print(temp)
            html = getHTML(temp)
            html2List(ulist, html)
        except:
            continue
    printList(ulist)
main()





