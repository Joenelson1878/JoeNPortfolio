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
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []
    
    data.append(transaction)

    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=4)