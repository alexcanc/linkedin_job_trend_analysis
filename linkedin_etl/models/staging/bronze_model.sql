-- Description: This model transforms raw skills data into the desired format for further analysis.
{{ config(materialized='table', schema='bronze') }}

WITH transformed_data AS (
    SELECT
        job_link,
        job_skills
    FROM {{ source('dbt_bronze', 'skills_raw') }}
)

SELECT
    job_link,
    job_skills
FROM transformed_data
