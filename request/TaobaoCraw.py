import requests
from bs4 import BeautifulSoup
import bs4
def getHTML(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("url出现问题")
        return ""    
def html2List(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    links = soup.find('div',id='page').find_all('div')#
    print(type(links))
def main():
    url = "https://s.taobao.com/search?q=%E8%B7%91%E9%9E%8B&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20170327&ie=utf8"
    html = getHTML(url)
    ulist = []
    html2List(ulist, html)
main()





