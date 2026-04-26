from data import storage

def check_balance():
    print(f"Current Balance: ₹{storage.balance}")

def deposit():
    amount = float(input("Enter amount to deposit: ₹"))
    storage.balance += amount
    storage.transactions.append(f"Deposited ₹{amount}")
    print("Deposit successful!")

def withdraw():
    amount = float(input("Enter amount to withdraw: ₹"))
    
    if amount <= storage.balance:
        storage.balance -= amount
        storage.transactions.append(f"Withdrew ₹{amount}")
        print("Withdrawal successful!")
    else:
        print("Insufficient balance!")

def show_transactions():
    print("\n--- Transaction History ---")
    if not storage.transactions:
        print("No transactions yet.")
    else:
        for t in storage.transactions:
            print(t)