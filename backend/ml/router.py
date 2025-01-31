from fastapi import APIRouter

from ml.schemas import LoanApplicationSchema

router = APIRouter(tags=['machine learning',
                         'artificial intelligence',
                         'ml', 'ai'])

@router.post('/loan_default')
async def predict_default(loan_application: LoanApplicationSchema):
    """
    Predict if loan application will result in a default
    """
    print(loan_application)
    
    
    
    return loan_application