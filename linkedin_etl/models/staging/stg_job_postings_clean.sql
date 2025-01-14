-- models/staging/stg_job_postings_clean.sql
{{ config(materialized='table', schema='silver', alias='cleaned_job_postings') }}

WITH cleaned_job_postings AS (
    SELECT
        job_link,
        DATE(last_processed_time) AS last_processed_date,
        CASE
            WHEN got_summary = 'true' THEN 'Yes'
            ELSE 'No'
        END AS has_summary,
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
    WHERE job_title IS NOT NULL
      AND company IS NOT NULL
)

SELECT *
FROM cleaned_job_postings
