from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:dhaka1971@localhost/expenditure_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
db = SQLAlchemy(app)
print("Database connection initialized successfully!")
DB_NAME='expendituredb'
DB_USER='username'
DB_PASSWORD='cowboy'
DB_HOST='localhost'
DB_PORT='5432'
try:
    conn=psycopg2.connect(
        dbname= DB_NAME,
        user= DB_USER,
        password= DB_PASSWORD,
        host= DB_HOST,
        port= DB_PORT
    )
    print ('connected to posgresql succesfully')
    cursor=conn.cursor()
    cursor.execute('select version();')
    db_version = cursor.fetchone()
    print ('database version:', db_version)
    cursor.close()
    conn.close()
except Exception as e :
    print("Error connecting to posgresql:", e)

class Transaction(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    type=db.Column(db.String(10),nullable= False)
    category=db.Column(db.String(50),nullable=False)
    amount=db.Column(db.Float,nullable=False)
    date=db.Column(db.String(10),nullable=False)
    customer_id=db.Column(db.Integer,db.ForeignKey('customer.id'),nullable=True)
class Customer(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True,nullable=False)
    Transaction= db.relationship('Transaction',backref='customer',lazy=True)
def initialize_database():
    with app.app_context():
        db.create_all()
    
def calculate_totals():
    total_income=db.session.query(db.func.sum(Transaction.amount)).filter(Transaction.type=='income').scalar() or 0
    total_expense=db.session.query(db.func.sum(Transaction.amount)).filter(Transaction.type=='expense').scalar() or 0
    balance=total_income-total_expense
    return total_income,total_expense,balance
    
@app.before_first_request
def create_tables():
    db.create_all()
def add_transactions(transaction_type,amount,date,category,customer_name=''):
    customer=None
    if transaction_type.lower() == 'income' and customer_name :
        customer= Customer.query.filter_by(name=customer_name).first()
        if not customer:
            customer=Customer(name=customer_name)
            db.session.add(customer)
            db.session.commit()
    new_transaction=Transaction(type=transaction_type,category=category,amount=amount,date=date,customer=customer)
    db.session.add(new_transaction)
    db.session.commit()
def get_totals():
    total_income=db.session.query(db.func.sum(Transaction.amount)).filter_by(type='income').scalar() or 0
    total_expense=db.session.query(db.func.sum(Transaction.amount)).filter_by(type='expense').scalar() or 0 
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


