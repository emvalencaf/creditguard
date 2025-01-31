import pandas as pd
import joblib
from sklearn.impute import KNNImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Project dependencies
from helpers.datetime_partition import get_datetime_partition, get_timestamp
from helpers.calc import calculate_expected_loan_percent
from helpers.logging import get_logging
from helpers.makedir import ensure_dir
from config import global_settings

# Logging configuration
logging = get_logging()

if __name__ == "__main__":
    try:
        logging.info("Starting ETL process.")
        base_credit = pd.read_csv('../dataset/raw/credit_risk_dataset.csv')
        logging.info("Dataset successfully loaded.")
        
        date_dir = get_datetime_partition()
        
        # Fixing loan_percent_income inconsistencies
        base_credit['expected_loan_percent'] = calculate_expected_loan_percent(base_credit)
        base_credit['loan_percent_income'] = base_credit['expected_loan_percent']
        base_credit.drop(columns=['expected_loan_percent'], inplace=True)
        logging.info("loan_percent_income fixed.")
        
        # Fixing person_age inconsistencies
        base_credit.loc[base_credit['person_age'] > 115, 'person_age'] = None
        logging.info("Invalid values in person_age replaced with None.")
        
        # Transforming categorical data
        encoder = OneHotEncoder()
        
        categorical_columns = ['person_home_ownership', 'loan_intent', 'loan_grade', 'cb_person_default_on_file']
        encoded_data = encoder.fit_transform(base_credit[categorical_columns])
        
        encoded_df = pd.DataFrame(encoded_data.toarray(), columns=encoder.get_feature_names_out(categorical_columns))
        
        base_credit_encoded = pd.concat([base_credit.drop(columns=categorical_columns), encoded_df], axis=1)
        
        logging.info("Categorical data successfully transformed.")
        logging.info(f"DataFrame:\n {base_credit_encoded.head(15)}")

        # Handling missing values
        imputer = KNNImputer(n_neighbors=5)
        base_credit_encoded = pd.DataFrame(imputer.fit_transform(base_credit_encoded), columns=base_credit_encoded.columns)
        logging.info("Missing values imputed successfully.")
        
        # Creating trusted dataset
        trusted_base_credit = base_credit.copy()
        trusted_base_credit['person_age'] = base_credit_encoded['person_age']
        trusted_base_credit['person_emp_length'] = base_credit_encoded['person_emp_length']
        trusted_base_credit['loan_int_rate'] = base_credit_encoded['loan_int_rate']
        
        trusted_dir = f'{global_settings.TRUSTED_PARTITION}/{date_dir}'
        ensure_dir(trusted_dir)
        filename = f"{get_timestamp()}.csv"
        
        trusted_base_credit.to_csv(f'{trusted_dir}/{filename}', index=False)
        logging.info(f"DataFrame:\n {trusted_base_credit.head(15)}")

        logging.info("Trusted dataset saved successfully.")
        
        # Normalizing numerical data
        scaler = StandardScaler()
        numerical_cols = ['person_age', 'person_income', 'loan_amnt', 'loan_int_rate', 'loan_percent_income', 'person_emp_length']
        base_credit_encoded[numerical_cols] = scaler.fit_transform(base_credit_encoded[numerical_cols])
        
        # Saving the scaler for later inference
        artifact_dir = f'{global_settings.ML_ARTIFACTS_DIRECTORY}/utils'
        ensure_dir(artifact_dir)
        
        joblib.dump(scaler, f'{artifact_dir}/scaler.pkl')
        
        logging.info("Numerical data normalized and scaler saved for inference.")
        logging.info(f"DataFrame:\n {base_credit_encoded.head(15)}")
        
        # Feature selection
        features_cols = ['loan_grade_A', 'loan_grade_B', 'loan_grade_C', 'loan_grade_D', 'loan_grade_E', 'loan_grade_F', 'loan_grade_G',
                         'loan_amnt', 'loan_int_rate', 'loan_percent_income', 'cb_person_default_on_file_Y',
                         'loan_intent_EDUCATION', 'loan_intent_HOMEIMPROVEMENT', 'loan_intent_MEDICAL',
                         'loan_intent_PERSONAL', 'loan_intent_VENTURE', 'person_emp_length']
        features = base_credit_encoded[features_cols]
        target = base_credit_encoded['loan_status']
        
        features_dir = f'{global_settings.FEATURE_PARTITION}/{date_dir}'
        target_dir = f'{global_settings.FEATURE_PARTITION}/{date_dir}'
        
        ensure_dir(features_dir)
        ensure_dir(target_dir)
        
        features.to_csv(f'{features_dir}/feature-{filename}', index=False)
        target.to_csv(f'{target_dir}/target-{filename}', index=False)
        
        logging.info("Features and target saved successfully.")
        logging.info(f"DataFrame Features:\n {features.head(15)}")
        logging.info(f'DataFrame Target:\n{target.head(15)}')
        
        logging.info("ETL process completed successfully.")
    except Exception as e:
        logging.error(f"Error in ETL process: {e}")
