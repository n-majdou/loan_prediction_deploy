from flask import Flask, request, jsonify, render_template
#import util
import server.util as util

app = Flask(__name__, static_url_path='/client', static_folder='../client', template_folder='../client')

@app.route('/')
def index():
    if request.method == "GET":
        return render_template("app.html")

@app.route('/get_loan_terms')
def get_loan_terms():
    response = jsonify({
        'loan_terms': util.get_loan_terms()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_loan', methods=['POST'])
def predict_loan():
    applicant_income = float(request.form['applicant_income'])
    coapplicant_income = float(request.form['coapplicant_income'])
    loan_amount = float(request.form['loan_amount'])
    loan_amount_term = float(request.form['loan_amount_term'])
    credit_history = int(request.form['credit_history']) -1
    #print(applicant_income,coapplicant_income,loan_amount,loan_amount_term,credit_history)

    response = jsonify({
        'loan_or_no_loan' : util.get_loan_prediction(applicant_income,coapplicant_income,loan_amount,loan_amount_term,credit_history)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Flask Server for loan predictions....")
    app.run(debug=True)