"""實作---名字顯示器"""
#讓使用者輸入姓名
#輸入完後按下確認按鈕
#如果輸入值為空值
#下方必須顯示提示訊息"不能為空，請輸入姓名"
#否則下方會顯示"歡迎光臨+(使用者姓名)+您好"

import tkinter as tk

def checkname():
    if (name.get()!= ""):
        msg = "歡迎光臨  " + str(name.get()) +"您好!"
        alartmsg.set(msg)
    else:
        alartmsg.set("不能為空，請輸入姓名")


yrwin = tk.Tk()
name = tk.StringVar()
alartmsg = tk.StringVar()

inputlable = tk.Label(yrwin,text="請輸入姓名")
inputlable.pack()

#使用者輸入tk.Entry(主視窗名稱,動態文字) 輸入會存值於textvariable
userkeyin = tk.Entry(yrwin,textvariable=name)
userkeyin.pack()

yrbtn = tk.Button(yrwin,text="確定!",command=checkname)
yrbtn.pack()

msglabel = tk.Label(yrwin,textvariable=alartmsg)
msglabel.pack()

yrwin.mainloop()