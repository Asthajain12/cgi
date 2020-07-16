#!C:\Users\mis\AppData\Local\Programs\Python\Python38-32\python.exe
print("content-type: text/html\n\n")

import cgi,cgitb
import mysql.connector

print("<h1>welcome to python file</h1>")
print("<hr>")
print("<h1>using input tag</h1>")
print("<body bgcolor='orange'>")

form = cgi.FieldStorage()

first_name=form.getvalue("first_name")
last_name=form.getvalue("last_name")
email=form.getvalue("email")
password=form.getvalue("password")
address=form.getvalue("address")
address2=form.getvalou("address2")
city=form.getvalue("city")
state=form.getvalue("state")
pin=form.getvalue("pin")

con=mysql.connector.connect(user='root',password='',host='localhost',database='compilersacademy')
cur=con.cursor()

cur.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(first_name,last_name,email,password,address,address2,city,state,pin))
con.commit()
cur.close()
con.close()
print("<h1>record inserted sucessful</h1>")