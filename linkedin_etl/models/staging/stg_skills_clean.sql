-- models/staging/stg_skills_clean.sql
{{ config(materialized='table', schema='silver', alias='cleaned_skills') }}

WITH cleaned_skills AS (
    SELECT
        job_link,
        job_skills
    FROM {{ source('dbt_bronze', 'skills_raw') }}
    WHERE job_link IS NOT NULL
      AND job_skills IS NOT NULL
)

SELECT *
FROM cleaned_skills
