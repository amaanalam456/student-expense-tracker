expenses = []

while True:
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount: $"))
        expenses.append([name, amount])
        print("Expense added!")

    elif choice == "2":
        total = 0

        for expense in expenses:
            print(f"{expense[0]}: ${expense[1]:.2f}")
            total += expense[1]

        print(f"Total spent: ${total:.2f}")

    elif choice == "3":
        break

    else:
        print("Invalid option. Try again.")