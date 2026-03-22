import json
from datetime import datetime

FILE_NAME = "expenses.json"

# Load existing data
def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

# Save data
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Add expense
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (food, travel, etc): ")
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

    if date == "":
        date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

    print("✅ Expense added successfully!")

# View expenses
def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\n📊 All Expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['date']} | {exp['category']} | ₹{exp['amount']}")

# Calculate total
def total_spending():
    expenses = load_expenses()
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Spending: ₹{total}")

# Menu
def menu():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spending()
        elif choice == "4":
            print("👋 Exiting...")
            break
        else:
            print("Invalid choice!")

# Run program
menu()
