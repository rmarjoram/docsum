import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

print(cur.execute("SELECT * FROM user").fetchall())
print(cur.execute("SELECT * FROM document").fetchall())

connection.commit()
connection.close()