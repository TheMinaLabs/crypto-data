
  
  create view "crypto_vault"."main"."stg_raw_coin_data__dbt_tmp" as (
    -- This model reads the raw parquet file created by the Python script
select
    ticker::varchar as ticker,
    price::float as price_eur,
    current_timestamp as processed_at
from 'data/raw_coin_data.parquet'
  );
