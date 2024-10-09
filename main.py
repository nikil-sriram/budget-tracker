import sys
import json
filename = "./data/expenses.json"

print("Welcome to the budget app.")
initial_budget = int(input("Please enter your initial budget."))

expense_amounts = []

while True:
    print("What would you like to do? \n 1. Add an expense \n 2. Show budget details. \n 3. Exit")
    decision = int(input("Enter your choice (1/2/3): "))

    def view_data():
        with open(filename, "r") as f:
            temp = json.load(f)
            for entry in temp:
                expense_description = entry["expense_description"]
                expense_amount = entry["expense_amount"]
                print(f"{expense_description}: {expense_amount}")

    def add_data():
        item_data = {}
        with open (filename, "r") as f:
            temp = json.load(f)
        item_data["expense_description"] = input("Enter expense description.")
        item_data["expense_amount"] = input("Enter expense amount.")
        expense_amounts.append(int(item_data["expense_amount"]))
        print(f"Added expense: {item_data["expense_description"]}, Amount: {item_data["expense_amount"]}")
        temp.append(item_data)
        with open (filename, "w") as f:
            json.dump(temp, f, indent=4)
        
    if decision == 1:
       add_data()
    if decision == 2:
        view_data()
        print(f"Total Spent: {sum(expense_amounts)}")
        remaining_budget = initial_budget-sum(expense_amounts)
        print(f"Remaining Budget: {remaining_budget}")
    if decision == 3:
        def clear_json_file(filename):
            with open(filename, 'w') as f:
                json.dump([], f)
        clear_json_file(filename)
        break