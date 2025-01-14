"""
The page with the descriptive statistics allows a user of this dashboard
to get the summary statistics of the tables in the database.
"""
import streamlit as st
from f1dashboard.advanced.state import F1State
from f1dashboard.advanced.constants import F1Constants
from f1dashboard.advanced.database import LinkedinDatabase
from f1dashboard.advanced.queries import F1Queries


class DescriptiveStatistics:
    def __init__(self, header_font_size="20px", text_font_size="14px") -> None:
        """Initialize the class"""
        self.header_font_size = header_font_size
        self.text_font_size = text_font_size
        self.inject_custom_css()

        self.f1_state = F1State()
        # self.f1_database = F1Database()
        self.f1_queries = F1Queries()
        self.linkedin_db = LinkedinDatabase()

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

    def select_table(self):
        """Select the table to explore"""
        with st.sidebar:
            st.subheader("Select table to explore")
            self.selected_table = "races"
            # TODO: REPLACE THIS LINE ABOVE BY A "st.selectbox" using F1Constants
            # $CHALLENGIFY_BEGIN
            self.selected_table = st.selectbox("Table name", F1Constants.table_names())
            # $CHALLENGIFY_END

    def summary_statistics(self):
        """st.write summary statistics of the selected dable"""
        st.title("Descriptive statistics")

        if self.selected_table in st.session_state:
            st.info(f"Retrieve the {self.selected_table} table from state...")
            # $CHALLENGIFY_BEGIN
            table_results = self.f1_state.get_data_from_state(self.selected_table)
            # $CHALLENGIFY_END
        else:
            st.info(f"Retrieve the {self.selected_table} table from the database...")
            # $CHALLENGIFY_BEGIN
            table_results = self.f1_queries.retrieve_table(self.selected_table)
            # $CHALLENGIFY_END
            st.info(f"Saving the {self.selected_table} table to state...")
            # $CHALLENGIFY_BEGIN
            self.f1_state.store_in_state(self.selected_table, table_results)
            # $CHALLENGIFY_END

        # TODO: describe the table_results data
        # $CHALLENGIFY_BEGIN
        st.write(table_results.describe())
        # $CHALLENGIFY_END


if __name__ == "__main__":
    data_visualizations = DescriptiveStatistics(header_font_size="26px", text_font_size="14px")
    data_visualizations.select_table()
    data_visualizations.summary_statistics()
