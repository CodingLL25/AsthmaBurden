import streamlit as st

def page_project_hypothesis_body():
    """ 
    Streamlit page for the project/study hypotheses.
    """
    st.title("Project Hypothesis and Validation")

    st.markdown(
        """
        To better understand the factors influencing asthma risk, four key hypotheses were formulated based on domain knowledge and the available data. Each hypothesis focuses on a variable expected to impact asthma status.

        | Hypothesis | Rationale | Validation |
        |------------|-----------|------------|
        | **H1: Poorer clinical factors (lower LungFunctionFEV1 or LungFunctionFVC) is associated with asthma** | Reduced airflow and obstruction are classic features of asthma | Compare distributions of lung function metrics by Diagnosis; use of t-tests or Mann-Whitney to confirm differences |
        | **H2: Presence of symptoms (Wheezing, ShortnessOfBreath, ChestTightness, Coughing, NighttimeSymptoms) is associated with asthma** | Symptoms like wheeze are clinical hallmarks of asthma and likely predictive of diagnosis | Compare symptom prevalence by Diagnosis; assess association with Chi-square tests |
        | **H3: Smoking exposure is associated with asthma** | Smoking and secondhand smoke irritate airways and can exacerbate or trigger asthma symptoms | Compare SmokingHistory by Diagnosis; statistical tests for association |
        | **H4: Higher exposure to dust or pollutants is associated with higher asthma risk** | Environmental irritants can trigger asthma attacks or chronic inflammation | Compare PollutionExposure, PollenExposure and DustExposure by Diagnosis; statistical test for differences |

        """
    )

    st.error(
        "Only two features, **ExerciseInduced** and **ChestTightness**, showed "
        "meaningful correlation with asthma diagnosis during exploratory "
        "data analysis. None of the initial hypotheses were strongly supported "
        "by the data, indicating the need for further investigation."
    )
