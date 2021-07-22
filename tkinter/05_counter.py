"""實作---計數器"""

import tkinter as tk

def add1():
    global num
    num += 1
    yrlabeltxt.set("目前計數為:"+str(num))


yrwin = tk.Tk()

yrlabeltxt = tk.StringVar()
yrbtntxt = tk.StringVar()
num = 0

mylabel = tk.Label(yrwin,textvariable=yrlabeltxt,font=("新細明體",13),fg="blue")
yrlabeltxt.set("目前計數為0")
mylabel.pack()


mybtn = tk.Button(yrwin,textvariable=yrbtntxt,command=add1)
yrbtntxt.set("+1")
mybtn.pack()

yrwin.mainloop()