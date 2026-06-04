# Personal Expense Tracker 

expenses = []
budget = 0

# Set Budget
def set_budget():
    global budget
    budget = float(input("Enter your budget: "))
    print("Budget set successfully!\n")

# Add Expense with Date
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/Shopping/etc): ")
    date = input("Enter date (DD/MM/YYYY): ")
    
    expenses.append({"amount": amount, "category": category, "date": date})
    print("Expense added successfully!\n")
    
    check_budget()

# View Expenses
def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.\n")
        return
    
    print("\nAll Expenses:")
    i = 1
    for expense in expenses:
        print(str(i) + ". Rs." + str(expense["amount"]) + " - " + expense["category"] + " - " + expense["date"])
        i = i + 1
    print()

# Total Expense
def total_expense():
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    print("\nTotal Expense: Rs." + str(total) + "\n")

# Check Budget Limit
def check_budget():
    if budget == 0:
        return
    
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    
    if total > budget:
        print("Warning! You have exceeded your budget!\n")

# Search Expense by Category
def search_expense():
    search = input("Enter category to search: ")
    found = False
    
    print("\nSearch Results:")
    for expense in expenses:
        if expense["category"].lower() == search.lower():
            print("Rs." + str(expense["amount"]) + " - " + expense["category"] + " - " + expense["date"])
            found = True
    
    if not found:
        print("No matching expenses found.")
    print()

# Menu
while True:
    print("==== Expense Tracker ====")
    print("1. Set Budget")
    print("2. Add Expense")
    print("3. View Expenses")
    print("4. Total Expense")
    print("5. Search Expense")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        set_budget()
    elif choice == '2':
        add_expense()
    elif choice == '3':
        view_expenses()
    elif choice == '4':
        total_expense()
    elif choice == '5':
        search_expense()
    elif choice == '6':
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Try again.\n")