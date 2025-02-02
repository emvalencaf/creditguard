import datetime
import streamlit as st
import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

BACKEND_URL= getenv("BACKEND_URL",
                    "http://localhost:8000/api/v1/loan_default")

def main():
    st.title("CreditGuard - Loan Application Form")
    
    with st.form("loan_form"):
        name = st.text_input("Applicant Name")
        birthdate = st.date_input("Date of Birth")
        
        loan_intent = st.selectbox(
            "Reason for Loan",
            ["Personal", "Education", "Medical", "Venture", "Home Improvement",
            "Debt Consolidation"]
        )

        has_dependents = st.selectbox(
            "Has Dependents",
            ["Yes", "No"]
        )
        
        n_dependents = st.number_input("Number of Depedents",
                                       min_value=0, step=1)
        
        housing_status = st.selectbox(
            "Housing Status",
            ["Own", "Rent", "Mortgage", "Other"]
        )
        
        int_rate = st.number_input("Interest Rate (%)",
                                   min_value=0.0, step=0.1, max_value=100.0)

        employement_hist = st.number_input("Years Employed",
                                           min_value=0, step=1)
        profession = st.text_input("Profession")
        
        loan_amount = st.number_input("Loan Amount ($)",
                                        min_value=0.0, step=1000.0)
        
        loan_grade = st.selectbox(
            "Loan Grade",
            ["A", "B", "C", "D", "E", "F", "G"]
        )
        
        marital_status = st.selectbox(
            "Marital Status",
            ["Single", "Married", "Separated"]
        )
        
        yearly_income = st.number_input("Annual Income ($)",
                                        min_value=0.0, step=1000.0)
        
        education = st.selectbox(
            "Education Level",
            ["High School", "Associate's Degree", "Bachelor's Degree", 
             "Master's Degree", "Doctorate"]
        )
        
        has_default_history = st.selectbox(
            "Default History",
            ["Yes", "No"]
        )
        
        defaults = st.number_input("Defaults",
                                   min_value=0, step=1)
        
        submitted = st.form_submit_button("Submit Application")
        
        if submitted:
            errors = []
            if has_dependents == "Yes" and n_dependents <= 0:
                errors.append("If applicant has dependents, number of dependents must be at least 1.")
            today = datetime.date.today()

            if birthdate >= today:
                errors.append("Date of Birth must be in the past (not today or a future date).")
            if int_rate <= 0:
                errors.append("Interest Rate must be greater than 0.")
            if yearly_income <= 0:
                errors.append("Annual Income must be greater than 0.")
            if loan_amount <= 0:
                errors.append("Loan Amount must be greater than 0.")
            if has_default_history == "Yes" and defaults <= 0:
                errors.append("If applicant has default history, defaults must be at least 1.")

            if errors:
                for error in errors:
                    st.error(error)
            else:
                birthdate_str = birthdate.strftime("%Y-%m-%d")                
                # payload
                payload = {
                    "applicant_name": name,
                    "applicant_birthdate": birthdate_str,
                    "applicant_loan_intent": loan_intent,
                    "applicant_housing_status": housing_status,
                    "applicant_profession": profession,
                    "applicant_has_dependents": has_dependents,
                    "applicant_n_dependents": n_dependents if has_dependents == "Yes" else 0,
                    "applicant_marital_status": marital_status,
                    "applicant_employement_hist": employement_hist,
                    "applicant_yearly_income": yearly_income,  # Certifique-se de passar um número válido
                    "applicant_education": education,
                    "applicant_has_default_history": has_default_history,
                    "applicant_defaults": defaults if has_default_history == "Yes" else 0,
                    "loan_int_rate": int_rate,
                    "loan_amount": loan_amount,
                    "loan_grade": loan_grade
                }
                
                st.success("Application submitted successfully!")
                try:
                    response = requests.post(BACKEND_URL, json=payload)
                    response.raise_for_status()  # Levanta um erro se a resposta não for 200
                    result = response.json()  # Exemplo de resposta {"result": true} ou {"result": false}
                    print("result: ", result)
                    if result.get("prediction", False):
                        st.warning("This applicant is likely to default on the loan.")
                    else:
                        st.success("This applicant is unlikely to default on the loan.")
                    
                except requests.exceptions.RequestException as e:
                    st.error(f"Error contacting the backend: {e}")
                
                # Exibe resumo da aplicação
                st.write("### Application Summary")
                st.write(f"**Payload**: {payload}")
                st.write(f"**Name:** {name}")
                st.write(f"**Date of Birth:** {birthdate}")
                st.write(f"**Reason for Loan:** {loan_intent}")
                st.write(f"**Housing Status:** {housing_status}")
                st.write(f"**Interest Rate:** {int_rate}%")
                st.write(f"**Years Employed:** {employement_hist}")
                st.write(f"**Profession:** {profession}")
                st.write(f"**Loan Grade:** {loan_grade}")
                st.write(f"**Marital Status:** {marital_status}")
                st.write(f"**Annual Income:** ${yearly_income}")
                st.write(f"**Loan Amount**: ${loan_amount}")
                st.write(f"**Education Level:** {education}")
                st.write(f"**Has Default History**: {has_default_history}")
                st.write(f"**How Many Defaults**: {defaults}")

if __name__ == "__main__":
    main()