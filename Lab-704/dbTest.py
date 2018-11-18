#!/usr/bin/python3
# import PyMySQL
import pymysql

# Open database connection
db = pymysql.connect(host="localhost",port=3307,user="root",password="",db="dbStudent" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
# cursor.execute("SELECT VERSION()")
def insert():
    try:
        sql = "INSERT INTO student VALUES('%s','%s',%d,'%s')" %(usn,name,age,branch)
        cursor.execute(sql)
        print('done')
        db.commit()
    except:
        print('Error')    

# Fetch a single row using fetchone() method.
def find():
    cursor.execute("SELECT * FROM student")
    data = cursor.fetchall()
    for i in data:
        print(i)

print('1.Insert 2.Find  Enter choice:')
ch = int(input())

if ch == 1:
    usn = input('Usn:')
    name = input('Name:')
    age = int(input('Age:'))
    branch = input('Branch:')
    insert()
else:
    find()

# disconnect from server
db.close()
