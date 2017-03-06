# -*- coding: utf-8 -*-
import sqlite3
#Подключение к базе
conn = sqlite3.connect('my.sqlite')
#Создание курсора
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS stocks
             (name text, txt text, time text, status text)''')



SQL_SELECT = '''
    SELECT
        id, short_url, original_url, created
    FROM
        shortener
'''
purchases = [('6662006-01-05','666BUY','RHAT',100),
             ('6662006-04-05', '666BUY', 'MSFT', 100),
             ('6662006-04-06', '666SELL', 'IBM', 500),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?)', purchases)



for row in c.execute('SELECT * FROM stocks ORDER BY txt'):
        print(row)



# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

info = ["id", "name", "txt", "time", "status"]