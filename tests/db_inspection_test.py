import sqlite3

DB_PATH = "data/data.db"


def inspect_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("\n===== DATABASE INSPECTION START =====\n")

    # 1. List all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    if not tables:
        print("No tables found in database.")
        return

    print(f"Tables found: {[t[0] for t in tables]}\n")

    # 2. Inspect each table
    for table in tables:
        table_name = table[0]
        print(f"--- Table: {table_name} ---")

        # Get schema
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()

        print("Columns:")
        for col in columns:
            print(f"  - {col[1]} ({col[2]})")

        # Get sample data
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 3;")
        rows = cursor.fetchall()

        print("Sample rows:")
        for row in rows:
            print(f"  {row}")

        print("\n")

    conn.close()

    print("===== DATABASE INSPECTION END =====\n")


if __name__ == "__main__":
    inspect_database()