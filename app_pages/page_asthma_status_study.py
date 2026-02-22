import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from src.data_management import load_patient_data


sns.set_style("whitegrid")

from scipy.stats import (
    chi2_contingency,
    fisher_exact,
    mannwhitneyu,
    ttest_ind,
    shapiro,
)

#  Load data and clean
df = load_patient_data()
df = df.astype({"Age": "float64"})
df = df.drop(columns=["PatientID", "DoctorInCharge"], errors="ignore")


def page_asthma_status_study_body():
    st.title("Asthma Status Study")

    # Overview of page
    st.info(
        "Asthma is a prevalent, burdensom disease with high prevalence. "
        "To help clinicians and researchers understand asthma further, "
        "this **Athma Status Study** focuses on answering"
        " **Business Requirement One**. Business requirement one is focused on"
        " identifying which factors are most correlated with asthma diagnosis."
        " To undersand such relationships, **visual** and **statistical** "
        "analyses were performed. "
    )

    if st.checkbox("Inspect Patient data"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows."
        )

        st.write(df.head(10))

    st.write("---")

    # Check distribution of the data
    st.write(
        "The dataset contains a multitude of variables for analysis. "
        "This included 10 numeric and 16 binary variables (PatientID and ) "
        "DoctorInCharge removed)."
        "Distributions were analysed to identify outliers. "
    )

    if st.checkbox("Distribution of continuous data"):
        violin_plots(df)

    if st.checkbox("Distribution of categorical data"):
        bar_plots(df)

    st.success(
        "No outliers were noted for numeric features. Additionally,  "
        "descriptive statistics for categorical variables showed no outliers "
        "(data not shown). However, for age and ethnicity, base sizes were "
        "small for specific groups, meaning they needed to be combined.\n"
        "Note, age was categorised as integer variable (amended to float)\n\n"
    )

    # Correlation study
    st.write(
        "* A correlation study was conducted to better understand the"
        "relationship between the variables and asthma diagnosis. \n"
        "However, due to the small pool of asthma patients the analyses "
        "was limited.\n\n"
        "No continuous variables were significantly correlated."
    )


# Functions for the charts
def violin_plots(df):
    continuous_features = df.select_dtypes(
        include="float"
    ).columns.tolist()

    fig, axes = plt.subplots(3, 4, figsize=(10, 8))
    axes = axes.flatten()

    for ax, feature in zip(axes, continuous_features):
        sns.violinplot(
            x="Diagnosis",
            y=feature,
            data=df,
            hue="Diagnosis",
            ax=ax,
            inner="box",
            palette="Set2",
            legend=False,
        )
        ax.set_title(feature, fontsize=10)
        ax.set_xlabel(ax.get_xlabel(), fontsize=8)
        ax.set_ylabel(ax.get_ylabel(), fontsize=8)
        ax.tick_params(axis="both", which="major", labelsize=7)  #

    plt.tight_layout()
    st.pyplot(fig)


def bar_plots(df):
    """
    Function to create the bar plots based on contigency tables.
    Amends were made to the code from 03_DataExploration re: too big"""
    target = "Diagnosis"
    binary_features = df.select_dtypes(include="int").columns.drop(target)
    contingency_tables = {}

    for feature in binary_features:
        contingency_tables[feature] = pd.crosstab(df[target], df[feature])

    fig, axes = plt.subplots(4, 4, figsize=(12, 9), dpi=80)
    axes = axes.flatten()

    for ax, (feature, table) in zip(axes, contingency_tables.items()):
        proportion_table = table.div(table.sum(axis=1), axis=0) * 100
        # Reindex columns to ensure consistent order of categories
        proportion_table = proportion_table.reindex(
            columns=[0, 1, 2, 3], fill_value=0
        )
        # Plot without legend
        proportion_table.plot(
            kind="bar",
            stacked=False,
            ax=ax,
            colormap="tab10",
            legend=False,
        )
        ax.set_title(feature, fontsize=10)
        ax.set_ylabel("Proportion (%)", fontsize=9)
        ax.set_ylim(0, 100)

    # Make a shared legend for 0, 1, 2, 3
    unique_values = ["0", "1", "2", "3"]
    colors = plt.get_cmap("tab10").colors[: len(unique_values)]
    handles = [plt.Line2D([0], [0], color=c, lw=4) for c in colors]

    fig.legend(
        handles,
        unique_values,
        title="Value",
        loc="lower center",
        ncol=4,
        fontsize=9,
    )

    plt.tight_layout(rect=[0, 0.05, 1, 1])
    st.pyplot(fig)
