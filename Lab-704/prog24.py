from tkinter import *
import math

root = Tk()

var1 = DoubleVar()
var2 = DoubleVar()
var3 = DoubleVar()
res = DoubleVar()

def calculate():
    investAmt = var1.get()
    year = var2.get()
    annualInterestRate = var3.get()
    monthlyInterestRate = annualInterestRate / 1200
    futureValue = investAmt * math.pow((1 + monthlyInterestRate),year * 12)
    res.set(futureValue)

label1 = Label(root,text='Investment Amount')
invs = Entry(root,textvariable=var1)
label2 = Label(root,text='Years')
yrs = Entry(root,textvariable=var2)
label3 = Label(root,text='Annual Interest Rate')
air = Entry(root,textvariable=var3)
label4 = Label(root,text='Future Value')
result = Label(root,textvariable=res)
butt = Button(root,text="Calculate",command=calculate)

label1.grid(row='1',column='1')
invs.grid(row='1',column='2')
label2.grid(row='2',column='1')
yrs.grid(row='2',column='2')
label3.grid(row='3',column='1')
air.grid(row='3',column='2')
label4.grid(row='5',column='1')
result.grid(row='5',column='2')
butt.grid(row='6',column='2')

root.mainloop()
