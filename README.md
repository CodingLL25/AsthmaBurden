# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In the terminal, run `heroku_config`
5. Paste in your API key when asked
You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API 

# Asthma Burden

## Project Overview

This project is a data analytics and machine learning application designed to explore, analyse, and interpret patient health data related to asthma. The objective is to identify key factors associated with lung function, and to support the prediction of asthma prognosis. The insights generated aim to enable early identification of high-risk individuals and support preventative, evidence-based clinical decision-making.

## Dataset Content

Data from the publicly available [Asthma Disease Dataset]( https://www.kaggle.com/datasets/rabieelkharoua/asthma-disease-dataset/data) was used. This dataset contained anonymised individual-level records, with each row representing a patient.

The dataset included the following variables:

### Patient Demographic Details

* Age
* Gender (0: Male, 1: Female)
* Ethnicity (0: Caucasian, 1: African American, 2: Asian, 3: Other)
* Education Level (0: None, 1: High School, 2: Bachelors, 3: Higher)

### Lifestyle Factors

* BMI
* Smoking Status (0: No, 1: Yes)
* Physical activity
* DietQuality
* SleepQuality

### Environmental and Allergy Factors

* PollutionExposure
* PollenExposure
* DustExposure
* PetAllergy

### Medical History

* FamilyHistoryAsthma (0: No, 1: Yes)
* HistoryOfAllergies (0: No, 1: Yes)
* Eczema (0: No, 1: Yes)
* HayFever (0: No, 1: Yes)
* GastroesophagealReflux (0: No, 1: Yes)

### Clinical Measurements

* LungFunctionFEV1
* LungFunctionFVC

### Symptoms

* Wheezing (0: No, 1: Yes)
* ShortnessOfBreath (0: No, 1: Yes)
* ChestTightness (0: No, 1: Yes)
* Coughing (0: No, 1: Yes)
* NighttimeSymptoms (0: No, 1: Yes)
* ExerciseInduced (0: No, 1: Yes)

### Diagnosis Information

* Diagnosis (0: No, 1: Yes)

### Confidential Information

* DoctorInCharge

DoctorInCharge is confidential information, however includes “Dr_Confid” as the value for all patients. All data is anonymised, with no personally identifiable information. 

## Business Requirements

The client seeks to better understand the prognosis of patients with asthma in order to identify high-risk individuals at an early stage. Early identification enables preventative interventions that can reduce the likelihood of severe outcomes. The objective of this project is to develop a machine learning model that predicts asthma prognosis by identifying key demographic, lifestyle, environmental, allergy-related, medical history, and symptom-based factors associated with lung function indicators (FEV1 and FVC).

To achieved the outlined objectives, this project will focus on the following key requirements:

### Business requirement one: Data visualisation and correlation study (conventional Analysis)

To identify and visualize the key demographic, lifestyle, environmental, allergy-related, medical history, and symptom-based factors associated with lung function measures (FEV1 and FVC).
* Perform exploratory data analysis (EDA) to assess distributions, trends, and relationships between patient attributes and lung function.
* Conduct correlation and statistical analyses to determine which factors are most strongly associated with variations in FEV1 and FVC.
* Produce clear, interpretable visualizations (e.g., correlation heatmaps, boxplots, scatter plots) to support clinical understanding.
Business Value: This analysis enables physicians and stakeholders to understand the primary drivers of lung function decline, supporting clinical insight and hypothesis generation prior to model deployment.

### Business requirement two: Prognosis Prediction via Supervised Learning (Machine Learning)

To develop a predictive model that classifies patients based on lung function status and overall asthma prognosis.
* Build and evaluate classification and/or regression models to predict lung function outcomes (e.g., good vs. poor lung function derived from FEV1 and FVC thresholds).
* Use patient attributes as inputs to identify individuals at higher risk of adverse asthma outcomes.
Business Value: This capability supports early risk stratification, enabling preventative interventions for patients likely to experience poor lung function and worse asthma prognosis.

## Hypothesis and how to validate?

* List here your project hypothesis(es) and how you envision validating it (them)

## The rationale to map the business requirements to the Data Visualizations and ML tasks

* List your business requirements and a rationale to map them to the Data Visualizations and ML tasks

## ML Business Case

* In the previous bullet, you potentially visualized an ML task to answer a business requirement. You should frame the business case using the method we covered in the course

## Dashboard Design

* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).

## Unfixed Bugs

* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/
* Set the runtime.txt Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.

## Credits

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.

* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

* The text for the Home page was taken from Wikipedia Article A
* Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/)
* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

None.

## Acknowledgements (optional)

* Thank the people who provided support through this project.
