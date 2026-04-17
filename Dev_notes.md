# 🧠 0. PURPOSE OF THIS DOCUMENT

This document is the complete engineering blueprint for building QueryGraph AI.

It contains:
- full folder structure
- module responsibilities
- execution flow
- input/output contracts
- system design decisions (implementation-level)
- pipeline behavior

This file is meant to be the **single source of truth** for building and extending the system.

---

# 🏗️ 1. SYSTEM OVERVIEW

QueryGraph AI is a data intelligence system that converts:

```text
Natural Language → SQL → Execution → Explanation

It is designed as a modular pipeline where each stage is independent and replaceable.

⸻

🔄 2. HIGH-LEVEL EXECUTION FLOW

User Query
   ↓
Schema Extraction
   ↓
Schema Retrieval (Top-K)
   ↓
Metadata Enrichment
   ↓
SQL Generation (LLM)
   ↓
SQL Validation Loop
   ↓
Database Execution
   ↓
Result Explanation
   ↓
Final Output


⸻

📁 3. COMPLETE PROJECT STRUCTURE

project/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   └── data.db
│
├── src/
│   ├── ingestion/
│   │   ├── file_loader.py
│   │   ├── cleaner.py
│   │   └── to_sqlite.py
│   │
│   ├── database/
│   │   └── db_manager.py
│   │
│   ├── schema/
│   │   └── extractor.py
│   │
│   ├── retrieval/
│   │   ├── embedder.py
│   │   └── retriever.py
│   │
│   ├── metadata/
│   │   ├── generator.py
│   │   └── cache.py
│   │
│   ├── llm/
│   │   ├── sql_generator.py
│   │   ├── validator.py
│   │   └── explainer.py
│   │
│   ├── pipeline/
│   │   └── graph.py
│   │
│   ├── cache/
│   │   └── cache_manager.py
│   │
│   └── utils/
│       └── helpers.py
│
├── evaluation/
│   ├── evaluator.py
│   └── test_cases.json
│
├── tests/
│   └── test_pipeline.py
│
└── DEV_NOTES.md


⸻

🔹 4. MODULE DESIGN (DETAILED)

⸻

📦 4.1 ingestion/

Purpose

Convert raw user files into structured SQLite tables.

⸻

Flow

CSV / Excel → DataFrame → Clean → SQLite Table


⸻

Files

file_loader.py
	•	Reads CSV / Excel files
	•	Returns pandas DataFrame

cleaner.py
	•	Cleans column names
	•	Handles missing values
	•	Standardizes formats

to_sqlite.py
	•	Converts DataFrame into SQLite table
	•	Creates schema automatically

⸻

Output
	•	One table per file inside data.db

⸻

📦 4.2 database/

db_manager.py

Purpose

Single interface for all database operations.

⸻

Responsibilities
	•	connect to SQLite
	•	execute SQL queries
	•	fetch schema
	•	return results safely

⸻

Core Functions

connect_db()
execute_query(sql)
get_tables()
get_columns(table)


⸻

Rule

All database interaction MUST go through this module.

⸻

📦 4.3 schema/

extractor.py

Purpose

Extract structured schema from database.

⸻

Output Format

{
  "sales": {
    "columns": ["amount", "region", "date"]
  }
}


⸻

Role

Provides structured schema context to retrieval and LLM layers.

⸻

📦 4.4 retrieval/

Purpose

Select only relevant schema parts for a query.

⸻

embedder.py
	•	Converts schema elements into embeddings

⸻

retriever.py
	•	Converts user query into embedding
	•	Performs similarity search
	•	Returns Top-K relevant schema fields

⸻

Flow

Query → Embedding → Similarity Search → Top-K Schema


⸻

Output

["sales.amount", "sales.region"]


⸻

Rule

Only Top-K schema is passed forward to LLM.

⸻

📦 4.5 metadata/

Purpose

Convert raw column names into meaningful descriptions.

⸻

generator.py

Input
	•	column name
	•	sample values (few rows)

Output
	•	semantic meaning of column

⸻

Example

amt → transaction amount
dt → transaction date


⸻

cache.py

Purpose

Store metadata results to avoid repeated generation.

⸻

Flow

Check Cache → If Missing → Generate → Store → Return


⸻

📦 4.6 llm/

⸻

sql_generator.py

Purpose

Convert natural language query into SQL.

⸻

Input
	•	user query
	•	retrieved schema
	•	metadata

⸻

Output
	•	SQL query string

⸻

Example

SELECT region, SUM(amount)
FROM sales
GROUP BY region;


⸻

validator.py

Purpose

Validate and fix SQL queries using feedback loop.

⸻

Flow

SQL → Execute → Error?
            ↓
     Send error to LLM
            ↓
      Regenerate SQL


⸻

Constraint

Max retry attempts = 3

⸻

explainer.py

Purpose

Convert query results into human-readable insights.

⸻

Example Output

North region has the highest total sales.


⸻

📦 4.7 pipeline/

⸻

graph.py

Purpose

Defines complete execution pipeline using LangGraph.

⸻

Execution Order

extract_schema()
    ↓
retrieve_schema()
    ↓
generate_metadata()
    ↓
generate_sql()
    ↓
validate_sql()
    ↓
execute_sql()
    ↓
generate_explanation()


⸻

Role

Acts as the central orchestrator of the system.

⸻

📦 4.8 cache/

⸻

cache_manager.py

Purpose

Store intermediate results to reduce computation cost.

⸻

Stored Data
	•	metadata results
	•	SQL results
	•	schema retrieval outputs

⸻

Implementation
	•	in-memory dictionary (MVP)

⸻

📦 4.9 utils/

⸻

helpers.py

Purpose

Shared utility functions.

⸻

Examples
	•	column name normalization
	•	text cleaning
	•	formatting outputs

⸻

📦 5. evaluation/

⸻

evaluator.py

Purpose

Evaluate system accuracy and reliability.

⸻

Metrics
	•	SQL correctness
	•	execution success rate
	•	response latency

⸻

test_cases.json

Contains predefined query → expected behavior pairs.

⸻

📦 6. tests/

⸻

test_pipeline.py

Purpose

End-to-end system validation.

⸻

Execution Flow Tested

ingestion → schema → retrieval → SQL → validation → execution


⸻

📦 7. app/

⸻

streamlit_app.py

Purpose

User interface for interacting with system.

⸻

Features
	•	file upload
	•	natural language query input
	•	SQL preview
	•	result visualization
	•	explanation output

⸻

🔄 8. FULL SYSTEM EXECUTION MODEL

1. User uploads dataset
2. ingestion module converts to SQLite
3. schema extractor builds schema graph
4. retrieval selects relevant schema subset
5. metadata enriches column meaning
6. SQL generator creates query
7. validator fixes errors if needed
8. database executes query
9. explainer generates final output


⸻

🧠 9. DESIGN RULES

⸻

Rule 1

Each module has a single responsibility

Rule 2

LLM calls are isolated in llm/ module

Rule 3

Database access only via db_manager

Rule 4

Pipeline is the only orchestrator

Rule 5

No module depends on UI layer

⸻

🚀 10. SYSTEM DESIGN GOAL

The system is designed to be:
	•	modular
	•	replaceable
	•	testable
	•	scalable in structure

⸻

🧾 11. FINAL EXECUTION MINDSET

Data → Schema → Retrieval → Metadata → SQL → Validate → Execute → Explain

