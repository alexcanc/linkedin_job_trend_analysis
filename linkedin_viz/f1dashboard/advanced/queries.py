import pandas as pd
import streamlit as st
from f1dashboard.advanced.database import LinkedinDatabase


class F1Queries:
    def __init__(self) -> None:
        #self.conn = F1Database().db_connection
        self.client = LinkedinDatabase().client

    # # Perform query.
    # # Uses st.experimental_memo to only rerun when the query changes or after 10 min.
    @st.cache_data(ttl=600)
    def _run_query(_self, query):
        """
        Base utility method queries a database using pandas and returning a dataframe

        Parameters
        ----------
        query: Str
            SQL query as a f-string

        Returns
        -------
        races: pandas.DataFrame
            Dataframe containing the result of the query

        """

        return pd.read_sql_query(query, _self.conn)

    # # Uses st.experimental_memo to only rerun when the query changes or after 10 min.
    @st.cache_data(ttl=600)
    def _run_query_ld(_self, query):
        """
        Runs a query on the BigQuery database and returns a DataFrame.

        Args:
            query (str): SQL query string

        Returns:
            pd.DataFrame: Query results
        """
        query_job = _self.client.query(query)
        return query_job.result().to_dataframe()

    def retrieve_table(self, table_name):
        if table_name.lower() == "linkedin":
            # Handle BigQuery table
            # linkedin_db = LinkedinDatabase()
            return self._run_query_ld("SELECT * FROM `linkedin123456.gold.linkedin_data_job_skills_uk_2024`")
        else:
            # Existing logic for SQL tables
            return self._run_query(f"SELECT * FROM {table_name}")

    # Inside F1Queries class add a new method for getting filtered data from BigQuery
    def get_filtered_skills(self, job_title=None, job_level=None):
        # Construct your query based on the filters
        where_clauses = []
        if job_title and job_title != "All":
            where_clauses.append(f"job_title = '{job_title}'")
        if job_level and job_level != "All":
            where_clauses.append(f"job_level = '{job_level}'")

        where_statement = ' AND '.join(where_clauses)
        query = f"SELECT job_skills, COUNT(*) as skill_count FROM `linkedin123456.gold.linkedin_data_job_skills_uk_2024`"

        if where_statement:
            query += f" WHERE {where_statement}"

        query += " GROUP BY job_skills ORDER BY skill_count DESC LIMIT 5"

        return self._run_query_ld(query)

    def get_filtered_titles(self, job_skills=None):
        # Construct your query based on the filters
        where_clauses = []
        if job_skills and job_skills != "All":
            where_clauses.append(f"job_skills = '{job_skills}'")

        where_statement = ''.join(where_clauses)
        query = f"SELECT job_title, job_level, COUNT(*) as job_title_count FROM `linkedin123456.gold.linkedin_data_job_skills_uk_2024`"

        if where_statement:
            query += f" WHERE {where_statement}"

        query += " GROUP BY job_title, job_level ORDER BY job_title_count DESC LIMIT 25"

        return self._run_query_ld(query)

    def get_skills_transferrability_trend(self, job_skills=None):
        # Construct your query based on the filters
        where_clauses = []
        if job_skills and job_skills != "All":
            where_clauses.append(f"job_skills = '{job_skills}'")

        where_statement = ''.join(where_clauses)
        query = f"SELECT first_seen, COUNT(DISTINCT job_title) as unique_role_count FROM `linkedin123456.gold.linkedin_data_job_skills_uk_2024`"

        if where_statement:
            query += f" WHERE {where_statement}"

        query += " GROUP BY first_seen ORDER BY first_seen ASC"

        return self._run_query_ld(query)

if __name__ == "__main__":
    queries = F1Queries()
