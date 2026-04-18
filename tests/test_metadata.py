from src.schema.extractor import get_schema
from src.metadata.generator import generate_metadata

schema = get_schema("data/data.db")

enriched = generate_metadata("data/data.db", schema)

for table, cols in enriched.items():
    print("\n=====================")
    print("Table:", table)

    for col in cols:
        print(f"\nColumn: {col['name']}")
        print("Type:", col["type"])
        print("Description:", col["description"])
        print("Sample Values:", col["sample_values"])