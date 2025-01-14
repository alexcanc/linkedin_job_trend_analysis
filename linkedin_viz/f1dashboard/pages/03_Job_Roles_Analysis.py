"""
In data visualizations the following visualizations are shown:
- A bar chart with the top 5 job roles with the most job posting for a job skill
- A line chart with unique count of jobs over time for a skill to transferrability of a skill
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
        # Create a selector for 'Job Skill'
        with st.sidebar:
            st.subheader("Select a skill to explore")
            self.selected_table = "All"
            self.selected_job_skill = st.selectbox("Skill", F1Constants.job_skills())
            self.selected_table = "Job_Skill: " + self.selected_job_skill

    def get_filtered_table(self, query_name):
        if query_name == "get_filtered_titles": #caching bar tables
            self.selected_table = "Job_Skill: " + self.selected_job_skill
            # retrieve_filtered_table from state or database
            if self.selected_table in st.session_state:
                st.info(f"Retrieve the {self.selected_table} table from state...")
                # $CHALLENGIFY_BEGIN
                table_results = self.f1_state.get_data_from_state(self.selected_table)
                # $CHALLENGIFY_END
            else:
                st.info(f"Retrieve the {self.selected_table} table from the database...")
                # $CHALLENGIFY_BEGIN
                table_results = self.f1_queries.get_filtered_titles(self.selected_job_skill)
                # $CHALLENGIFY_END
                st.info(f"Saving the {self.selected_table} table to state...")
                # $CHALLENGIFY_BEGIN
                self.f1_state.store_in_state(self.selected_table, table_results)
                # $CHALLENGIFY_END
        else: #caching trend tables
            self.selected_table = "Job_Skill_time: " + self.selected_job_skill
            # retrieve_filtered_table from state or database
            if self.selected_table in st.session_state:
                st.info(f"Retrieve the {self.selected_table} table from state...")
                # $CHALLENGIFY_BEGIN
                table_results = self.f1_state.get_data_from_state(self.selected_table)
                # $CHALLENGIFY_END
            else:
                st.info(f"Retrieve the {self.selected_table} table from the database...")
                # $CHALLENGIFY_BEGIN
                table_results = self.f1_queries.get_skills_transferrability_trend(self.selected_job_skill)
                # $CHALLENGIFY_END
                st.info(f"Saving the {self.selected_table} table to state...")
                # $CHALLENGIFY_BEGIN
                self.f1_state.store_in_state(self.selected_table, table_results)
                # $CHALLENGIFY_END
        return table_results

    # Assuming filtered_data is a DataFrame with 'job_skills' and 'skill_count' columns
    def create_roles_report(self,filtered_data):
        st.subheader("Table Highlights")
        st.write(filtered_data.head())

    # Assuming filtered_data is a DataFrame with 'job_skills' and 'skill_count' columns
    def create_roles_chart(self, filtered_data):
        """Create a bar chart with the top Job Roles
        """
        st.subheader("Top Job Roles for the selected Skill")
        # Use your package logic to load data, then plot it accordingly.
        top_roles_data = filtered_data
        bar_chart = alt.Chart(top_roles_data).mark_bar().encode(y=alt.Y("job_title_count"), x=alt.X("job_title", sort="-y"),
                                                             color="job_level", tooltip="job_title_count")
        st.altair_chart(bar_chart, use_container_width=True)

    # Assuming filtered_data is a DataFrame with 'job_skills' and 'skill_count' columns
    def create_skill_transferrability_chart(self, filtered_data):
        """Create a line chart showing skill transferrability trend
        """
        st.subheader("Unique Job Role Count over Time for the Selected Skill")
        # Use your package logic to load data, then plot it accordingly.
        trend_data = filtered_data
        line_chart = alt.Chart(trend_data).mark_line().encode(y=alt.Y("unique_role_count"), x=alt.X("first_seen", sort="x"),
                                                            tooltip="unique_role_count")
        st.altair_chart(line_chart, use_container_width=True)

if __name__ == "__main__":
    st.title("Data visualizations & Insights of Job Roles Analysis")
    # $CHALLENGIFY_BEGIN
    data_visualizations = DataVisualizations(header_font_size="26px", text_font_size="14px")
    data_visualizations.select_filters()
    data_visualizations.create_roles_report(data_visualizations.get_filtered_table("get_filtered_titles"))
    data_visualizations.create_roles_chart(data_visualizations.get_filtered_table("get_filtered_titles"))
    data_visualizations.create_roles_report(data_visualizations.get_filtered_table("get_skills_transferrability_trend"))
    data_visualizations.create_skill_transferrability_chart(data_visualizations.get_filtered_table("get_skills_transferrability_trend"))
    # $CHALLENGIFY_END
