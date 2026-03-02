
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select price_eur
from "crypto_vault"."main"."fct_crypto_prices"
where price_eur is null



  
  
      
    ) dbt_internal_test