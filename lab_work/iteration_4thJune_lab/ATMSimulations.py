balance = 10000

for i in range(5):
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance = ₹", balance)
        break

    elif choice == 2:
        amount = float(input("Enter deposit amount: ₹"))
        balance += amount
        print("Amount Deposited Successfully!")
        break

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: ₹"))
        break

        if amount <= balance:
            balance -= amount
            print("Amount Withdrawn Successfully!")
            break
        else:
            print("Insufficient Balance!")
            break

    elif choice == 4:
        print("Thank You for Using ATM")
        break
