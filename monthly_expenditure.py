from flask import Flask, render_template, request, redirect, url_for
import csv
import os
app = Flask(__name__)
FILE_NAME = "expenditure_data.csv"
file_name="expenditure_data.csv"
def initilaize_file():
    if not os.path.exists(file_name):
        with open(file_name,mode='w',newline='') as file:
            writer=csv.writer(file)
            writer.writerow(['Type','Catagory','Amount','Date'])
def add_transaction(transaction_type,category,amount,date):
    with open(file_name,mode='a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow([transaction_type,category,amount,date])
   
def calculate_totals():
    total_income =0
    total_expense= 0

    with open(file_name,mode='r') as file:
        reader=csv.reader(file)
        next(reader)
        for row in reader:
            if row:
                transaction_type, _,amount, _=row  
                try:
                  amount=float(amount)
                  if transaction_type.lower()=='income':
                    total_income += amount
                  elif transaction_type.lower()== 'expense':
                    total_expense += amount
                except ValueError:
                    continue
            
    balance=total_income - total_expense
    return total_income,total_expense,balance
    
@app.route('/')
def index():
    total_income, total_expense, balance = calculate_totals()
    return f"""
    <h1>Monthly Expenditure Tracker</h1>
    <p>Total Income: ${total_income:.2f}</p>
    <p>Total Expenses: ${total_expense:.2f}</p>
    <p>Remaining Balance: ${balance:.2f}</p>
    <h3>Add Transaction</h3>
    <form action='/add' method='post'>
        <label>Type:</label>
        <select name='type'>
            <option value='Income'>Income</option>
            <option value='Expense'>Expense</option>
        </select>
        <br>
        <label>Category:</label>
        <input type='text' name='category' required><br>
        <label>Amount:</label>
        <input type='number' name='amount' step='0.01' required><br>
        <label>Date:</label>
        <input type='date' name='date' required><br>
        <button type='submit'>Add Transaction</button>
    </form>
    """

@app.route('/add', methods=['POST'])
def add():
    transaction_type = request.form['type']
    category = request.form['category']
    amount = request.form['amount']
    date = request.form['date']
    add_transaction(transaction_type, category, float(amount), date)
    return redirect(url_for('index'))

if __name__ == "__main__":
    initilaize_file()
    app.run(debug=True)




