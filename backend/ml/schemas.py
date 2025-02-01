from typing import Literal
from pydantic import BaseModel, Field, field_validator

from pydantic import BaseModel, Field

class LoanApplicationSchema(BaseModel):
    """
    Schema for loan application data validation.

    This schema defines the required fields for a loan application, ensuring
    correct data types and basic constraints.
    """
    applicant_name: str = Field(..., description="Full name of the loan applicant.")
    applicant_birthdate: str = Field(..., description="Applicant's date of birth (YYYY-MM-DD).")
    applicant_loan_intent: Literal["Personal", "Education", "Medical", "Venture", "Home Improvement", "Debt Consolidation"] = Field(..., description="Reason for the loan.")
    applicant_housing_status: Literal["Own", "Rent", "Mortgage", "Other"] = Field(..., description="Housing status.")
    applicant_profession: str = Field(..., description="Applicant's current profession.")
    applicant_has_dependents: Literal["Yes", "No"] = Field(..., description="Indicates if the applicant has dependents.")
    applicant_n_dependents: int = Field(..., ge=0, description="Number of dependents (must be 0 or greater).")
    applicant_marital_status: Literal["Single", "Married", "Separated"] = Field(..., description="Marital status.")
    applicant_employement_hist: int = Field(..., ge=0, description="Number of years the applicant is in his current job")
    applicant_yearly_income: float = Field(..., gt=0, description="Applicant's annual income (must be greater than 0).")
    applicant_education: Literal["High School", "Associate's Degree", "Bachelor's Degree", "Master's Degree", "Doctorate"] = Field(..., description="Highest level of education achieved.")
    applicant_has_default_history: Literal["Yes", "No"] = Field(..., description="Indicates if the applicant has a default history.")
    applicant_defaults: int = Field(..., ge=0, description="Number of defaults (must be 0 or greater).")
    loan_int_rate: float = Field(..., gt=0, le=100, description="Interest rate for the loan (must be between 0 and 100).")
    loan_amount: float = Field(..., gt=0, description="Requested loan amount (must be greater than 0).")
    loan_grade: Literal["A",'B',"C","D","E","F","G"] = Field(...,description="Loan grade")
    

    @field_validator('applicant_birthdate')
    @classmethod
    def validate_birthdate(cls, value):
        import datetime
        try:
            birthdate = datetime.datetime.strptime(value, "%Y-%m-%d").date()
            if birthdate >= datetime.date.today():
                raise ValueError("Birthdate must be in the past.")
        except ValueError:
            raise ValueError("Invalid birthdate format. Use YYYY-MM-DD.")
        return value
    
class LoanApplicationFeaturesSchema(LoanApplicationSchema):
    loan_percent_income: float = Field(..., description="Loan percentage relative to applicant yearly income.")