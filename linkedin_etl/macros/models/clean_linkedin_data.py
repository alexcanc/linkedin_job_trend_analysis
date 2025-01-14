from google.cloud import bigquery
import pandas as pd

# Initialize a BigQuery client
client = bigquery.Client()

def clean_and_load_table(bronze_table_id, silver_table_name, clean_query):
    """
    Load data from a bronze table, clean it, and store it in the silver dataset.
    """
    # Run the clean query
    job = client.query(clean_query)
    result = job.result()  # Waits for the job to complete.

    # Define the destination table ID for the cleaned data
    cleaned_table_id = f'linkedin123456.silver1.{silver_table_name}'

    # Save the result into the silver dataset
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",  # Overwrites the table if it exists
    )

    load_job = client.load_table_from_dataframe(
        result.to_dataframe(),
        cleaned_table_id,
        job_config=job_config
    )
    load_job.result()  # Waits for the table load to complete.

    print(f"Loaded cleaned data from {bronze_table_id} into {cleaned_table_id}.")

# Cleaning queries
clean_skills_query = """
SELECT DISTINCT skill_name, skill_category
FROM `linkedin123456.bronze.skills_raw`
WHERE skill_name IS NOT NULL AND skill_name != ''
"""

clean_job_posting_query = """
SELECT DISTINCT *
FROM `linkedin123456.bronze.job_posting_raw`
WHERE job_title IS NOT NULL AND job_title != ''
"""

# Clean and load skills_raw
clean_and_load_table('linkedin123456.bronze.skills_raw', 'cleaned_skills', clean_skills_query)

# Clean and load job_posting_raw
clean_and_load_table('linkedin123456.bronze.job_posting_raw', 'cleaned_job_postings', clean_job_posting_query)
