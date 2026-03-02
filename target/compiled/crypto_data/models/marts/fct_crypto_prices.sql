

WITH prices AS (
    SELECT * FROM "crypto_vault"."main"."stg_raw_coin_data"
)

select
    ticker,
    price_eur,
    processed_at,
    -- Data Quality Flag: flag if the price is valid (positive)
    case when price_eur > 0 then true else false end as is_valid_price
from prices