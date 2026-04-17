from src.ingestion.file_loader import load_file
from src.ingestion.cleaner import clean_columns
from src.ingestion.to_sqlite import save_to_sqlite
import sqlite3

# step 1 -> load file
df = load_file("data/sample.csv")

# step 2 -> clean columns
df = clean_columns(df)

# step 3 -> save to sqlite
save_to_sqlite(df, "data/data.db", "data/sample.csv")

# step 4 -> verify 
conn = sqlite3.connect("data/data.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM sales LIMIT 5")
rows = cursor.fetchall()
conn.close()

print(rows)