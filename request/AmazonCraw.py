import requests
import os
from nt import mkdir
if __name__=='__main__':
    dir = 'C:\\Users\\mlq\\Desktop\\'
    url = "http://image.nationalgeographic.com.cn/2017/0322/20170322120238770.jpg"
    path = dir+url.split('/')[-1]
    if not os.path.exists(dir):
        mkdir(dir)
    if not os.path.exists(path):
        #kv = {'User-Agent','Mozella/5.0'}
        #headers=kv
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
    else:
        print('文件已经存在了')   