class Account:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return True
        return False

    def transfer(self, target_account, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {target_account.user_id}")
            target_account.transaction_history.append(f"Received ${amount} from {self.user_id}")
            return True
        return False

    def display_transaction_history(self):
        print("\nTransaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def get_balance(self):
        return self.balance


def main():
    # Create two sample accounts
    account1 = Account("12345", "54321", 1000)
    account2 = Account("67890", "09876", 500)

    # User authentication
    user_id = input("Enter User ID: ")
    pin = input("Enter PIN: ")

    if user_id == account1.user_id and pin == account1.pin:
        current_account = account1
        print("Authentication successful. Welcome!")

        while True:
            print("\nATM Menu:")
            print("1. View Transaction History")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Transfer Money")
            print("5. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                current_account.display_transaction_history()
            elif choice == "2":
                amount = float(input("Enter withdrawal amount: $"))
                if current_account.withdraw(amount):
                    print(f"Withdrew ${amount}")
                else:
                    print("Invalid amount or insufficient balance.")
            elif choice == "3":
                amount = float(input("Enter deposit amount: $"))
                if current_account.deposit(amount):
                    print(f"Deposited ${amount}")
                else:
                    print("Invalid amount.")
            elif choice == "4":
                target_user_id = input("Enter target User ID for transfer: ")
                amount = float(input("Enter transfer amount: $"))
                if target_user_id == account2.user_id:
                    if current_account.transfer(account2, amount):
                        print(f"Transferred ${amount} to {account2.user_id}")
                    else:
                        print("Invalid amount or insufficient balance.")
                else:
                    print("Invalid target User ID.")
            elif choice == "5":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Authentication failed. Please try again.")

if __name__ == "__main__":
    main()