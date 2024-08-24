expenses = {}

def add():
    category = input("Category: ").casefold()
    amount = float(input("Amount: "))
    if category in expenses:
        expenses[category].append(amount)
    else:
        expenses[category] = [amount]

def view():
    for category, amounts in expenses.items():
        print(category, ":", sum(amounts))

def sum_expenses():
    total = sum(amount for category in expenses.values() for amount in category)
    print("Total expenses:", total)

print("[Basic Expense Tracker]")
print()

while True:
    print("Select an option:")
    print()
    print("Add Expense: (Type 1)")
    print("View Expenses: (Type 2)")
    print("Sum of Expenses: (Type 3)")
    print("Exit: (Type 4)")
    x = int(input("Enter your choice: "))
    if x == 1:
        add()
    elif x == 2:
        view()
    elif x == 3:
        sum_expenses()
    elif x == 4:
        break
    else:
        print("Invalid choice. Please try again.")
