request_spending ={
    "Mahek" : {
        "balance" : 3000.00,
        "transactions" : [
            {"amount": -9000.00, "category" : "Creatives"},
            {"amount": 7000.00, "category" : "Sponsor"},
            {"amount": -2000.00, "category" : "Prize-Money"}
        ]   
    },
    "Arham" : {
        "balance" : 5000.00,
        "transactions" : [
            {"amount": 8000.00, "category" : "Stalls"},
            {"amount": 7500.00, "category" : "Seminars"}
        ]
    },
    "Unnati" : {
        "balance" : 3500.00,
        "transactions" : [
            {"amount": -5000.00, "category" : "Attraction"},
            {"amount": 2500.00, "category" : "Promo"},
            {"amount": -900.00, "category" : "Lighting"},
            {"amount": -3000.00, "category" : "Games"}
        ]
    },
    "Gaurang" : {
        "balance" : 2000.00,
        "transactions" : [
            {"amount": -1500.00, "category" : "Website"},
            {"amount": -1000.00, "category" : "C2C"},
            {"amount": -500.00, "category" : "Posters"}
        ]
    }
}

def total_spending(request_spending,account_id: str,category: str):
    amt_spent = 0
    for transaction in request_spending[account_id]['transactions']:
        if transaction['category']== category and transaction['amount']<0:
            amt_spent += abs(transaction['amount'])
    print(f'{account_id} spent {amt_spent}')
        
def account_balance(request_spending, account_id: str):
    end_balance = request_spending[account_id]['balance']
    for transaction in request_spending[account_id]['transactions']:
        end_balance = end_balance + transaction['amount']
    return end_balance

def money_owed(request_spending, account_id: str):
    balance= account_balance(request_spending, account_id)
    if balance < 0:
        print(f'{account_id} owes {balance}')
    else:
        print(f'{account_id} owes nothing')    


total_spending(request_spending, "Mahek", "Creatives")

print(f'{account_balance(request_spending, "Gaurang")} was spent by the account holder')

money_owed(request_spending, "Unnati")