import sqlite3

conn = sqlite3.connect('DevOps.db')
cursor = conn.cursor()
cursor.execute('SELECT*from product_info')
records=cursor.fetchall()
print(records)