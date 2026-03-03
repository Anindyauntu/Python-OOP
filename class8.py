# Topic: Encapsulation

# Topic: Encapsulation - Protecting data(main)
# Example: 
# - vending machine - restricting direct access to inventory/cokes/sodas
# - bank account - restricting direct access to balance

class BankAccount():
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance #private attribute
        
        
    def deposit(self, amount):
        if amount > 0 :
            self.__balance = self.__balance + amount
            print(f"Deposit Amount:{amount}")
            
        else:
            print("Deposit amount must be greater than 0")
            
            
    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance = self.__balance - amount
            print(f"Withdraw Amount: {amount}")
            
        else:
            print("Insufficient Balance or invalid amount ...")
            
#greater method to unlock or access private data ...

    def get_balance(self):
        print(f"Your balance is {self.__balance} tk ...")

        
    