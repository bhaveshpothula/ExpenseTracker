import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense():
    category = input("Category (food, travel, bills, etc): ").strip().capitalize()
    amount = float(input("Amount: $"))
    description = input("Description: ").strip()
    date = input("Date (YYYY-MM-DD, blank for today): ").strip() or datetime.today().strftime("%Y-%m-%d")

    expense = {
        "category": category,
        "amount": amount,
        "description": description,
        "date": date
    }
    expenses = load_data()
    expenses.append(expense)
    save_data(expenses)
    print(f"✅ Added expense: {amount:.2f} for {category} on {date}")

def view_expenses():
    expenses = load_data()
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n📋 All Expenses:")
    print("-" * 50)
    for e in expenses:
        print(f"{e['date']} | {e['category']:<10} | ${e['amount']:>7.2f} | {e['description']}")
    print("-" * 50)

def summary():
    expenses = load_data()
    if not expenses:
        print("No expenses to summarize.")
        return

    total = sum(e['amount'] for e in expenses)
    by_category = {}
    for e in expenses:
        by_category[e['category']] = by_category.get(e['category'], 0) + e['amount']

    print("\n💰 Summary:")
    print(f"Total Spent: ${total:.2f}")
    print("By Category:")
    for cat, amt in by_category.items():
        print(f"  {cat:<10}: ${amt:.2f}")

def monthly_report():
    expenses = load_data()
    if not expenses:
        print("No data available.")
        return

    month = input("Enter month (YYYY-MM): ").strip()
    filtered = [e for e in expenses if e["date"].startswith(month)]

    if not filtered:
        print(f"No expenses found for {month}.")
        return

    total = sum(e["amount"] for e in filtered)
    print(f"\n📆 Report for {month}:")
    print("-" * 50)
    for e in filtered:
        print(f"{e['date']} | {e['category']:<10} | ${e['amount']:>7.2f} | {e['description']}")
    print("-" * 50)
    print(f"Total: ${total:.2f}")

def delete_expense():
    expenses = load_data()
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses()
    idx = int(input("Enter index (starting from 1) to delete: ")) - 1
    if 0 <= idx < len(expenses):
        removed = expenses.pop(idx)
        save_data(expenses)
        print(f"🗑️ Deleted {removed['category']} - ${removed['amount']:.2f} on {removed['date']}")
    else:
        print("Invalid index.")

def main():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summary")
        print("4. Monthly Report")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary()
        elif choice == "4":
            monthly_report()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
