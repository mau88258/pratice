"""圖形化視窗tkinter基礎設定"""

import tkinter as tk
"""---------------------視窗外框設定-------------------------"""
yrwin = tk.Tk()             #創造圖形化視窗
yrwin.geometry('700x300')   #長寬設定，乘必須要用小寫x
yrwin.title("myname")       #視窗名設定

"""---------------------內容物設定---------------------------"""
#元件設定Label(主視窗名稱,text=內容文字,font=文字設定,bg=背景顏色,fg=字體顏色)
yrlabel = tk.Label(yrwin,text="哈囉",font=("標楷體",10),bg="blue",fg="white")  
#元建置入pack()
yrlabel.pack()   
#按鈕設定Button(主視窗名稱,text=按鈕文字,font=文字設定,bg=背景顏色,command=按鈕點擊後呼叫)
yrbtn = tk.Button(yrwin,text="按我!",bg="green",font=("新細明體",15))
yrbtn.pack()




yrwin.mainloop()            #視窗重複執行，維持開啟狀態