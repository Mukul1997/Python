from tkinter import *
import random as ran

root = Tk()

colors = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]

var1 = IntVar()
var2 = IntVar()

def draw():
    canvas.delete(ALL)
    if var1.get():
        if var2.get():
            canvas.create_rectangle(50,50,250,200,fill=ran.choice(colors))
        else:
            canvas.create_rectangle(50,50,250,200)
    else:
        if var2.get():
            canvas.create_oval(50,50,250,200,fill=ran.choice(colors))
        else:
            canvas.create_oval(50,50,250,200)

canvas = Canvas(root,width=300,height=300,bg='white')
frame = Frame(root)
r1 = Radiobutton(frame,text="Rekt",variable=var1,value=1,activeforeground='green',command=draw)
r2 = Radiobutton(frame,text="Oval",variable=var1,value=0,activeforeground='green',command=draw)
c1 = Checkbutton(frame,text="Fill",variable=var2,offvalue=0,onvalue=1,activeforeground='green',command=draw)
r1.grid(row='1',column='1')
r2.grid(row='1',column='2')
c1.grid(row='1',column='3')
canvas.pack()
frame.pack()

root.mainloop()
