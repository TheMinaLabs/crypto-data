-- This model reads the raw parquet file created by the Python script
select
    ticker::varchar as ticker,
    price::float as price_eur,
    current_timestamp as processed_at
from 'data/raw_coin_data.parquet'
