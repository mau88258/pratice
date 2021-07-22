"""---網址解析---"""
# urllib套件中 urlparse函式(解析網址內容)

#scheme 通訊協定
#netloc 網站名稱
#path   環境路徑
#params 參數
#query  查詢字串
#port   查詢通訊port

from urllib.parse import urlparse
url = "https://www.lccnet.tv/pages/watch.aspx?v=P057070"
info = urlparse(url)
print(info)
