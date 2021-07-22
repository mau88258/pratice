"""動態變數textvarible"""

import tkinter as tk

def answer():
    yrtextvar.set("阿拉伯數字")

yrwin = tk.Tk()
yrwin.geometry("500x500")
yrwin.title("簡易答題設計")

"""設定動態變數型態textvarible"""
#有支援三種方式"""
#tk.StringVar()
#tk.IntVar()
#tk.Double()
yrtextvar = tk.StringVar()

yrbtn = tk.Button(yrwin,textvariable=yrtextvar,command=answer)

"""動態變數設定與獲取"""
#變數.set() --> 變數值設定
#變數.get(字串)
yrtextvar.set("什麼字全世界通用?")
yrbtn.pack()


yrwin.mainloop()