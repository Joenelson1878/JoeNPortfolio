import json
import os
from datetime import datetime
import pandas as pd

JSON_FILE = "transactions.json"

def load_transactions():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []
    return pd.DataFrame(data)

def save_transaction(transaction):
    # Load existing
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(transaction)

    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_transaction():
    print("\n--- Add Transaction ---")
    date = input("Date (YYYY-MM-DD): ")
    description = input("Description: ")
    category = input("Category: ")
    amount = float(input("Amount (use negative for expense): "))
    t_type = "Income" if amount > 0 else "Expense"
    account = input("Account (Main/Savings/etc): ")

    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format.")
        return

    transaction = {
        "date": date_obj.strftime("%Y-%m-%d"),
        "description": description,
        "category": category,
        "amount": amount,
        "type": t_type,
        "account": account
    }

    save_transaction(transaction)
    print("Transaction saved.")
