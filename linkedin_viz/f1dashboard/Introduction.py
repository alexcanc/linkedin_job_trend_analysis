import streamlit as st

class F1Dashboard:
    def __init__(self, header_font_size="20px", text_font_size="14px") -> None:
        self.header_font_size = header_font_size
        self.text_font_size = text_font_size
        self.inject_custom_css()

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

    def introduction_page(self):
        """Layout the views of the dashboard"""

        st.title("LinkedIn Job & Skills Analysis Dashboard")
        st.write(
            """
            HI!!!!This is a dashboard designed for job seekers & career switchers in the UK.
            It is designed to help them identify on-demand skills and job roles in the UK data jobs market.
            The dashboard is built with **Skills Analysis** and **Job Roles Analysis**.
            You can navigate to the different pages using the sidebar.

            ---

            The page with the Skills Analysis allows a user of this dashboard to
            identify popular skills for a given job role. This will help user understand
            his/her skills gap in the current role or a role of interest. Based on this
            analysis, user can seek to upskill himself/herself with the required skills.

            ---

            The page with the Job Roles Analysis allows a user of this dashboard to
            identify popular job roles for a given skill. This will help user understand
            the relevance of their current skillset in the job market.
            """
        )

if __name__ == "__main__":
    dashboard = F1Dashboard(header_font_size="20px", text_font_size="14px")
    dashboard.introduction_page()
