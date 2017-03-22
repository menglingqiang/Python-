from bs4 import BeautifulSoup
import requests
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,'html.parser')
for child in soup.body.contents:
    print(child)