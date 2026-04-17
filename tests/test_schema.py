from src.schema.extractor import get_schema

schema = get_schema("data/data.db")
print(schema)