# sqlite3 is built-in to Python.
# The entire database is stored in a file.
# It is lightweight but a little slower and less secure.
import sqlite3

connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("INSERT INTO users (name) VALUES ('Mr McLeod')")
cursor.execute("SELECT * FROM users")

# result = cursor.fetchone()
result = cursor.fetchall()
# connection.commit()

cursor.close()
connection.close()

print(result)
