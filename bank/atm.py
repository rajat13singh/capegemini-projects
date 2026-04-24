# Initial account data
account = {
    "balance": 1000,
    "transactions": []
}

def show_balance():
    print("Current Balance:", account["balance"])

def deposit():
    amount = int(input("Enter amount to deposit: "))
    account["balance"] += amount
    account["transactions"].append(f"Deposited ₹{amount}")
    print("Amount deposited successfully")

def withdraw():
    amount = int(input("Enter amount to withdraw: "))
    if amount <= account["balance"]:
        account["balance"] -= amount
        account["transactions"].append(f"Withdrew ₹{amount}")
        print("Please collect your cash")
    else:
        print("Insufficient balance")

def statement():
    print("\n--- Transaction Statement ---")
    if not account["transactions"]:
        print("No transactions yet")
    else:
        for t in account["transactions"]:
            print(t)
    print("----------------------------")

# Menu
while True:
    print("\n--- ATM Menu ---")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Statement")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        show_balance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        statement()
    elif choice == 5:
        print("Thank you for using ATM")
        break
    else:
        print("Invalid choice")