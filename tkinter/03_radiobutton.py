"""擇一按鈕Radiobutton(單選)"""

import tkinter as tk

def mymsg():
    foodmsg.set("您最喜歡的主食為"+choosefood.get()) #利用get獲取choosefood中的值,型態為StringVar



yrwin = tk.Tk()
choosefood = tk.StringVar()
foodmsg = tk.StringVar()

foodlabel = tk.Label(yrwin,text="請選擇你最愛的主食",font=("新細明體",15),bg="gray",fg="white")
foodlabel.pack()

"""設定擇一按鈕"""
#擇一按鈕Radiobutton(主視窗名稱,text=按鈕文字,value=回傳值,variable=回傳值位址,command=按鈕按下執行命令)
ch01 = tk.Radiobutton(yrwin,text="飯",value="飯",variable=choosefood,command=mymsg)
ch01.pack()
ch02 = tk.Radiobutton(yrwin,text="麵",value="麵",variable=choosefood,command=mymsg)
ch02.pack()

ch02.select()   #擇一按鈕變數.select 預設選取值
mymsg()
msglabel = tk.Label(yrwin,textvariable=foodmsg,fg="blue")
msglabel.pack()

yrwin.mainloop()