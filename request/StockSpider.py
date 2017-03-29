#http://quote.eastmoney.com/stocklist.html
#https://gupiao.baidu.com/stock/
import requests
from bs4 import BeautifulSoup
import re
#获得页面的源码
def getHtml(url,code="utf-8"):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""
#从页面源码中得到股票的编号
def getStockList(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    body = soup.find_all('a')
    for i in body:
        try:
            href = i.attrs['href']
            id = re.findall(r"s[hz][\d]{6}", href)[0]
            ulist.append(id)
        except:
            continue

def getStockInfo(ulist,url,file_path):
    info_list=[]
    count=0
    #print(ulist)
    for i in range(50):
        info_url = url+ulist[i]+'.html'
        #print(info_url)
        count=count+1
        html = getHtml(info_url)#得到股票详情页面
        if(html!=''):
            try:
                soup = BeautifulSoup(html,'html.parser')
                name_temp = soup.find_all('a', class_='bets-name')[0].text
                name = choose_name(name_temp)
                #name =re.findall(r'\n[\s]+.*?\n', name_temp)[0]
                price = soup.find_all('strong',class_="_close")[0].string
                #序列，名称，编号，价钱
                info_list.append([i,name,ulist[i],price])
                #print("test")
                print("已经进行了百分之:%.2f"%(count*100/50))
            except:
                continue
    writeFile(info_list, file_path)
    return info_list
def writeFile(ulist,file_path):
    with open(file_path, 'a', encoding='utf-8') as f:
        for i in range(len(ulist)):
            f.write( str(ulist[i]) + '\n' )
            
def choose_name(str):
    p = re.compile(r'\n[\s]*(.*?)[\s]*\n')
    p2 = re.compile(r'.*?[(]')
    m=p.match(str)
    name1 = m.group(0).strip()#获得 东方财富(34344)
    m2=p2.match(name1)
    name = m2.group(0).strip()[0:m2.end()-1]#获得东方财富
    return name
def main():
    list_url = 'http://quote.eastmoney.com/stocklist.html'
    info_url = 'https://gupiao.baidu.com/stock/'
    html = getHtml(list_url,"GB2312")
    file_path= 'C:/Users/mlq/Desktop/temp.txt'
    ulist = []#股票编号列表
    getStockList(ulist, html)
    infolist = getStockInfo(ulist,info_url,file_path)#股票信息列表
    #print(infolist)
#     for i in range(len(infolist)):
#          print(infolist[i])
#     writeFile(ulist, file_path)

main()





