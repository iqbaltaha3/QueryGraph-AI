from src.schema.extractor import get_schema
from src.retrieval.retriever import retrieve_relevant_schema

# Load schema
schema = get_schema("data/data.db")

# =========================
# DEBUG: CHECK SCHEMA STRUCTURE
# =========================
print("\n===== SCHEMA CHECK =====\n")

for table, cols in schema.items():
    print(f"Table: {table}")
    print("Type of cols:", type(cols))

    if len(cols) > 0:
        print("First element:", cols[0])
        print("Type of first element:", type(cols[0]))
    break


# =========================
# TEST QUERIES
# =========================
queries = [
    "total sales by region",
    "customer names in delhi",
    "product price",
    "employee salary"
]

# =========================
# RUN RETRIEVAL
# =========================
for query in queries:
    relevant_schema = retrieve_relevant_schema(query, schema)

    print("\n========================")
    print("Query:", query)

    # =========================
    # DEBUG: CHECK RETRIEVER OUTPUT
    # =========================
    print("\nRETRIEVER OUTPUT:\n", relevant_schema)

    for table, cols in relevant_schema.items():
        print(f"\nTable: {table}")
        print("Type of cols:", type(cols))

        if len(cols) > 0:
            print("First element:", cols[0])
            print("Type of first element:", type(cols[0]))

        # =========================
        # FINAL OUTPUT
        # =========================
        print("\nColumns:")
        for col in cols:
            print(f"  - {col['name']} ({col['type']})")