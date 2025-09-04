import csv
import datetime
import argparse
import os

def init_file(filename):   # File Management
    try:
        with open(filename, "x", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "category", "amount"])
    except FileExistsError:
        pass

def add_expense(filename, date, category, amount):   # Expense Functions
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount])
    print(f"Added: {date}, {category}, {amount}")

def view_expenses(filename):   # View Expense Functions
    if not os.path.exists(filename):
        print("No records found. Please sign in first.")
        return

    with open(filename, "r") as f:
        reader = list(csv.reader(f))
    if len(reader) <= 1:
        print("No expenses recorded yet.")
        return

    print("\nYour Expenses:")
    for i, row in enumerate(reader[1:], start=1):
        print(f"{i}. Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}")

def delete_expense(filename):   # Delete Expense Functions
    if not os.path.exists(filename):
        print("No records found. Please sign in first.")
        return

    with open(filename, "r") as f:
        reader = list(csv.reader(f))

    if len(reader) <= 1:
        print("No expenses recorded yet.")
        return

    print("\nCurrent Expenses:")
    for i, row in enumerate(reader[1:], start=1):
        print(f"{i}. {row}")

    try:
        index = int(input("\nEnter the row number to delete: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if index < 1 or index >= len(reader):
        print("Invalid index. Use the row number shown above.")
        return

    deleted = reader.pop(index)
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(reader)

    print(f"Deleted: {deleted}")

def update_expense(filename):   #Update Expense Functions
    if not os.path.exists(filename):
        print("No records found. Please sign in first.")
        return

    with open(filename, "r") as f:
        reader = list(csv.reader(f))

    if len(reader) <= 1:
        print("No expenses recorded yet.")
        return

    print("\nCurrent Expenses:")
    for i, row in enumerate(reader[1:], start=1):
        print(f"{i}. {row}")

    try:
        index = int(input("\nEnter the row number to update: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if index < 1 or index >= len(reader):
        print("Invalid index. Use the row number shown above.")
        return

    old = reader[index]      # Old data
    new_date = input(f"Date [{old[0]}]: ") or old[0]
    new_category = input(f"Category [{old[1]}]: ") or old[1]
    new_amount = input(f"Amount [{old[2]}]: ") or old[2]
    reader[index] = [new_date, new_category, new_amount]

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(reader)

    print(f"Updated row {index}: {reader[index]}")

if __name__ == "__main__":   # Main CLI
    parser = argparse.ArgumentParser(description="Personal Expense Tracker (CLI)")
    subparsers = parser.add_subparsers(dest="command")

    signin_parser = subparsers.add_parser("signin", help="Create a new account")
    signin_parser.add_argument("--name", required=True, help="Your name")

    login_parser = subparsers.add_parser("login", help="Login with existing account")
    login_parser.add_argument("--name", required=True, help="Your name")
    login_parser.add_argument("action", choices=["add", "view", "delete", "update"], help="Action to perform")
    login_parser.add_argument("--category", help="Expense category")
    login_parser.add_argument("--amount", type=float, help="Expense amount")
    login_parser.add_argument("--date", default=None, help="Expense date (YYYY-MM-DD). Defaults to today.")

    args = parser.parse_args()

    if args.command == "signin":
        filename = f"{args.name}_expenses.csv"
        if os.path.exists(filename):
            print("Account already exists! Try login.")
        else:
            init_file(filename)
            print(f"Account created for {args.name}! File: {filename}")
            
    elif args.command == "login":
        filename = f"{args.name}_expenses.csv"
        if not os.path.exists(filename):
            print("No account found. Please sign in first.")
        else:
            if args.action == "add":
                if not args.category or not args.amount:
                    print("For 'add' you must provide --category and --amount")
                else:
                    expense_date = args.date or datetime.datetime.now().strftime("%Y-%m-%d")
                    add_expense(filename, expense_date, args.category, args.amount)
            elif args.action == "view":
                view_expenses(filename)
            elif args.action == "delete":
                delete_expense(filename)
            elif args.action == "update":
                update_expense(filename)