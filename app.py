import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_asthma_status_study import page_asthma_status_study_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_predict_asthma_model import page_predict_asthma_model_body


app = MultiPage(app_name= "AsthmaBurden") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Asthma Status Study", page_asthma_status_study_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("Machine Learning: Prospect Asthma Patient", page_predict_asthma_model_body)

app.run() # Run the  app