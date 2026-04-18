SYNONYMS = {
    "revenue": ["sales", "amount", "price"],
    "sales": ["revenue", "amount"],
    "customer": ["customer_id", "name"],
    "location": ["city"],
    "date": ["order_date"]
}

STOPWORDS = {"by", "in", "on", "at", "to", "for", "of", "the", "a", "an", "total"}

def is_match(word, col_name):
    col_name = col_name.lower()

    # exact match
    if word == col_name:
        return True

    # word boundary match (better than substring)
    if word in col_name.split("_"):
        return True

    # synonyms
    if word in SYNONYMS:
        return any(syn in col_name for syn in SYNONYMS[word])

    return False


def retrieve_relevant_schema(query: str , schema: dict):
    query_words = [word for word in query.lower().split()
                   if word not in STOPWORDS]
    print("\nQuery words:", query_words)

    relevant = {}

    for table,columns in schema.items():
        matched_columns = {}

        for col in columns:
            col_name = col["name"].lower()

            # match any word in query
            for word in query_words:
                if is_match(word,col_name):
                    matched_columns[col["name"]] = col
                    break

        if len(matched_columns) >= 2:
            relevant[table] = {
                "columns": list(matched_columns.values()),
                "score": len(matched_columns)
                }
        print(f"Table: {table}, Score: {len(matched_columns)}")

    # sort tables by score
    sorted_tables = sorted(
        relevant.items(),
        key=lambda x: x[1]["score"],
        reverse=True
    )

    # keep top 2 tables (simple baseline)
    keep_tables = 2
    final_result = {}

    for table, data in sorted_tables[:keep_tables]:
        final_result[table] = data["columns"]

    return final_result