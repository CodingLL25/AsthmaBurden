import streamlit as st


def page_summary_body():
    """
    Streamlit page summarising the project jargon, information and business
    requirements.
    """
    st.title("Project Summary")

    st.info("""
        In the healthcare sector, effective early detection of conditions like 
        asthma is critical to improving patient outcomes and reducing 
        preventable complications. Undiagnosed asthma can lead to severe 
        health setbacks and increased healthcare utilization. 
        The Asthma Burden project aims to help healthcare providers better 
        understand the drivers of asthma risk and proactively identify 
        patients who may have undiagnosed or under-recognized asthma.

        From a business perspective, this project helps healthcare institutions 
        identify high-risk patients early, make data-driven care decisions,
        and provide targeted interventions for at-risk individuals. 
        These insights support improved clinical outcomes, operational efficiency, 
        and resource allocation.
        
        Note, this project was created as part of a full stack diploma.
    """)

    # Overview of key words
    st.info("""
        **Project Terms & Jargon**

        * A **patient** is an individual whose health data is recorded in the
            dataset.
        * An **asthma** patient refers to a patient who has been diagnosed with
            asthma.
        * A **feature** refers to a variable in the dataset.
        * **Target Feature** refers to the variable of interest, i.e. asthma
            diagnosis.
        * A **non-asthma patient** is someone in the dataset without an asthma
            diagnosis.
        * **Clinical measurements** are numerical indicators such as forced
            expiratory volume (LungFunctionFEV1) and forced vital capacity
            (LungFunctionFVC), that reflect lung capacity and function.
        * **Lifestyle factors** include body mass index (BMI), physical
            activity, diet quality, sleep quality, and smoking status.
        * **Environmental and allergy factors** describe exposure to pollution,
            dust, pollen, or pet allergens.
        * **Medical history** includes prior conditions like eczema, hayfever,
            gastroesophageal reflux, or family history of asthma.
        * **Symptoms** are patient-reported indicators such as wheezing,
            chest tightness, coughing, or shortness of breath.
    """)

    # Dataset summary
    st.info("""
        **Project Dataset**

        * The dataset represents an anonymised **Asthma Disease Dataset**
            from [Kaggle](https://www.kaggle.com/datasets/rabieelkharoua/
            asthma-disease-dataset/data), containing individual-level patient
            data.
        * Each record includes demographic, lifestyle, environmental, allergy,
            medical history, clinical measurements, and symptom features,
            as well as a binary asthma diagnosis.
        * The dataset contains 2,392 patients, of which 124 have asthma,
            reflecting a highly imbalanced real-world population.

        Each row represents a patient record with demographic, lifestyle,
            environmental, allergy-related, symptom-based, and clinical
            attributes. The target variable, **Diagnosis**, indicates whether
            the patient has asthma (`0` = no asthma, `1` = asthma).

        **Dataset variables**

        **Numeric Variables (10):**
        - Age (5–80 years)
        - BMI (15–40)
        - PhysicalActivity (hours/week, 0–10)
        - DietQuality (0–10)
        - SleepQuality (4–10)
        - PollutionExposure (0–10)
        - PollenExposure (0–10)
        - DustExposure (0–10)
        - LungFunctionFEV1 (1.0–4.0 L)
        - LungFunctionFVC (1.5–6.0 L)

        **Categorical Variables (18):**
        - PatientID (unique identifier)
        - Gender (0 = Male, 1 = Female)
        - Ethnicity (0 = Caucasian, 1 = African-American, 2 = Asian, 3 = Other)
        - EducationLevel(0 = None, 1 = High School, 2 = Bachelor's, 3 = Higher)
        - Smoking (0 = No, 1 = Yes)
        - PetAllergy (0 = No, 1 = Yes)
        - FamilyHistoryAsthma (0 = No, 1 = Yes)
        - HistoryOfAllergies (0 = No, 1 = Yes)
        - Eczema (0 = No, 1 = Yes)
        - HayFever (0 = No, 1 = Yes)
        - GastroesophagealReflux (0 = No, 1 = Yes)
        - Wheezing (0 = No, 1 = Yes)
        - ShortnessOfBreath (0 = No, 1 = Yes)
        - ChestTightness (0 = No, 1 = Yes)
        - Coughing (0 = No, 1 = Yes)
        - NighttimeSymptoms (0 = No, 1 = Yes)
        - ExerciseInduced (0 = No, 1 = Yes)
        - Diagnosis (target variable, 0 = No asthma, 1 = Yes)
        - DoctorInCharge (all values 'Dr_Confid')

        DoctorInCharge and PatientID were not used for analyses.

        No **missing data** or **duplicate entries** were noted during data
            cleaning.
    """)

    # Business Requirements
    st.success("""
        The project has two business requirements:

        1. **Data Insights (Conventional Analysis)**: Identify and visualize
            the key demographic, lifestyle, environmental, allergy-related,
            medical history, symptom-based, and clinical factors associated
            with asthma status. Perform exploratory data analysis to examine
            distributions and group differences between asthma and non-asthma
            patients. Use interpretable visualizations such as boxplots for
            categorical/binary data, violin plots for numerical data, and
            correlation figures to highlight important relationships.

        2. **Classification Model (Machine Learning)**: Develop a predictive
            model to identify patients with asthma, accounting for the highly
            imbalanced nature of the dataset. Apply techniques like class
            weighting, SMOTE, or anomaly detection to improve sensitivity to
            asthma cases. Evaluate model performance using recall and precision
            to ensure effective early identification.
    """)

    # Link to README file for full project documentation
    st.write(
        "* For additional information, please visit and **read** the "
        "[Project README file](https://github.com/CodingLL25/AsthmaBurden)."
    )
