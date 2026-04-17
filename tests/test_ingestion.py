import os

from src.ingestion.file_loader import load_file
from src.ingestion.cleaner import clean_columns
from src.ingestion.to_sqlite import save_to_sqlite

DATA_FOLDER = "data"

# Detect all CSV and Excel files
files = [
    os.path.join(DATA_FOLDER, f)
    for f in os.listdir(DATA_FOLDER)
    if f.endswith(".csv") or f.endswith(".xlsx")
]

for file_path in files:
    print(f"\nProcessing file: {file_path}")
    
    df = load_file(file_path)
    df = clean_columns(df)
    table_name = save_to_sqlite(df, "data/data.db", file_path)
    
    print(f"Loaded → table: {table_name}")