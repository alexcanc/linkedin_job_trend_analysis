-- tests/check_bronze_has_rows.sql

SELECT COUNT(*)
FROM {{ source('linkedin_data', 'dbt_bronze') }}
HAVING COUNT(*) = 0
