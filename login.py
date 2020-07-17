#!C:\Users\mis\AppData\Local\Programs\Python\Python38-32\python.exe
print("content-type: text/html\n\n")

import cgi,cgitb
import mysql.connector

print("<h1>welcome to python file</h1>")
print("<hr>")
print("<h1>using input tag</h1>")
print("<body bgcolor='orange'>")

form = cgi.FieldStorage()


email=form.getvalue("email")
password=form.getvalue("password")


con=mysql.connector.connect(user='root',password='',host='localhost',database='compilersacademy')
cur=con.cursor()

cur.execute("select * from customer where email='{}' and password='{}'".format(email,password))
data=cur.fetchone()
if data:
    print("=======Welcome {}========".format(data[1]))

else:
    print("<h1>Wrong Credentials..</h1>")
con.commit()
cur.close()
con.close()
