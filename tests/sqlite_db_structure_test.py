import sqlite3

conn = sqlite3.connect("data/data.db")
cursor = conn.cursor()

# see tables in the db
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

# see columns of a table 
cursor.execute("PRAGMA table_info(sample);")
print(cursor.fetchall())