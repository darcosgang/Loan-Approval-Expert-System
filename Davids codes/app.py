from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
# Store user data temporarily
user_data = {}
@app.route('/')
def collection_of_information():
    return render_template('collection_of_information.html')
@app.route('/financial_records', methods=['POST'])
def financial_records():
    # Receive data from the first form
    user_data['first_name'] = request.form.get('first_name')
    user_data['last_name'] = request.form.get('last_name')
    user_data['age_range'] = request.form.get('age_range')
    user_data['address'] = request.form.get('address')
    user_data['state'] = request.form.get('state')
    user_data['next_of_kin'] = request.form.get('next_of_kin')
    user_data['occupation'] = request.form.get('occupation')
    
    return render_template('financial_records.html')
@app.route('/loan_application', methods=['POST'])
def loan_application():
    # Receive data from the financial records form
    user_data['working'] = request.form.get('working')
    user_data['salary'] = request.form.get('salary')
    user_data['other_income'] = request.form.get('other_income')
    user_data['other_income_amount'] = request.form.get('other_income_amount')
    user_data['debt'] = request.form.get('debt')
    user_data['repay_plan'] = request.form.get('repay_plan')
    user_data['credit_history'] = request.form.get('credit_history')
    user_data['credit_score'] = request.form.get('credit_score')
    user_data['agreement'] = request.form.get('agreement')
    user_data['loan_amount'] = request.form.get('loan_amount')
    
    return render_template('loan_application_form.html')
@app.route('/calculate_loan', methods=['POST'])
def calculate_loan():
    loan_amount = float(request.form.get('loan_amount'))
    loan_duration = int(request.form.get('loan_duration'))
    
    # Calculate interest rate and total amount to pay back
    if loan_duration == 1:
        interest_rate = 0.05
    elif loan_duration == 2:
        interest_rate = 0.10
    else:
        interest_rate = 0.05 * loan_duration  # 5% per month
    
    total_amount = loan_amount + (loan_amount * interest_rate)
    
    return render_template('loan_application_form.html', total_amount=total_amount)
if __name__ == '__main__':
    app.run(debug=True)