from services import atm_operations

def main():
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm_operations.check_balance()
        elif choice == "2":
            atm_operations.deposit()
        elif choice == "3":
            atm_operations.withdraw()
        elif choice == "4":
            atm_operations.show_transactions()
        elif choice == "5":
            print("Thank you for using ATM!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()