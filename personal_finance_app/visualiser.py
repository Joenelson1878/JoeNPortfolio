import matplotlib.pyplot as plt
import pandas as pd

def plot_balance_over_time(df):
    if df.empty:
        print("No transactions to display")
        return
    
    df = df.sort_values("date")
    df["date"] = pd.to_datetime(df["date"])
    df["balance"] = df["amount"].cumsum()

    plt.figure(figsize=(10,5))
    plt.plot(df["date"])
    plt.title("Account Balance over time")
    plt.xlabel("Date")
    plt.ylabel("Balance (£))")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
def plot_spending_by_category(df):
    if df.empty:
        print("No transactions to display")
        return
    expenses = df[df["ammount"] < 0]
    category_totals = expenses.groupby("category")["amount"].sum().abs()
        
    if category_totals.empty:
        print("No expenses are available")
        return
        
    category_totals.plot(kind="bar", figsize=(8,40))
    plt.title("spending by category")
    plt.xlabel("category")
    plt.ylabel("Amount spent (£)")
    plt.tight_layout()
    plt.show()