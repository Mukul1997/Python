from tkinter import *
import random as ran

root = Tk()

bounds = [50,50,250,250]
extent = [0,90,180,270]
colors = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]

canvas = Canvas(root,width=300,height=300,bg='white')
for i in extent:
    canvas.create_arc(bounds,start=i,extent=35,fill=ran.choice(colors))
canvas.pack()

root.mainloop()
