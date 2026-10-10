def daily_expense_tracker():
    daily_expenses = []
    while True:
        expense = input("Enter your daily expense (or type 'done' to finish): ")
        if expense.lower() == 'done':
            break
        try:
            expense_amount = float(expense)
            daily_expenses.append(expense_amount)
        except ValueError:
            print("Please enter a valid number.")
    
    total_expense = sum(daily_expenses)
    print(f"Total daily expenses: ${total_expense:.2f}")

'''idk if it works or not'''