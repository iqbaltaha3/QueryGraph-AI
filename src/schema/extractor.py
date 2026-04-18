import sqlite3

def get_schema(db_path: str):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    schema = {}

    # step 1 -> Get all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]

        # step 2 -> Get columns of each table
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns_info = cursor.fetchall()

        columns = [
            {
                "name":col[1],
                "type":col[2]
            } 
            for col in columns_info
        ]

        schema[table_name] = columns

    conn.close()
    return schema
