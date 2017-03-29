import requests
import re
def choose_name(str):
    p = re.compile(r'\n[\s]*(.*?)[\s]*\n')
    p2 = re.compile(r'.*?[(]')
    m=p.match(str)
    name1 = m.group(0).strip()#获得 东方财富(34344)
    m2=p2.match(name1)
    name = m2.group(0).strip()[0:m2.end()-1]
    return name
name = choose_name('\n      测试(4545)     \n')
print(name)
# name = '\n      测试(4545)     \n'
# p=re.compile(r'\n[\s]*(.*?)[\s]*\n')
# m=p.match(name)
# temp=m.group(0).strip()
# print(temp)
# 
# p2 = re.compile(r'.*?[(]')
# m2=p2.match(temp)
# test = m2.group(0).strip()[0:m2.end()-1]
# print(test)
#temp2=m2.group(0).strip()
#print(temp2)