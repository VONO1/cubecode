# -*- coding: utf-8 -*-
import sqlite3
#Подключение к базе
conn = sqlite3.connect('my.sqlite2')
#Создание курсора
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS stocks
             (name text, txt text, time text, status text)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100)")
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
print(c)
info = ["id", "name", "txt", "time", "status"]