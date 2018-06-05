from flask import Flask, flash, session, request, redirect, render_template, url_for
from db.data_layer import get_all_bills, get_bill, create_bill, delete_bill, update_bill

app = Flask(__name__)

@app.route('/')
def index():
    bills = get_all_bills()
    return render_template('index.html', all_bills = bills)

@app.route('/add_bill', methods=['POST'])
def add_bill():
    description = request.form['description']
    amount = request.form['amount']
    create_bill(amount, description)
    return redirect(url_for('index'))

@app.route('/delete_bill/<bill_id>')
def delete(bill_id):
    delete_bill(bill_id)
    return redirect(url_for('index'))

app.run(debug=True)