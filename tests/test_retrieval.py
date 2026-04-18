from src.schema.extractor import get_schema
from src.metadata.generator import generate_metadata
from src.retrieval.retriever import retrieve_relevant_schema


def debug_schema(schema):
    print("\n===== DEBUG SCHEMA CHECK =====")
    for table, cols in schema.items():
        print(f"\nTable: {table}")
        print("Type of cols:", type(cols))
        if len(cols) > 0:
            print("First element:", cols[0])
            print("Type of first element:", type(cols[0]))
        break  # only check one table


def run_tests():
    # Step 1: Load schema
    schema = get_schema("data/data.db")

    # Step 2: Generate metadata (IMPORTANT)
    enriched_schema = generate_metadata("data/data.db", schema)

    # Debug check
    debug_schema(enriched_schema)

    # Step 3: Queries to test semantic understanding
    queries = [
        "people in delhi",
        "total revenue",
        "payment method used",
        "employee income"
    ]

    # Step 4: Run retrieval
    for query in queries:
        print("\n========================")
        print("Query:", query)

        relevant_schema = retrieve_relevant_schema(query, enriched_schema)

        print("\nRETRIEVER OUTPUT:\n", relevant_schema)

        # Pretty print
        for table, cols in relevant_schema.items():
            print(f"\nTable: {table}")
            print("Type of cols:", type(cols))

            if len(cols) > 0:
                print("First element:", cols[0])
                print("Type of first element:", type(cols[0]))

            print("\nColumns:")
            for col in cols:
                print(f"  - {col['name']} ({col['type']})")


if __name__ == "__main__":
    run_tests()