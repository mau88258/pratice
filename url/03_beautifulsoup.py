#beautifulsoup 可以擷取較複雜的資料

#建立beautifulsoup 物件型別 bsp
#bsp = BeautifulSoup(網頁原始碼,'html.parser')

import requests
from bs4 import BeautifulSoup

url = "https://www.cakenobel.com.tw/"
html = requests.get(url)

bsp = BeautifulSoup(html.text,'html.parser')
#print(bsp)
#print(bsp.text)    #去除html部分

datatitle = bsp.select("title")
print(datatitle)