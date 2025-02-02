# CreditGuard: Application for Default Detection
[![English version](https://img.shields.io/badge/lang-en-red.svg)](README.md)
&nbsp;&nbsp;
[![Portuguese version](https://img.shields.io/badge/lang-pt--br-green.svg)](README.pt-br.md)

`CreditGuard` is an application for analyzing loan applications and making data-driven decisions on whether to lend to an applicant. The application uses predictive models to determine the likelihood of an applicant repaying the loan.

The chosen machine learning model is `Random Forest`, which was trained using the dataset from [laotse/credit-risk-dataset](https://www.kaggle.com/datasets/laotse/credit-risk-dataset). To learn more about the project, read [this notebook](/docs/notebook/notebook_default_loan.pt-br.ipynb).

This project was developed as part of the evaluation for the course `Smart Deployment: Systems with Predictive Models` at SENAC Pernambuco.

## Microservices Architecture

The project was developed with a microservices architecture, consisting of the following components:

### 1. `backend`
- The `backend` component is responsible for all business logic, including exposing APIs, authentication, authorization, and data management.

### 2. `frontend`
- The `frontend` component is responsible for the user interface, providing an interactive and responsive experience for the end users. It communicates with the `backend` via APIs.

### 3. `etl`
- The `etl` component is responsible for **extracting**, **transforming**, and **loading** the data into the database. It is also in charge of correcting and cleaning data, performing the following transformations:
    - **Age Correction**:
      - It was identified that some records had unrealistic ages, such as 140 years. Based on the assumption that no one should be older than 115 years, the ages of these records were corrected.
      - The correction was done by replacing the ages of these outliers with the average age of the 5 most similar records using the KNN algorithm.
    - **Missing Data Imputation**:
      - For missing data, imputation was applied using the average of the 5 nearest records, utilizing the KNN algorithm.
    - **Categorical Variable Transformation**:
      - Categorical variables, both ordinal and nominal, were transformed using the One-Hot-Encoding technique (for nominal variables) and Label Encoding (for ordinal variables).
    - **Variable Scaling**:
      - Continuous and discrete variables were scaled to optimize the model learning. The technique used was normalization/standardization, which was saved in the `etl` component to be used later.
    - **Saving the Scaling Model**:
      - The scaling model was trained and saved locally to be reused for future transformations.
    - **Note**: The `etl` component is also responsible for saving the variable scaling model.

    For more details on how the `etl` component works, read the document [here](/etl/README.md).

### 4. `ml`
- The `ml` component is responsible for training the machine learning model and saving it locally. It is fed by the data transformed by the `etl` component and performs predictions based on the trained model.

## Project Structure

```plaintext
├── backend/                        # Backend
├── docs/                           # Project documents (ex: diagrams)
├── dataset/                        # data repository, store raw, trusted, features and logs
├── ml/                             # ML training code, store ml model and scaler
├── etl/                            # ETL code
├── frontend/                       # Project documents (ex: diagrams)
├── .gitignore
├── README.md                       # Main documentation
└── README.pt-br.md  
```

## Requirements

## How to Use

## License
