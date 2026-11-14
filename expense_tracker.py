
import csv
from datetime import datetime

# Load previously saved expenses
expenses = []

try:
    with open("expenses.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            expenses.append(row)

except FileNotFoundError:
    print("No previous expense records found. Starting fresh.")

# Main menu
while True:
    print("\n===== INSTITUTE EXPENSE TRACKER =====")
    print("1. Add New Expense")
    print("2. Show All Expenses")
    print("3. Calculate Total Expenses by Category")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add New Expense
    if choice == "1":

        # Validate expense date
        while True:
            date = input("Enter expense date (DD-MM-YYYY): ")

            try:
                datetime.strptime(date, "%d-%m-%Y")
                break
            except ValueError:
                print("Invalid date! Please enter date in DD-MM-YYYY format.")

        item = input("Enter item name: ")
        category = input("Enter category: ")

        # Validate expense amount
        while True:
            try:
                amount = float(input("Enter amount: "))
                break
            except ValueError:
                print("Invalid amount! Please enter a valid number.")

        expense = {
            "date": date,
            "item": item,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        # Save expenses to CSV file
        with open("expenses.csv", "w", newline="") as file:
            fieldnames = ["date", "item", "category", "amount"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(expenses)

        print("Expense added and saved successfully!")

    # Show All Expenses
    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("\n----- ALL EXPENSES -----")

            for expense in expenses:
                print(
                    expense["date"],
                    expense["item"],
                    expense["category"],
                    expense["amount"]
                )

    # Calculate Total Expenses by Category
    elif choice == "3":
        if not expenses:
            print("No expenses available.")
        else:
            categories = set(
                expense["category"] for expense in expenses
            )

            print("\n----- EXPENSES BY CATEGORY -----")

            for category in categories:
                total = 0

                for expense in expenses:
                    if expense["category"] == category:
                        total += float(expense["amount"])

                print(category, ":", total)

    # Exit
    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please select 1 to 4.")
