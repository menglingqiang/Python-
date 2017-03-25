# encoding = UTF-8
import requests
import bs4
from bs4 import BeautifulSoup
def downUrl(url):#下载url的内容
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('url下载错误')
        return ''
def url2List(ulist,html_content):#将url中的内容解析成list
    soup = BeautifulSoup(html_content,'html.parser')
    for list in soup.find('tbody').children:
        if(isinstance(list,bs4.element.Tag)):
            tds =list('td')
            ulist.append([tds[1].string,tds[2].string,tds[3].string,tds[4].string])#组合成一个list放进去
def printList(ulist,num):#将list中的数据打印出前num项
    tplt = "{0:{5}^10}\t{1:{5}^10}\t{2:{5}^10}\t{3:{5}^10}\t{4:{5}^10}"
    print(tplt.format("排名","学校名称","省份","总分","指标得分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(i+1,u[0],u[1],u[2],u[3],chr(12288)))
def main():
    url ="http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html"#2017的html有bug 排名的td没有写完整，所以手动添加排名
    html_content = downUrl(url)
    ulist = []
    url2List(ulist, html_content)
    printList(ulist, 20)
main()
    
    
# if __name__=='__main__':
#     html_content = downUrl("http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html")
#     soup = BeautifulSoup(html_content,'html.parser')
#     count = 0
#     for tr in soup.find('tbody').children:
#         print(tr)
#         print(type(tr))
#         count = count+1
#         if(count==4):
#             break
        
    
    
    