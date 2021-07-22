"""文字區塊INSERT"""
#tk.insert  字串加入至文字方塊
#tk.end     字串加入至文字方塊，但此行過後加入結束
#元件名稱.insert(tk.insert/end, 字串)
import tkinter as tk 

yrwin = tk.Tk()

#文字方塊Text(主視窗名稱)
yrtxt = tk.Text(yrwin)

yrtxt.insert(tk.INSERT,"第一行的文字內容,\n")
yrtxt.insert(tk.INSERT,"第二行的文字內容,\n")
yrtxt.insert(tk.END,"最後一行的文字內容")
yrtxt.config(state=tk.DISABLED)         #元件.config(state)使用者能否更改文字方框內容，預設為NORMAL
yrtxt.pack()

yrwin.mainloop()