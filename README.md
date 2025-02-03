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

### Configuring the `etl` Module
1. The first step is to prepare the data using the `etl` module script.
2. To do this, download the dataset from `Kaggle` ([click here](https://www.kaggle.com/datasets/laotse/credit-risk-dataset)) and create a `dataset/raw` directory at the root of your project. Save the `csv` file there.
   - You can customize the destination of the `etl` process data by creating a `.env` file in the `etl` directory and configuring the following variables:
     - `LOG_DIRECTORY`: Determines where the `etl` process logs will be saved. By default, it is `../dataset/logs/etl`.
     - `ML_ARTIFACTS_DIRECTORY`: Determines where the `scale` model will be saved, responsible for keeping all dataset `features` at the same scale. Default value: `../ml/artifacts/models`.
     - `TARGET_PARTITION`: Determines where the target variables of the dataset, such as `loan_status`, will be saved. Default value: `../dataset/features/`.
     - `FEATURE_PARTITION`: Determines where the dataset features will be saved. Default value: `../dataset/features`.
     - `TRUSTED_PARTITION`: Determines where the pre-processed data will be saved. Default value: `../dataset/trusted`.
     - `RAW_PARTITION`: Determines where the dataset is located. Default value: `../dataset/raw/credit_risk_dataset.csv`. Pay attention to the dataset name or use a wildcard, e.g., `../dataset/raw/*`.
     - **Note**: The `etl` module code will run in the `etl` directory, so `../` saves at the root of the project. If omitted, data will be saved within the `etl` directory.
3. Once the execution environment for the `etl` module is set up, use the following commands:
   1. `cd ./etl`: Open the terminal in the `etl` directory.
   2. `python -m venv .venv`: Create a project-level virtual environment.
   3. `.venv/Scripts/activate`: Activate the project-level virtual environment.
   4. `pip install -r requirements.txt`: Install all dependencies required to run the `etl` module.
   5. `python main.py`: Run the `etl` process.
   6. `deactivate`: Deactivate the virtual environment for the `etl` module.
   7. `cd ..`: Return to the project root.

### Configuring the `ml` Module
4. Now that you have the features and targets for training the machine learning model, you need to configure the machine learning module.
5. Go to the `ml` directory and create a `.env` file with the following variables:
   - `TARGET_PARTITION`: Indicates the path where the target variable data is stored. Default: `../dataset/features/*/*/*/target-*.csv`.
   - `FEATURE_FEATURE`: Indicates the path where the feature data is stored. Default: `../dataset/features/*/*/*/feature-*.csv`.
   - `MODEL_PARTITION`: Indicates the path where the trained machine learning model will be saved. Default: `./artifacts/models`.
   - `MODEL_ALG`: Indicates the algorithm used for training the machine learning model. Default: `rf`.
   - `MODEL_VERSION`: Indicates the version of the machine learning model. Default: `1.0.0`.
   - `LOG_DIRECTORY`: Indicates the location where training logs will be saved. Default: `../dataset/logs/training`.
   - **Note**: Data is saved by the `etl` module following this convention: `{partition}/YYYY/MM/DD/{timestamp}.csv`. Feature and target data follow: `features/YYYY/MM/DD/{target|feature}-{timestamp}.csv`.
   - **Note 2**: The model is saved using the naming convention `{MODEL_ALG}-{MODEL_VERSION}-{timestamp}.pkl`.
6. Once the execution environment for the `ml` module is set up, use the following commands:
   1. `cd ./ml`: Open the terminal in the `ml` directory.
   2. `python -m venv .venv`: Create a project-level virtual environment.
   3. `.venv/Scripts/activate`: Activate the project-level virtual environment.
   4. `pip install -r requirements.txt`: Install all dependencies required to run the `ml` module.
   5. `python main.py`: Run the `ml` process.
   6. `deactivate`: Deactivate the virtual environment for the `ml` module.
   7. `cd ..`: Return to the project root.

### Configuring the `backend` Module
7. With both models - one for prediction and one for feature scaling - you can configure the application `backend`.
8. Go to the `backend` directory, create a `.env` file, and configure the following variables:
   - `API_V_STR`: Determines the endpoint suffix. Default: `/api/v1`.
   - `DB_URL`: Determines the database connection. Default: `localhost:5432/creditguard_db` (function not implemented).
   - `ENVIRONMENT`: Determines whether the backend environment is production or development. Default: `DEVELOPMENT`. If set to `PRODUCTION`, Google Drive authentication variables must be provided.
   - `GOOGLE_API_PROJECT_ID`: Required when configuring the backend for production. Needed for calling the Google Drive API and deploying the project.
   - `GOOGLE_API_SERVICE_ID`: Required for production. Needed for calling the Google Drive API and deploying the project.
   - `GOOGLE_API_SERVICE_EMAIL`: Required for production. Needed for calling the Google Drive API and deploying the project.
   - `GOOGLE_API_SERVICE_PRIVATE_KEY_ID`: Required for production. Needed for calling the Google Drive API and deploying the project.
   - `GOOGLE_API_SERVICE_PRIVATE_KEY`: Required for production. Needed for calling the Google Drive API and deploying the project.
   - `BACKEND_PORT`: Determines the port where the project runs. Default: `8080`.
   - `BACKEND_HOST`: Determines the backend host. Default: `localhost`.
   - `MODEL_ARTIFACT_URI`: Determines the path to the trained model. Default: `../ml/artifacts/models/rf-1.0.0-*.pkl`. Check the exact model name.
   - `SCALER_ARTIFACT_URI`: Determines the path to the trained scaler model for feature scaling. Default: `../ml/artifacts/utils/scaler.pkl`.
   - **Note**: In production, `MODEL_ARTIFACT_URI` and `SCALER_ARTIFACT_URI` should be set with the respective object IDs stored in Google Drive.
   - `FRONTEND_URL`: Determines the frontend URL for CORS purposes. Default: `http://localhost:8501`.
9. Once the execution environment for the `backend` module is set up, use the following commands:
   1. `cd ./backend`: Open the terminal in the `backend` directory.
   2. `python -m venv .venv`: Create a project-level virtual environment.
   3. `.venv/Scripts/activate`: Activate the project-level virtual environment.
   4. `pip install -r requirements.txt`: Install all dependencies required to run the `backend` module.
   5. `fastapi run main.py`: Start the backend. To stop, press `Ctrl+C` or close the terminal.
   6. `deactivate`: Deactivate the virtual environment for the `backend` module.
   7. `cd ..`: Return to the project root.
### Setting up the `frontend` module  

10. Keep the `backend` running in one terminal and open another.  
11. Go to the `frontend` directory and create a `.env` file in the directory, then configure the following variables:  
   - `BACKEND_URL`: This variable specifies the API URL. By default, its value is `localhost:8000/api/v1/ml/loan_default`.  
12. Once the execution environment for the `frontend` module is set up, use the following commands:  
   1. `cd ./ml`: Open the terminal inside the `frontend` directory.  
   2. `python -m venv .venv`: Creates a project-level virtual environment.  
   3. `.venv/Scripts/activate`: Activates the project-level virtual environment.  
   4. `pip install -r requirements.txt`: Installs all the necessary dependencies to run the `frontend` module.  
   5. `streamlit run index.py`: Runs the frontend. To close it, press `Ctrl+C` or close the terminal.  
   6. `deactivate`: Deactivates the `frontend` module's virtual environment.  
   7. `cd ..`: Returns to the project's root directory.

## License
