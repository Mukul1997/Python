#!/usr/bin/python
import cgi,cgitb

form = cgi.FieldStorage()

if form.getvalue("name"):
    entry = form.getvalue("name")

print("Content-type:text/html \n")
print("<html>")
print("<body>")
print("<h1>Your name is "+entry+"</h1>")
print("</body></html>")
