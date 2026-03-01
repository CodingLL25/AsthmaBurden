import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from src.data_management import load_patient_data
from scipy.stats import (
    chi2_contingency,
    fisher_exact,
    mannwhitneyu,
    ttest_ind,
    shapiro,
)


sns.set_style("whitegrid")

#  Load data and clean
df = load_patient_data()
df = df.astype({"Age": "float64"})
df = df.drop(columns=["PatientID", "DoctorInCharge"], errors="ignore")


def page_asthma_status_study_body():
    """
    Streamlit page for the exploratory data analysis.
    """
    st.title("Asthma Status Study")

    # Overview of page
    st.info("""
        Asthma is a prevalent, burdensome disease with high prevalence.
        To help clinicians and researchers understand asthma further,
        this **Athma Status Study** focuses on answering
        **Business Requirement One**. Business requirement one is focused on
        identifying which factors are most correlated with asthma diagnosis.
        To undersand such relationships, **visual** and **statistical**
        analyses were performed.
    """)

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
        "This included 10 numeric and 16 binary variables (PatientID and "
        "DoctorInCharge removed). "
        "Distributions were analysed to identify outliers. "
    )

    if st.checkbox("Distribution of continuous data"):
        violin_plots(df)

    if st.checkbox("Distribution of categorical data"):
        bar_plots(df)

    st.success("""
        No outliers were noted for numeric features. Additionally,
        descriptive statistics for categorical variables showed no outliers
        (data not shown). However, for age and ethnicity, base sizes were
        small for specific groups, meaning they needed to be combined.

        Note, age was categorised as integer variable (amended to float).
    """)

    # Correlation study
    st.write("""
        * A correlation study was conducted to better understand the
        relationship between the variables and asthma diagnosis.
        However, due to the small pool of asthma patients the findings
        were limited (imbalanced sample).

        No continuous variables were significantly correlated.
    """)

    # Updated data frame
    df_updated = process_categorical(df)

    # Correlation data - continuous variables
    continuous_results_df = continuous_significance(df_updated)

    if st.checkbox("Continuous data significance:"):
        st.dataframe(
            continuous_results_df.style.format(
                {"statistic": "{:.3f}", "p-value": "{:.4f}"}
            )
        )

    st.success("""
        One categorical variables was significantly correlated with asthma
        status. This could relate to the specific type of asthma the patient
        has been diagnosed with (exercise induced).
    """)

    # Correlation data - binary variables
    binary_results_df = binary_significance(df_updated)

    if st.checkbox("Binary data significance:"):
        st.dataframe(
            binary_results_df.style.format(
                {"statistic": "{:.3f}", "p-value": "{:.4f}"}
            )
        )

    # Feature-Target correlation
    st.write("""
        Additional analyses were performed to assess the linear relationships
        between features and the target variable using correlation analysis.
        A feature–target correlation plot was generated to evaluate the
        strength and direction of associations, as well as to explore
        potential multicollinearity among predictors. This provided an
        alternative route for assessing meaninful relationships with the
        target feature.
    """)

    if st.checkbox("Feature-Target Correlation:"):
        st.dataframe(
            feature_target_correlation_plot(df_updated)
        )

    st.success("""
        Most features show very weak correlations with asthma status,
        indicating limited linear relationships.

        Exercise-induced symptoms has the strongest positive correlation,
        possibly reflecting the specific asthma subtype diagnosed.
        While chest tightness shows the strongest negative correlation.
    """)


# Functions for the charts
def violin_plots(df):
    continuous_features = df.select_dtypes(
        include="float"
    ).columns.tolist()

    fig, axes = plt.subplots(3, 4, figsize=(10, 8), dpi=40)
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

    fig, axes = plt.subplots(4, 4, figsize=(12, 9), dpi=40)
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


