:::writing{variant=“standard” id=“91823”}

CONTRIBUTING.md — QueryGraph AI

⸻

🤝 Why This Project Exists

Tools like Databricks and Snowflake are powerful—but they are also:
	•	expensive
	•	complex
	•	not easily accessible to everyone

At the same time, many people:
	•	have data
	•	want insights
	•	but don’t have the tools or expertise

⸻

I built QueryGraph AI as a small step toward:

Making data systems more accessible, understandable, and open


⸻

🧠 What This Project Is

QueryGraph AI is a system that:
	•	converts natural language → SQL
	•	validates and corrects queries
	•	executes them safely
	•	explains results in simple language

⸻

It is designed to be:
	•	modular
	•	extensible
	•	easy to experiment with

⸻

🔄 Project Status

This project is actively evolving.

It is not production-ready, and that’s intentional.

There are known limitations, and improving them is part of the goal.

⸻

⚠️ Areas That Need Improvement

If you’re looking to contribute, these are meaningful areas:

⸻

1. Retrieval Quality

The system may select:
	•	incorrect tables
	•	irrelevant columns

Ideas:
	•	hybrid retrieval (embedding + keyword)
	•	reranking

⸻

2. Metadata Understanding

Column meanings are inferred and may be inaccurate.

Ideas:
	•	better prompts
	•	statistical summaries
	•	user-provided descriptions

⸻

3. SQL Generation

Complex queries (joins, nested logic) can fail.

Ideas:
	•	step-by-step reasoning
	•	query decomposition

⸻

4. Validation Layer

Currently focuses on:
	•	syntax errors

But not always:
	•	logical correctness

⸻

5. Database Support

Currently supports:
	•	SQLite

Future scope:
	•	PostgreSQL
	•	MySQL
	•	cloud databases

⸻

6. Performance & Cost

LLM calls introduce:
	•	latency
	•	cost

Ideas:
	•	caching
	•	reducing redundant calls
	•	using smaller models

⸻

🧩 How to Contribute

You don’t need to understand the entire system.

You can:
	•	improve a single module
	•	fix bugs
	•	optimize performance
	•	improve prompts
	•	enhance documentation

⸻

Suggested Approach
	1.	Pick a module (e.g., retrieval, metadata, validator)
	2.	Understand its role from DEV_NOTES.md
	3.	Make focused improvements
	4.	Test using tests/test_pipeline.py
	5.	Submit a pull request

⸻

🧠 Contribution Principles

When contributing, I try to follow:
	•	keep things simple
	•	avoid unnecessary complexity
	•	reduce reliance on LLM where possible
	•	prioritize reliability over cleverness

⸻

💬 Open Questions

These are areas I’m still exploring:
	•	How can retrieval better understand intent?
	•	How can results be validated beyond execution success?
	•	What parts truly require LLMs?
	•	How can multi-database support be made clean and modular?

⸻

📌 Before Submitting
	•	Ensure your code is modular
	•	Avoid breaking existing flow
	•	Keep changes focused
	•	Add comments where necessary

⸻

🌱 Final Note

This project is open by design.

It will improve through contributions, experiments, and shared ideas


⸻

If you have an idea—even a small one—feel free to contribute.

⸻

:::
