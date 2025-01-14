-- tests/check_bronze2_has_rows.sql

SELECT COUNT(*)
FROM {{ source('linkedin_data', 'dbt_bronze2') }}
HAVING COUNT(*) = 0
