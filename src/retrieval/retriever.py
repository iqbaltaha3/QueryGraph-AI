SYNONYMS = {
    "revenue": ["sales", "amount", "price"],
    "sales": ["revenue", "amount"],
    "customer": ["customer_id", "name"],
    "location": ["city"],
    "date": ["order_date"]
}

STOPWORDS = {
    "by", "in", "on", "at", "to", "for",
    "of", "the", "a", "an", "total"
}


def retrieve_relevant_schema(query: str, schema: dict):
    query_words = [
        word for word in query.lower().split()
        if word not in STOPWORDS
    ]

    print("\nQuery words:", query_words)

    relevant = {}

    for table, columns in schema.items():
        matched_columns = {}
        table_score = 0

        for col in columns:
            col_name = col["name"].lower()
            description = col.get("description", "").lower()
            sample_values = [
                str(v).lower() for v in col.get("sample_values", [])
            ]

            col_score = 0

            for word in query_words:

                # 1. direct match (name or description)
                if word in col_name or word in description:
                    col_score += 2

                # 2. sample value match
                if any(word in val for val in sample_values):
                    col_score += 3

                # 3. synonym match
                if word in SYNONYMS:
                    for syn in SYNONYMS[word]:
                        if syn in col_name or syn in description:
                            col_score += 2

            # store column if it got any score
            if col_score > 0:
                matched_columns[col["name"]] = {
                    **col,
                    "match_score": col_score
                }
                table_score += col_score

        print(f"Table: {table}, Score: {table_score}")

        if table_score > 0:
            relevant[table] = {
                "columns": list(matched_columns.values()),
                "score": table_score
            }

    # sort tables by relevance score
    sorted_tables = sorted(
        relevant.items(),
        key=lambda x: x[1]["score"],
        reverse=True
    )

    # keep top 2 tables (baseline for now)
    final_result = {
        table: data["columns"]
        for table, data in sorted_tables[:2]
    }

    return final_result