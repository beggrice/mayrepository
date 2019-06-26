# -*- coding: utf-8 -*-
#スクレイピングに必要なライブラリはrequets,bs4の二つ
import requests
import re
from bs4 import BeautifulSoup
url="https://search.nifty.com/imagesearch/search?cflg=検索&select=1&chartype=&q=%s&xargs=&img.fmt=all&img.imtype=color&img.filteradult=no&img.type=all&img.dimensions=all&start=%s&num=20"
keywords=[]
keyword=input("")
keywordn=input("")
keywords.append(keyword)

pages=[0,20,40,60,100,120,180,160,200,220,240,260,280,300]
i=0
for keyword in keywords:
    for page in pages:
        r=requests.get(url%(keyword,page))

        soup = BeautifulSoup(r.text,"lxml")
        links=soup.findAll("a",href=re.compile("jpg"))
    
    
    
        for link in links:
            link=requests.get(link["href"])
            #print(link)
            i=i+1
            with open(str('D:\\nogizaka\\')+str(keywordn)+str("\\")+str(i)+str('.jpeg'),'wb')as file:
                        file.write(link.content)