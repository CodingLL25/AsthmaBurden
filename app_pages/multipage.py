import streamlit as st

# Welcome message
def welcome():
    st.markdown("## 👋 Welcome")

    st.write("""
    Welcome to the application!

    This app allows you to explore different features using the sidebar.
    """)

    st.info("Select a page from the menu to begin.")

# Class to generate multiple Streamlit pages using an object oriented approach 
class MultiPage: 

    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon="🖥️",
            layout="wide"
        )

    def add_page(self, title, func) -> None: 
        self.pages.append({
            "title": title,
            "function": func
        })

    def run(self):
        st.title(self.app_name)

        page = st.sidebar.radio(
            'Menu',
            self.pages,
            format_func=lambda page: page['title']
        )

        page['function']()