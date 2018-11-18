from tkinter import *
import pymysql
from tkinter import messagebox

root = Tk()

usn = StringVar()
name = StringVar()
age = IntVar()
branch = StringVar()

l1 = Label(root,text='USN')
l2 = Label(root,text='NAME')
l3 = Label(root,text='AGE')
l4 = Label(root,text='BRANCH')

e1 = Entry(root,textvariable=usn)
e2 = Entry(root,textvariable=name)
e3 = Entry(root,textvariable=age)
e4 = Entry(root,textvariable=branch)

def insert():
    db = pymysql.connect(host="localhost",port=3307,user="root",password="",db="dbStudent" )
    sql = "insert into student values('%s','%s',%d,'%s')" %(usn.get(),name.get(),age.get(),branch.get())
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        messagebox.showinfo('Success','Successfully inserted!')
    except:
        messagebox.showerror('Error','Unsuccessful')
    db.close()

def search():
    t = Toplevel()
    s = StringVar()
    lb1 = Label(t,text='Enter USN to search')
    et1 = Entry(t,textvariable=s)

    def find():
        db = pymysql.connect(host="localhost",port=3307,user="root",password="",db="dbStudent" )
        sql = "select * from student where usn = '%s'" %(s.get())
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                usn = row[0]
                name = row[1]
                age = row[2]
                branch = row[3]
            messagebox.showinfo('Success','Name = %s, USN = %s, Age = %d, Branch = %s' %(name,usn,age,branch))
        except:
            messagebox.showerror('Error','Unsuccessful')
        db.close()

    btn = Button(t,text='Search',command=find)
    lb1.grid(row='1',column='0')
    et1.grid(row='1',column='1')
    btn.grid(row='2',column='0')
    t.mainloop()

b1 = Button(root,text='Insert',command=insert)
b2 = Button(root,text='Search',command=search)

l1.grid(row='0',column='0')
e1.grid(row='0',column='1')
l2.grid(row='1',column='0')
e2.grid(row='1',column='1')
l3.grid(row='2',column='0')
e3.grid(row='2',column='1')
l4.grid(row='3',column='0')
e4.grid(row='3',column='1')
b1.grid(row='4',column='0')
b2.grid(row='4',column='2')

root.mainloop()
