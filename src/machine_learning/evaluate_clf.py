import streamlit as st
import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix


# Guidance from "05_PredictingAsthma" but adapted to show data frames
def confusion_matrix_and_report(X, y, pipeline, label_map):
    # Predict
    y_pred = pipeline.predict(X)

    # Confusion matrix
    st.write("--- Confusion Matrix ---")
    cm_df = pd.DataFrame(
        confusion_matrix(y_true=y, y_pred=y_pred),
        columns=[f"Predicted {label}" for label in label_map],
        index=[f"Actual {label}" for label in label_map],
    )
    st.dataframe(cm_df)

    # Classification report with only precision and recall
    st.write("--- Precision & Recall ---")
    report_dict = classification_report(
        y, y_pred, target_names=label_map, output_dict=True
    )
    # Convert to DataFrame
    report_df = pd.DataFrame(report_dict).transpose()
    report_df = report_df[
        ["precision", "recall"]
    ]  # keep only the two columns
    report_df = report_df.round(2)
    st.dataframe(report_df)


def clf_performance(X_train, y_train, X_test, y_test, pipeline, label_map):

    st.write("#### Train Set ####")
    confusion_matrix_and_report(X_train, y_train, pipeline, label_map)

    st.write("#### Test Set ####")
    confusion_matrix_and_report(X_test, y_test, pipeline, label_map)
