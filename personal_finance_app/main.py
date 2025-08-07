from transaction_handler import add_transaction, load_transactions
from visualiser import plot_balance_over_time, plot_spending_by_category

def main():
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Transaction")
        print("2. Show Balance Over Time")
        print("3. Show Spending by Category")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            df = load_transactions()
            plot_balance_over_time(df)
        elif choice == '3':
            df = load_transactions()
            plot_spending_by_category(df)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()