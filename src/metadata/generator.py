import sqlite3

def get_sample_values(conn, table, column, limit=5):
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT DISTINCT {column} FROM {table} LIMIT {limit}")
        values = [row[0] for row in cursor.fetchall()]
        return values
    except:
        return []
    

def generate_metadata(db_path: str, schema: dict):
    conn = sqlite3.connect(db_path)

    enriched_schema = {}

    for table, columns in schema.items():
        enriched_schema[table] = []

        for col in columns:
            col_name = col["name"]

            metadata = {
                "name": col_name,
                "type": col["type"],
                "description": f"{col_name} of {table}",
                "sample_values": get_sample_values(conn, table, col_name)
            }

            enriched_schema[table].append(metadata)

    conn.close()
    return enriched_schema