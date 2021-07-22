"""複選按鈕checkbox"""

import tkinter as tk

def checkbox():
    global ch,like
    showmsg = "您的興趣是: "
    for i in range(0,len(ch)):
        if (ch[i].get()==1):
            showmsg = showmsg + like[i] + "  ,"
    msglabel.set(showmsg)        

yrwin = tk.Tk()

ch=[]
like=["聽音樂","打球","看電視"]
msglabel = tk.StringVar()

mylabel = tk.Label(yrwin,text="請選擇你的興趣:",font=("",15))
mylabel.pack()
for i in range(0,len(like)):
    num=tk.IntVar()
    ch.append(num)
    mycheckbutton = tk.Checkbutton(yrwin,text=like[i],variable=ch[i],command=checkbox)
    mycheckbutton.pack()

answerlabel = tk.Label(yrwin,textvariable=msglabel)
answerlabel.pack()

yrwin.mainloop()