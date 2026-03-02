# 📈 VeraTrade: High-Veracity Crypto Data Platform

## **Project Overview**

This project implements a modern "Asset-Centric" data pipeline designed for a 2026 FinTech environment. [cite_start]It transitions from traditional task-based processing to **Software-Defined Assets (SDAs)**, ensuring built-in lineage and observability[cite: 50, 65, 66].

## **The Architecture**

- [cite_start]**Ingestion:** Python-based harvester targeting CoinGecko API, utilizing **PyArrow** for high-performance columnar storage in Parquet format[cite: 38].

- [cite_start]**Storage:** Local Data Lakehouse architecture using **DuckDB** for in-process analytical processing[cite: 54].

- **Transformation:** Modular **dbt** modeling following a multi-layered (Staging/Marts) approach.

- [cite_start]**Orchestration:** Conceptualized for **Dagster** to leverage asset-based tracking and "re-execution from the middle"[cite: 101, 102].

## **Data Contracts & Quality**

To achieve **99% accuracy**, this pipeline enforces:

- [cite_start]**Schema-on-Write:** Strict validation during the ingestion phase[cite: 11].

- [cite_start]**Automated Testing:** dbt tests for 'not_null' and price-range validation to prevent "data swamps"[cite: 11, 21].

- **Lineage:** Full visibility from raw API ingestion to final analytical models.

![alt text](image-1.png)

## **How to Run**

1. 'pip install -r requirements.txt'
2. 'python ingest_prices.py'
3. 'dbt run'
4. 'dbt test'
