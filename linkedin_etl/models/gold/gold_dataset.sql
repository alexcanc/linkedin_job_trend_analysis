{{ config(materialized='table', database='linkedin123456', schema='gold', alias='gold_dataset2') }}

WITH enriched_data AS (
    SELECT
        jp.job_link,
        jp.last_processed_date,
        jp.has_summary,
        jp.job_title,
        jp.company,
        jp.job_location,
        jp.first_seen,
        jp.search_city,
        jp.search_country,
        jp.search_position,
        jp.job_level,
        jp.job_type,
        sk.first_skill
    FROM {{ source('dbt_silver', 'cleaned_job_postings') }} AS jp
    LEFT JOIN {{ source('dbt_silver', 'cleaned_skills_first_skill') }} AS sk
    ON jp.job_link = sk.job_link
)

SELECT *
FROM enriched_data
