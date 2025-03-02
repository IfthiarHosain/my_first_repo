from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import os
app=Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URL']='posgresql://username:cowboy@localhost/expenditure_db'
app.config['SQlAlCHEMY_TRACK_MODIFICATION']= False
db=SQLAlchemy(app)
class Transaction(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    type=db.Column(db.String(10),nullable= False)
    category=db.Column(db.String(50),nullable=False)
    amount=db.Column(db.float,nullable=False)
    date=db.Column(db.String(10),nullable=False)
    customer_id=db.Column(db.Integer,db.Foreignkey('customer.id'),nullable=True)
class Customer(db.Model):
    id=db.Column(db.integer,primary_key=True)
    name=db.Column(db.string(100),unique=True,nullable=False)
    Transaction= db.relationship('transaction',backref='customer',lazy=True)
@app.before_frist_request
def create_tables():
    db.create_all
def add_transactions(transaction_type,amount,date,category,customer_name=''):
    customer=None
    if transaction_type.lower() == 'income' and customer_name :
        customer= Customer.query.filter_by(name=customer_name='').frist()
        if not customer:
            customer=Customer(name=customer_name)
            db.session.add(customer)
            db.session.commit()
    new_transaction=Transaction(type=transaction_type,category=category,amount=amount,date=date,customer=customer)
    db.session.add(new_transaction)
    db.session.commit()
def get_totals():
    total_income=db.session.query(db.func.sum(Transaction.amount)).filter_by(type='income')
    total_expense=db.session.query(db.func.sum(Transaction.amount)).filter_by(name='expense')   
    balance= total_income - total_expense
    return total_income,total_expense,balance
@app.route('/')
def index():
    total_income,total_expense,balance= get_totals()
    Transactions= Transaction.query.all()
    customers= Customer.query.all()
    return render_template('index.html',
                           total_income=total_income,
                           total_expense=total_expense,
                           balance=balance,
                           Transactions=Transactions,
                           customers=customers)
@app.route('/add',methods=['post'])
def add():
    transaction_type=request.form['type']
    category=request.form['category']
    amount= float(request.form['amount'])
    date=request.form['date']
    customer_name=request.form['customer'] if transaction_type.lower()=='income' else ''
    add_transactions(transaction_type,category,amount,date,customer_name)
    return redirect(url_for('index'))
if __name__=='__main__':
    app.run(debug=True)


