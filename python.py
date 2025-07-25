import mysql.connector

conn=mysql.connector.connect(host='localhost', username='root', password='@p@a@l@a@k@3005', database='connection')
my_cursor=conn.cursor()

conn.commit()
conn.close()

print("Connection successfully created!")