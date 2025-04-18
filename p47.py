# Write a Python program to create a class representing a bank.
# Include methods for managing customer accounts and transactions.

class Bank:
    def __init__(self):
        self.accounts = {}  # Dictionary to store customer accounts

    def create_account(self, customer_name, initial_balance=0):
        """Create a new account with an initial balance."""
        self.accounts[customer_name] = initial_balance
        print(f"Account for {customer_name} created with balance ${initial_balance}.")

    def deposit(self, customer_name, amount):
        """Deposit money into an existing account."""
        if customer_name in self.accounts:
            self.accounts[customer_name] += amount
            print(f"${amount} deposited into {customer_name}'s account.")
        else:
            print(f"Account for {customer_name} does not exist.")

    def check_balance(self, customer_name):
        """Check the balance of a customer's account."""
        if customer_name in self.accounts:
            print(f"{customer_name}'s balance: ${self.accounts[customer_name]}")
        else:
            print(f"Account for {customer_name} does not exist.")
# Example usage:
bank = Bank()
# Create account
bank.create_account("Alice", 100)
# Deposit money
bank.deposit("Alice", 50)
# Check balance
bank.check_balance("Alice")
