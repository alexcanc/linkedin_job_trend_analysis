import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from google.cloud import bigquery
import json
from google.oauth2 import service_account

# class F1Database:
#     def __init__(
#         self,
#     ) -> None:
#         #dockeself.db_connection = self.init_connection(URL.create(**st.secrets["postgres"]))

#     @st.cache_resource
#     def init_connection(_self, credentials):
#         """Create the database connection using the right credentials

#         Args:
#             credentials (_type_): _description_

#         Returns:
#             _type_: _description_
#         """
#         conn = create_engine(credentials, echo=False)
#         return conn

class LinkedinDatabase:
    def __init__(
        self,
    ) -> None:
        self.client = self.init_bigquery_client()

    @st.cache_resource
    def init_bigquery_client(_self):
        # Fetch secrets
        # service_account_info = st.secrets["bigquery"]["service_account_json"]
        # project_id = st.secrets["bigquery"]["project_id"]

        # Create and return a BigQuery client
        return bigquery.Client.from_service_account_json("/app/keys/service.json", project="bootcamp-data-413116")








# # To test LinkedinDatabase class, uncomment the following:
# # Example usage:
# if __name__ == "__main__":
#     linkedin_db = LinkedinDatabase()
#     query = "SELECT job_title, job_skills FROM `linkedin123456.gold.linkedin_data_job_skills_uk_2024` LIMIT 1"
#     df = linkedin_db.run_query(query)
#     print(df)
