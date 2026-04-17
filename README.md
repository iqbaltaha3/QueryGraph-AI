# QueryGraph AI

> A schema-aware, self-correcting data copilot for reliable natural language querying over structured data.

---

## 🚀 Overview

**QueryGraph AI** enables users to ask questions in natural language over their data (CSV/Excel/SQL) and receive accurate results with explanations.

Unlike typical NL→SQL demos, it is designed as a **robust system** with:

* **Schema-aware retrieval** (Top‑K context control)
* **Self-correcting SQL generation** (validator loop)
* **On-demand semantics** (lazy metadata)
* **Measurable quality** (evaluation harness)

---

## 🎯 Problem

Real-world datasets are messy:

* Large schemas (100s–1000s of columns)
* Ambiguous column names
* Missing documentation

Most tools fail due to:

* Overloading LLM context
* Incorrect joins/filters
* No recovery from errors

**QueryGraph AI** addresses these with retrieval, validation, and controlled LLM usage.

---

## 🧠 System Architecture

```
User Query
   ↓
Schema Retriever (Top‑K)
   ↓
Lazy Metadata (on-demand)
   ↓
SQL Generator (LLM)
   ↓
Validator Loop (fix & retry)
   ↓
Execution Engine (SQLite)
   ↓
Explanation Layer
   ↓
Answer
```

**Key idea:** *Reduce what is sent to the model, control how often it is called, and verify before returning results.*

---

## 🔑 Key Features

### 1) Schema-Aware Retrieval

* Embedding-based retrieval over tables/columns
* Returns **Top‑K relevant context** (prevents context explosion)

### 2) Self-Correcting SQL

* Generates SQL with LLM
* Executes and captures errors
* **Automatically fixes and retries** (bounded)

### 3) Lazy Metadata Generation

* Infers column meaning **only when needed**
* Cached for reuse (reduces cost/latency)

### 4) Safe Execution

* Executes on SQLite
* Limits output size and guards against heavy queries

### 5) Natural Language Explanations

* Converts results into concise, human-readable insights

### 6) Evaluation-First Design

* Test suite with predefined queries
* Metrics: success rate, correction rate, latency

---

## 🏗️ Design Principles

* **Top‑K Only**: never send full schema to the LLM
* **Lazy Computation**: generate metadata on-demand
* **Bounded Retries**: avoid runaway correction loops
* **Cache Aggressively**: metadata and query results
* **Modular Pipeline**: each component independently testable

---

## 🧪 Example

**User Query**

```
Show total revenue by region for last quarter
```

**Generated SQL (simplified)**

```sql
SELECT region, SUM(amount) AS revenue
FROM sales
WHERE date >= '2025-10-01'
GROUP BY region;
```

**Output**

```
North has the highest revenue, followed by West and South.
```

---

## ⚙️ Getting Started

### 1. Clone

```bash
git clone https://github.com/<your-username>/querygraph-ai.git
cd querygraph-ai
```

### 2. Install

```bash
pip install -r requirements.txt
```

### 3. Run App

```bash
streamlit run app/streamlit_app.py
```

### 4. Use

* Upload CSV/Excel files
* Ask a question in natural language
* View SQL, results, and explanation

---

## 🧩 Project Structure

```
project/
├── app/                    # Streamlit UI
├── data/                   # Raw + processed data
├── src/
│   ├── ingestion/          # File loading → SQLite
│   ├── database/           # Query execution
│   ├── schema/             # Schema extraction
│   ├── metadata/           # On-demand semantics
│   ├── retrieval/          # Embeddings + Top‑K
│   ├── llm/                # SQL gen + validation + explain
│   ├── pipeline/           # Orchestration (LangGraph)
│   ├── cache/              # In-memory cache
│   └── utils/
├── evaluation/             # Test cases + metrics
└── tests/                  # Integration tests
```

---

## 📊 Evaluation

We evaluate the system on a fixed set of queries.

**Metrics**

* **Execution Success Rate**: valid SQL that runs
* **Correction Rate**: fixed after initial failure
* **Failure Rate**: unrecoverable errors
* **Latency**: end-to-end response time

Run:

```bash
python evaluation/evaluator.py
```

---

## ⚖️ Trade-offs

* **SQLite for MVP**: simple, portable (not for large-scale production)
* **LLM Dependence**: reduced via retrieval + validation
* **Heuristics + LLM**: balance between cost and accuracy

---

## 🛣️ Roadmap (Short)

* PostgreSQL / cloud DB support
* Hybrid retrieval (embedding + keyword)
* Smarter join inference
* Persistent caching (Redis)

---

## 🧠 Why This Matters

This project demonstrates:

* Building **systems around LLMs**, not just prompts
* Handling **scale, cost, and reliability**
* **Evaluation-driven** ML engineering

---

## 📄 License

MIT

---

## 🙌 Acknowledgements

Inspired by modern LLM system design patterns (RAG, validation loops, and retrieval-first architectures).

