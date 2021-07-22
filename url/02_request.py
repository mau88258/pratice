import requests
url = "https://www.cakenobel.com.tw/"

html = requests.get(url)
#print(html.text)

word = html.text.splitlines()  #讀取文字並拆開放入值變數中,值為陣列 

time = 0

for txt in word:               #尋找特定字出現該網頁幾次
    if "借書" in txt : time += 1
print(time)