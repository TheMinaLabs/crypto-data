# 📈 VeraTrade: High-Veracity Crypto Data Platform

## **Project Overview**

This project implements a modern "Asset-Centric" data pipeline designed for a 2026 FinTech environment. It transitions from traditional task-based processing to **Software-Defined Assets (SDAs)**, ensuring built-in lineage and observability.

## **The Architecture**

- **Ingestion:** Python-based harvester targeting CoinGecko API, utilizing **PyArrow** for high-performance columnar storage in Parquet format.

- **Storage:** Local Data Lakehouse architecture using **DuckDB** for in-process analytical processing.

- **Transformation:** Modular **dbt** modeling following a multi-layered (Staging/Marts) approach.

- **Orchestration:** Conceptualized for **Dagster** to leverage asset-based tracking and "re-execution from the middle".

![alt text](image-2.png)
![alt text](image-3.png)

## **Data Contracts & Quality**

To achieve **99% accuracy**, this pipeline enforces:

- **Schema-on-Write:** Strict validation during the ingestion phase.

- **Automated Testing:** dbt tests for 'not_null' and price-range validation to prevent "data swamps".

- **Lineage:** Full visibility from raw API ingestion to final analytical models.

![alt text](image-1.png)

## **How to Run**

```bash
1. pip install -r requirements.txt
2. python ingest_prices.py
3. dbt run
4. dbt test
