CREATE DATABASE creditguard;

CREATE SCHEMA public;

CREATE TYPE marital_status_enum AS ENUM ('Single', 'Married', 'Divorced', 'Windowed');
CREATE TYPE education_enum AS ENUM ('High School', 'Associate Degree', 'Bachelor', 'Master', 'Doctor');
CREATE TYPE work_status_enum AS ENUM ('Unemployed', 'Employed', 'Self-employed', 'Business Owner');
CREATE TYPE housing_status_enum AS ENUM ('Own', 'Rent', 'Mortgage', 'Other');
CREATE TYPE loan_status_enum AS ENUM ('Paid', 'Refused', 'Defaulted', 'Pending', 'Partial Paid');
CREATE TYPE loan_intent_enum AS ENUM ('Personal', 'Education', 'Medical', 'Venture', 'Home Improvement', 'Debt Consolidation');
CREATE TYPE loan_grade_enum AS ENUM ('A', 'B', 'C', 'D', 'E', 'F', 'G');
CREATE TYPE predicted_outcome_enum AS ENUM ('Defaulted', 'Not Defaulted');

CREATE TABLE Applicants (
    applicant_id SERIAL PRIMARY KEY,
    applicant_first_name VARCHAR NOT NULL,
    applicant_last_name VARCHAR NOT NULL,
    applicant_marital_status marital_status_enum DEFAULT 'Single',
    applicant_birthdate DATE NOT NULL,
    applicant_dependents INTEGER NOT NULL,
    applicant_profession VARCHAR NOT NULL,
    applicant_yearly_income DECIMAL(10,2) NOT NULL,
    applicant_education education_enum DEFAULT 'High School',
    applicant_work_status work_status_enum DEFAULT 'Unemployed',
    applicant_work_experiences INTEGER NOT NULL,
    applicant_current_work_status_duration INTEGER NOT NULL,
    applicant_defaults INTEGER,
    applicant_housing_status housing_status_enum DEFAULT 'Own',
    updated_at DATE NULL,
    created_at DATE DEFAULT now()
);

CREATE TABLE Loans (
    loan_id SERIAL PRIMARY KEY,
    loan_ammount DECIMAL(10,2) NOT NULL,
    loan_payment_date DATE NOT NULL,
    loan_date DATE NOT NULL,
    loan_int_rate DECIMAL(10,2),
    loan_status loan_status_enum DEFAULT 'Pending',
    applicant_id INT NOT NULL REFERENCES Applicant(applicant_id) ON DELETE CASCADE,
    updated_at DATE NULL,
    created_at DATE DEFAULT now()
);

CREATE TABLE LoanDetails (
    loan_id INT PRIMARY KEY REFERENCES Loan(loan_id) ON DELETE CASCADE,
    loan_intent loan_intent_enum NOT NULL,
    loan_grade loan_grade_enum NOT NULL
);

CREATE TABLE Models (
    model_id SERIAL PRIMARY KEY,
    model_alg VARCHAR NOT NULL,
    model_scaler_id INT NULL REFERENCES Model(model_id) ON DELETE SET NULL,
    model_features VARCHAR NOT NULL,
    model_hyperparams JSON,
    model_path VARCHAR NOT NULL,
    model_trained_features_dataset_partition VARCHAR NOT NULL,
    model_trained_target_dataset_partition VARCHAR NOT NULL,
    created_at DATE DEFAULT now(),
    updated_at DATE NULL
);

CREATE TABLE LoanPrediction (
    prediction_id SERIAL PRIMARY KEY,
    loan_id INT UNIQUE NOT NULL REFERENCES Loan(loan_id) ON DELETE CASCADE,
    predicted_outcome predicted_outcome_enum NOT NULL,
    model_id INT NOT NULL REFERENCES Model(model_id) ON DELETE CASCADE,
    created_at DATE DEFAULT now(),
    updated_at DATE NULL
);