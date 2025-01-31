import streamlit as st

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
                
                # payload
                payload = {
                    "name" : name,
                    "birthdate" : birthdate,
                    "loan_intent" : loan_intent,
                    "housing_status" : housing_status,
                    "has_dependents" : has_dependents,
                    "n_dependents" : n_dependents if has_dependents == "Yes" else 0,
                    "int_rate" : int_rate,
                    "employement_hist" : employement_hist,
                    "profession" : profession,
                    "loan_grade" : loan_grade,
                    "marital_status" : marital_status,
                    "yearly_income" : marital_status,
                    "loan_amount" : loan_amount,
                    "education" : education,
                    "has_default_history" : has_default_history,
                    "defaults" : defaults if has_default_history == "Yes" else 0,
                }
                
                st.success("Application submitted successfully!")
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