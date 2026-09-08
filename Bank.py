bank = []

while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. View All Accounts")
    print("3. Search Account")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Transfer Money")
    print("7. Delete Account")
    print("8. Show Richest Account")
    print("9. Save Data")
    print("10. Exit")

    choice = input("Enter your choice: ")

    # Create Account
    if choice == "1":
        name = input("Enter account holder name: ")
        account_number = input("Enter account number: ")
        balance = float(input("Enter initial balance: "))

        account = {
            "name": name,
            "account_number": account_number,
            "balance": balance
        }

        bank.append(account)
        print("Account created successfully!")

    # View All Accounts
    elif choice == "2":
        if len(bank) == 0:
            print("No accounts found!")
        else:
            print("\n===== ALL ACCOUNTS =====")

            for account in bank:
                print(f"Account Name: {account['name']}")
                print(f"Account Number: {account['account_number']}")
                print(f"Account Balance: {account['balance']}")
                print("-----------------------")

    # Search Account
    elif choice == "3":
        account_number = input("Enter account number: ")
        found = False

        for account in bank:
            if account_number == account["account_number"]:
                print("\nAccount Found!")
                print(f"Account Name: {account['name']}")
                print(f"Account Number: {account['account_number']}")
                print(f"Account Balance: {account['balance']}")

                found = True
                break

        if not found:
            print("Account not found!")

    # Deposit Money
    elif choice == "4":
        account_number = input("Enter your account number: ")
        found = False

        for account in bank:
            if account_number == account["account_number"]:
                amount = float(input("Enter deposit amount: "))

                if amount > 0:
                    account["balance"] += amount
                    print("Money deposited successfully!")
                    print(f"New balance: {account['balance']}")
                else:
                    print("Invalid amount!")

                found = True
                break

        if not found:
            print("Account not found!")

    # Withdraw Money
    elif choice == "5":
        account_number = input("Enter account number: ")
        found = False

        for account in bank:
            if account_number == account["account_number"]:
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    print("Invalid amount!")
                elif amount > account["balance"]:
                    print("Insufficient balance!")
                else:
                    account["balance"] -= amount
                    print("Money withdrawn successfully!")
                    print(f"New balance: {account['balance']}")

                found = True
                break

        if not found:
            print("Account not found!")

    # Transfer Money
    elif choice == "6":
        sender_number = input("Enter sender account number: ")
        receiver_number = input("Enter receiver account number: ")

        sender = None
        receiver = None

        for account in bank:
            if account["account_number"] == sender_number:
                sender = account

            if account["account_number"] == receiver_number:
                receiver = account

        if sender is None:
            print("Sender account not found!")

        elif receiver is None:
            print("Receiver account not found!")

        elif sender_number == receiver_number:
            print("You cannot transfer money to the same account!")

        else:
            amount = float(input("Enter transfer amount: "))

            if amount <= 0:
                print("Invalid amount!")

            elif amount > sender["balance"]:
                print("Insufficient balance!")

            else:
                sender["balance"] -= amount
                receiver["balance"] += amount

                print("Money transferred successfully!")
                print(f"Sender new balance: {sender['balance']}")
                print(f"Receiver new balance: {receiver['balance']}")

    # Delete Account
    elif choice == "7":
        delete = input("Enter account number to delete: ")
        found = False

        for account in bank:
            if delete == account["account_number"]:
                bank.remove(account)
                print("Account delete successful!")

                found = True
                break

        if not found:
            print("No account found!")

    # Show Richest Account
    elif choice == "8":
        if len(bank) == 0:
            print("Account not found!")

        else:
            richest = bank[0]

            for account in bank:
                if account["balance"] > richest["balance"]:
                    richest = account

            print("\n===== RICHEST ACCOUNT =====")
            print(f"Account Name: {richest['name']}")
            print(f"Account Number: {richest['account_number']}")
            print(f"Account Balance: {richest['balance']}")

    # Save Data
    elif choice == "9":
        with open("bank.txt", "w") as file:
            for account in bank:
                file.write(f"Name: {account['name']}\n")
                file.write(f"Account Number: {account['account_number']}\n")
                file.write(f"Account Balance: {account['balance']}\n")
                file.write("-----------------------\n")

        print("Data saved successfully!")

    # Exit
    elif choice == "10":
        print("Thank you for using Bank Management System!")
        break

    else:
        print("Invalid choice!")