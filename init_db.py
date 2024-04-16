import sqlite3

connection = sqlite3.connect('database.db')

cur = connection.cursor()

with open('schema.sql') as f:
    script = f.read()
    cur.executescript(script)

cur.execute("INSERT INTO user (UserName, UserEmail) VALUES (?, ?)", ('Test User', 'Test.User@gmail.com'))
cur.execute("INSERT INTO document (UserID, docInput, docSum) VALUES (?, ?, ?)", (1, 'This is document text, please summarize it.', 'This is a summary of the document text you entered.'))


connection.commit()
connection.close()
