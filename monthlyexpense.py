import csv
import os
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
    print('transaction added successfully!\n')
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
    
def main():
    initilaize_file()
    while True:
        print('\nMonthly expenditure tracker')
        print('1.Add income')
        print('2.Add expense')
        print('3.view summary')
        print('4.Exit')
        choice=input('enter the choice')
        if choice=='1':
            category=input('enter income source:')
            amount=float(input('enter amount'))
            date=input('enter date (YYY-MM-DD):')
            add_transaction('income',category,amount,date)
        elif choice =='2':
            category= input('enter the expense catagory')
            amount= float(input('enter amount'))
            date=input('enter date(YYY-MM-DD)')
            add_transaction('Expense',category,amount,date)
        elif choice=='3':
            total_income, total_expense, balance = calculate_totals()
            print(f'total income: ${total_income:.2f}')
            print(f'total expense: ${total_expense:.2f}')
            print(f'total balance:${balance:.2f}')
        elif choice=='4':
            print('Exiting the program')
            break
        else :
            print('Invalid choice.Please Try again')
if __name__ == '__main__':
    main()