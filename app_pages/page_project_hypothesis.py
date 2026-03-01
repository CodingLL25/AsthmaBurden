import streamlit as st


def page_project_hypothesis_body():
    """
    Streamlit page for the project/study hypotheses.
    """
    st.title("Project Hypothesis and Validation")

    st.info("""
        To better understand the factors influencing asthma risk, four key 
        hypotheses were formulated based on domain knowledge and the available 
        data. Each hypothesis focuses on a variable expected to impact asthma
        status.
    """)

    st.markdown(
        """
        | Hypothesis | Rationale | Validation |
        |------------|-----------|------------|
        | **H1: Poorer clinical factors (lower LungFunctionFEV1 or LungFunctionFVC) is associated with asthma** | Reduced airflow and obstruction are classic features of asthma | Compare distributions of lung function metrics by Diagnosis; use of t-tests or Mann-Whitney to confirm differences |
        | **H2: Presence of symptoms (Wheezing, ShortnessOfBreath, ChestTightness, Coughing, NighttimeSymptoms) is associated with asthma** | Symptoms like wheeze are clinical hallmarks of asthma and likely predictive of diagnosis | Compare symptom prevalence by Diagnosis; assess association with Chi-square tests |
        | **H3: Smoking exposure is associated with asthma** | Smoking and secondhand smoke irritate airways and can exacerbate or trigger asthma symptoms | Compare SmokingHistory by Diagnosis; statistical tests for association |
        | **H4: Higher exposure to dust or pollutants is associated with higher asthma risk** | Environmental irritants can trigger asthma attacks or chronic inflammation | Compare PollutionExposure, PollenExposure and DustExposure by Diagnosis; statistical test for differences |

        """
    )

    st.success("""
        The feature-target correlation matrix shows generally weak linear
        relationships between individual features and asthma risk, with
        correlation values close to zero. However, some patterns align with
        our four key hypotheses, providing initial quantitative support for
        clinical and environmental factors related to asthma:

        - Hypothesis 1 (H1): Lung function metrics (LungFunctionFEV1
            and LungFunctionFVC) show a slight positive correlation with the
            target, suggesting poorer lung function relates to asthma status.

        - Hypothesis 2 (H2): Symptoms like Wheezing show weak positive
            correlation (0.027), while others have minimal correlations.

        - Hypothesis 3 (H3): Smoking has a small negative correlation,
            suggesting a subtle relationship with asthma.

        - Hypothesis 4 (H4): Environmental exposures such as
            DustExposure show mild negative correlation.

        Overall, these correlation results aligned with our hypotheses.
        However, upon statistical testing, only excerise induced was
        signifcantly associated with asthma.
    """)
