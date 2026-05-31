def add_expense():
    expenses = [100, 200, 300]

    new_expense = 150

    if new_expense <= 0:
        return "Invalid expense"

    expenses.append(new_expense)

    return expenses

print(add_expense())