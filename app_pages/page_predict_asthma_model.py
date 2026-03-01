import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_patient_data, load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance


def page_predict_asthma_model_body():
    """ 
    Streamlit page for predicting asthma status (diagnosis).
    """
    st.title("Machine Learning: Predicting Asthma Status")

    # Load prediction pipeline
    version = 'v1'
    asthma_pipeline_dc_fe = load_pkl_file(
        f'outputs/modeling_pipeline/predict_asthma/{version}/'
        'clf_pipeline_data_cleaning_feat_eng.pkl'
    )
    asthma_pipeline_model = load_pkl_file(
        f'outputs/modeling_pipeline/predict_asthma/{version}/clf_pipeline_model.pkl'
    )
    asthma_feature_importance = plt.imread(
        f"outputs/modeling_pipeline/predict_asthma/{version}/features_importance.png")

    X_train = pd.read_csv(
        f"outputs/modeling_pipeline/predict_asthma/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/modeling_pipeline/predict_asthma/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/modeling_pipeline/predict_asthma/{version}/y_train.csv").values
    y_test = pd.read_csv(
        f"outputs/modeling_pipeline/predict_asthma/{version}/y_test.csv").values

    st.write("## Predicting Asthma Status")
    st.info(
        "Business requirement two was to develop a predictive model that "
        "identifies patients with asthma within a highly imbalanced dataset. "
        "Key metrics were defined at project kick-off. The aim was to provide "
        "stakeholders with a tool for predicting asthma status to help guide "
        "clinical decisions and so forth.\n\n"
        "Success was defined as:\n"
        "- Recall for asthma ≥ 0.80 (minimise false negatives)\n"
        "- Precision for asthma ≥ 0.60 (minimise false positives)"
    )

    st.write("### Pipelines")
    st.write(" * The first is responsible for data cleaning and feature engineering.")
    st.write(asthma_pipeline_dc_fe)

    st.write("* The second is for feature scaling and modelling.")
    st.write(asthma_pipeline_model)

    st.write("### Feature Importance")
    st.write("The model was trained using the following features:")
    st.write(X_train.columns.to_list())
    st.image(asthma_feature_importance)

    # Pipeline performance
    st.write("### Pipeline Performance")
    clf_performance(
        X_train=X_train,
        y_train=y_train,
        X_test=X_test,
        y_test=y_test,
        pipeline=asthma_pipeline_model,
        label_map=['No asthma', 'Asthma']
    )

    st.write("### Performance summary")
    st.error(
        "Both metrics did not meet success criteria:\n\n"
        "- Train set: Recall = 0.53, Precision: 0.07.\n"
        "- Test set: Recall = 0.49, Precision: 0.06.\n\n"
        "Precision was low due to a high number of false positives meaning "
        "the model predicts a high number of incorrect asthma cases.\n"
        "Recall was moderate, with round half actual asthma cases being "
        "identified.\n\n"
        "However, due to the inability to identify asthma cases, this model "
        "was not utilised to create a prediction tool for stakeholders. "
        "A more in depth dataset, capturing more specific features related to "
        "asthma, as well as more asthma patients would be required to "
        "investigate this further."
    )