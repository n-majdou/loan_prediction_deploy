import pickle
import numpy as np
import os
import json

# init global variables
__model = None
__scaler = None
__loan_terms = None

def get_loan_prediction(applicant_income,coapplicant_income,loan_amount,loan_amount_term,credit_history):
    combined_income = np.log(applicant_income + coapplicant_income +1)
    applicant_income = np.log(applicant_income +1)
    coapplicant_income = np.log(coapplicant_income + 1)
    loan_unit_per_income = loan_amount*100/ (applicant_income+coapplicant_income)
    loan_per_term = loan_amount/loan_amount_term

    x = __scaler.transform(np.array([applicant_income,coapplicant_income,loan_amount,loan_amount_term,combined_income,loan_unit_per_income,
                  loan_per_term]).reshape(1, -1))
    prediction = __model.predict(np.append(x, [credit_history]).reshape(1, -1))[0]
    if prediction == 1:
        return  "Loan application accepted"
    else:
        return "Loan application rejected"

def get_loan_terms():
    return __loan_terms

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __model
    global __scaler
    global __loan_terms

    with open(os.getcwd()+"/server/artifacts/loan_terms.json", 'r') as f:
        __loan_terms = json.load(f)['loan_amount_term'] # interpreted as dictionary
    with open(os.getcwd()+'/server/artifacts/loan_prediction_model2.pickle', 'rb') as f:
        __model = pickle.load(f)
    with open(os.getcwd() + '/server/artifacts/loan_prediction_scaler.pickle', 'rb') as f:
        __scaler = pickle.load(f)

    print('loading saved artifacts...done')

load_saved_artifacts()
#print(get_loan_prediction(5821, 0.0, 144, 360, 1))
#print(get_loan_prediction(5821, 0.0, 144, 360, 0))
#print(__loan_terms)




