import os
from pathlib import Path
from dagster import Definitions, asset
from dagster_dbt import DbtCliResource, dbt_assets
import pandas as pd
import requests
import sys

# Find the dbt executable inside current .venv
dbt_executable = os.path.join(sys.prefix, "bin", "dbt")

# 1. Setup the dbt path
DBT_PROJECT_DIR = Path(__file__).joinpath("..").resolve()
dbt_resource = DbtCliResource(
    project_dir=os.fspath(DBT_PROJECT_DIR),
    executable=dbt_executable, # Forces Dagster to use the .venv dbt (virtual environment)
)

# 2. Define the Ingestion as a Dagster Asset
@asset(group_name="ingestion", compute_kind="python")
def raw_coin_data():
    """Fetches crypto data from CoinGecko API and saves to Parquet."""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=eur"
    response = requests.get(url).json()
    
    df = pd.DataFrame([
        {"ticker": "BTC", "price": response["bitcoin"]["eur"]},
        {"ticker": "ETH", "price": response["ethereum"]["eur"]}
    ])
    
    os.makedirs('data', exist_ok=True)
    df.to_parquet('data/raw_coin_data.parquet')
    return df

# 3. Load dbt models automatically as assets
@dbt_assets(manifest=DBT_PROJECT_DIR.joinpath("target", "manifest.json"))
def crypto_dbt_assets(context, dbt: DbtCliResource):
    # .stream() is the 2026 standard for handling dbt events in Dagster
    yield from dbt.cli(["build"], context=context).stream()

# 4. Combine everything into a single project definition
defs = Definitions(
    assets=[raw_coin_data, crypto_dbt_assets],
    resources={"dbt": dbt_resource},
)