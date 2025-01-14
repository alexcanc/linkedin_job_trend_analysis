"""
In data visualizations the following visualizations are shown:
- A bar chart with the top 5 skills with the most job posting for a job title
"""

import altair as alt
import streamlit as st
from f1dashboard.advanced.state import F1State
from f1dashboard.advanced.constants import F1Constants
# from f1dashboard.advanced.database import F1Database
from f1dashboard.advanced.queries import F1Queries
import pandas as pd

class DataVisualizations:
    def __init__(self, header_font_size="20px", text_font_size="14px") -> None:
        self.header_font_size = header_font_size
        self.text_font_size = text_font_size
        self.inject_custom_css()

        self.f1_state = F1State()
        # self.f1_database = F1Database()
        self.f1_queries = F1Queries()

    def inject_custom_css(self):
        """ Inject custom CSS """
        custom_css = f"""
            <style>
                /* Main content styles */
                body {{
                    color: #FFFFFF;
                    background-color: #0077B5;
                }}
                .stApp {{
                    background-color: #0077B5;
                }}
                h1 {{
                    font-size: {self.header_font_size};
                }}
                .markdown-text-container, .stMarkdown {{
                    font-size: {self.text_font_size};
                }}

                /* Sidebar styles */
                .css-1kyxreq, .css-1v3fvcr, .css-1e5imcs, .stSidebar {{
                    background-color: #FFFFFF;
                    color: #0077B5;
                }}
                [data-testid="stSidebar"] * {{
                    background-color: #FFFFFF;
                    color: #0077B5;
                }}
                /* You may need to add more selectors for different types of text within the sidebar */

            </style>
        """
        st.markdown(custom_css, unsafe_allow_html=True)

    def select_filters(self):
        # Create two selectors for 'Job Title' and 'Job Level'
        with st.sidebar:
            st.subheader("Select a job role to explore")
            self.selected_table = "All"
            self.selected_job_title = st.selectbox("Job Title", F1Constants.job_titles())
            st.subheader("Select a job level to explore")
            self.selected_table = "All"
            self.selected_job_level = st.selectbox("Job Level", F1Constants.job_levels())
            self.selected_table = "Job_Title: " + self.selected_job_title + ", Job Level: " + self.selected_job_level

    def get_filtered_table(self):
        # retrieve_filtered_table from state or database
        if self.selected_table in st.session_state:
            st.info(f"Retrieve the {self.selected_table} table from state...")
            # $CHALLENGIFY_BEGIN
            table_results = self.f1_state.get_data_from_state(self.selected_table)
            # $CHALLENGIFY_END
        else:
            st.info(f"Retrieve the {self.selected_table} table from the database...")
            # $CHALLENGIFY_BEGIN
            table_results = self.f1_queries.get_filtered_skills(self.selected_job_title, self.selected_job_level)
            # $CHALLENGIFY_END
            st.info(f"Saving the {self.selected_table} table to state...")
            # $CHALLENGIFY_BEGIN
            self.f1_state.store_in_state(self.selected_table, table_results)
            # $CHALLENGIFY_END
        return table_results


    # Assuming filtered_data is a DataFrame with 'job_skills' and 'skill_count' columns
    def create_skills_report(self,filtered_data):
        st.subheader("Table Highlights")
        st.write(filtered_data)

    # Assuming filtered_data is a DataFrame with 'job_skills' and 'skill_count' columns
    def create_skills_chart(self, filtered_data):
        """Create a bar chart with the top 5 Skills
        """
        st.subheader("Top 5 Skills for the selected Job Role")
        # Use your package logic to load data, then plot it accordingly.
        top_skills_data = filtered_data
        bar_chart = alt.Chart(top_skills_data).mark_bar().encode(y=alt.Y("skill_count"), x=alt.X("job_skills", sort="-y"),
                                                             color="job_skills", tooltip="skill_count")
        st.altair_chart(bar_chart, use_container_width=True)

if __name__ == "__main__":
    st.title("Data visualizations & Insights of Skills Analysis")
    # $CHALLENGIFY_BEGIN
    data_visualizations = DataVisualizations(header_font_size="26px", text_font_size="14px")
    data_visualizations.select_filters()
    # data_visualizations.create_skills_report(data_visualizations.get_filtered_table())
    data_visualizations.create_skills_chart(data_visualizations.get_filtered_table())
    # $CHALLENGIFY_END