def process_categorical(df):
    """
    Consolidate Ethnicity and EducationLevel into simplified binary categories.
    """
    df_updated = df.copy()

    # Simplify Ethnicity
    df_updated["Ethnicity"] = df_updated["Ethnicity"].replace(
        {
            0: 0,  # White
            1: 1,  # African American → 1
            2: 1,  # Asian → 1
            3: 1,  # Other → 1
        }
    )

    # Simplify EducationLevel
    df_updated["EducationLevel"] = df_updated["EducationLevel"].replace(
        {
            1: 1,  # Bachelor/Higher
            2: 1,  # Bachelor/Higher
            3: 0,  # None/High school
        }
    )

    return df_updated


def continuous_significance(df_updated):
    """
    Create a dataframe for continuous results
    """
    continuous_features = df_updated.select_dtypes(
        include="float"
    ).columns.tolist()

    continuous_results = {}

    for feature in continuous_features:
        group0 = df_updated[df_updated["Diagnosis"] == 0][feature].dropna()
        group1 = df_updated[df_updated["Diagnosis"] == 1][feature].dropna()

        # Check normality
        _, p0 = shapiro(group0) if len(group0) >= 3 else (None, 0)
        _, p1 = shapiro(group1) if len(group1) >= 3 else (None, 0)

        # Choose t-test if normal distribution, else Mann-Whitney
        if p0 > 0.05 and p1 > 0.05:
            stat, p = ttest_ind(group0, group1, equal_var=False)
            test_name = "t-test"
        else:
            stat, p = mannwhitneyu(group0, group1, alternative="two-sided")
            test_name = "Mann-Whitney U"

        significance = "Significant" if p < 0.05 else "Not significant"

        continuous_results[feature] = {
            "test": test_name,
            "statistic": stat,
            "p-value": p,
            "significance": significance,
        }

    # Create a dataframe and return it
    continuous_results_df = pd.DataFrame(continuous_results).T
    continuous_results_df.index.name = "Feature"
    return continuous_results_df


def binary_significance(df_updated):
    """
    Create a dataframe for binary results
    """
    # Remove diagnosis for analysis
    binary_features = [
        col
        for col in df_updated.select_dtypes("int").columns
        if col != "Diagnosis"
    ]

    # Create an empty dictionary for the results
    binary_results = {}

    # Loop through features, recreate contigency tables, and significance
    for feature in binary_features:
        table = pd.crosstab(df_updated[feature], df_updated["Diagnosis"])

        # Run chi-square test
        chi2, p_chi, dof, expected = chi2_contingency(table)

        # Decide whether to use Fisher (if any expected count < 5)
        if (expected < 5).any():
            oddsratio, p_value = fisher_exact(table)
            test_used = "Fisher's exact"
        else:
            p_value = p_chi
            oddsratio = (table.iloc[1, 1] / table.iloc[1, 0]) / (
                table.iloc[0, 1] / table.iloc[0, 0]
            )
            test_used = "Chi-square"

        # Significance
        significance = (
            "Significant" if p_value < 0.05 else "Not significant"
        )

        # Overview of the output
        binary_results[feature] = {
            "test": test_used,
            "p-value": p_value,
            "odds_ratio": oddsratio,
            "significance": significance,
        }

    binary_results_df = pd.DataFrame(binary_results).T
    binary_results_df.index.name = "Feature"
    return binary_results_df


def feature_target_correlation_plot(df_updated):
    """
    Generates a heatmap of feature-target correlations for a Streamlit app.
    """
    features = df_updated.drop(["Diagnosis"], axis=1)
    target = df_updated["Diagnosis"]

    correlation_matrix = features.corrwith(target)
    fig, ax = plt.subplots(figsize=(8, 6))
    corr_df = pd.DataFrame(correlation_matrix, columns=["Correlation"])

    sns.heatmap(
        corr_df,
        annot=True,
        cmap="coolwarm",
        cbar=True,
        ax=ax
    )

    ax.set_title("Feature-Target Correlation Matrix", fontsize=14)
    st.pyplot(fig)
