#!/usr/bin/python
# -*- coding:UTF-8 -*-
import pymysql

db = pymysql.connect("localhost","root","123",charset='utf8')
cursor = db.cursor()
cursor.execute("USE TestSQL;")


cursor.execute("SELECT * FROM EMPLOYEE;")
#cursor.execute("INSERT INTO EMPLOYEE VALUES('LHL','LIHONGLIANG','30','0','3.3');")
data = cursor.fetchone()
print(data)
db.close()