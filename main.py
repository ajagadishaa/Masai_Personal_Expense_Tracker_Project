import os
from datetime import datetime

FILENAME = "expenses_data1.txt"

def add_expense():
    category = input("Enter category (e.g., Food, Travel, Bus): ").strip()
    try:
        amount = float(input("Enter the amount: ").strip())
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return

    date = input("Enter date (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    with open(FILENAME, "a") as file:
        file.write(f"{category},{amount},{date}\n")
    print("Expense added successfully!")

def view_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses recorded.")
        return

    expenses = {}
    with open(FILENAME, "r") as file:
        for line in file:
            category, amount, date = line.strip().split(",")
            if category not in expenses:
                expenses[category] = []
            expenses[category].append((float(amount), date))

    if not expenses:
        print("No expenses recorded.")
        return

    print("Expenses:")
    for category, entries in expenses.items():
        print(f"{category}:")
        if entries:
            for i, (amount, date) in enumerate(entries, 1):
                print(f"  {i}. Amount: {amount} - Date: {date}")
        else:
            print(" No expenses recorded.")

def monthly_summary():
    if not os.path.exists(FILENAME):
        print("No expenses recorded.")
        return

    year_month = input("Enter month and year (YYYY-MM): ").strip()
    try:
        datetime.strptime(year_month, '%Y-%m')
    except ValueError:
        print("Invalid date format. Please use YYYY-MM.")
        return

    total_expenses = 0
    category_totals = {}

    with open(FILENAME, "r") as file:
        for line in file:
            category, amount, date = line.strip().split(",")
            if date.startswith(year_month):
                total_expenses += float(amount)
                category_totals[category] = category_totals.get(category, 0) + float(amount)

    print(f"Monthly Summary ({year_month}):")
    print(f"Total Expenses: {total_expenses}")
    print("By Category:")
    for category, total in category_totals.items():
        print(f"  {category}: {total}")

def search_expenses():
    keyword = input("Enter a keyword to search (e.g., category or date): ").strip()
    if not os.path.exists(FILENAME):
        print("No expenses recorded.")
        return

    found = False
    with open(FILENAME, "r") as file:
        for line in file:
            if keyword.lower() in line.lower():
                print(line.strip())
                found = True

    if not found:
        print("No matching records found.")

def delete_expense():
    date_to_delete = input("Enter the date of the expense to delete (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(date_to_delete, '%Y-%m-%d')
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    if not os.path.exists(FILENAME):
        print("No expenses recorded.")
        return

    with open(FILENAME, "r") as file:
        lines = file.readlines()

    matching_lines = [line for line in lines if line.strip().endswith(date_to_delete)]

    if not matching_lines:
        print(f"No expenses found for the date {date_to_delete}.")
        return

    print("Matching expenses:")
    for i, line in enumerate(matching_lines, 1):
        print(f"{i}. {line.strip()}")

    try:
        line_number = int(input("Enter the line number of the expense to delete: ").strip())
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if line_number < 1 or line_number > len(matching_lines):
        print("Invalid line number.")
        return

    selected_line = matching_lines[line_number - 1]
    lines.remove(selected_line)

    with open(FILENAME, "w") as file:
        file.writelines(lines)

    print("Expense deleted successfully!")

def main():
    while True:
        print("""
        Welcome to Personal Expense Tracker!
        1. Add Expense
        2. View Expenses
        3. Monthly Summary
        4. Search Expenses
        5. Delete Expense
        6. Exit
        """)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            search_expenses()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            print("ThankYou!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
