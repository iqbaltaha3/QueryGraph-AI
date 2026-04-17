import sqlite3
import os

def save_to_sqlite(df, db_path, file_path):

    # extract filename
    file_name = os.path.basename(file_path)

    # remove extension
    table_name = os.path.splitext(file_name)[0]

    # clean table name
    table_name = table_name.lower().replace(" ","_")

    # save to db
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()

    print("Table created -> ", table_name)