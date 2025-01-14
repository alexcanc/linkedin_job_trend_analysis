-- Description: This model transforms raw job posting data into a structured format for further analysis.
{{ config(materialized='table', schema='bronze') }}

WITH transformed_data AS (
    SELECT
        job_link,
        last_processed_time,
        got_summary,
        got_ner,
        is_being_worked,
        job_title,
        company,
        job_location,
        first_seen,
        search_city,
        search_country,
        search_position,
        job_level,
        job_type
    FROM {{ source('dbt_bronze', 'job_posting_raw') }}
)

SELECT
    job_link,
    last_processed_time,
    got_summary,
    got_ner,
    is_being_worked,
    job_title,
    company,
    job_location,
    first_seen,
    search_city,
    search_country,
    search_position,
    job_level,
    job_type
FROM transformed_data
