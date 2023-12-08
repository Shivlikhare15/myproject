from account_management.account import Account
from account_management.customer import Customer
from transaction_processing.transaction import Transaction
from transaction_processing.transaction_processor import TransactionProcessor

#create customers
customer1 = Customer("C001","Shiv Likhare")
customer2 = Customer("C002","Piyush Selode")

#create accounts
account1 = Account("A001",customer1)
account2 = Account("A002",customer2,balance=500.0)

#display initial balances
print(f"{customer1.name}'s Balance:{account1.get_balance()}")
print(f"{customer2.name}'s Balance:{account2.get_balance()}")

#perform transaction
transaction1 = Transaction("T001",account1,"deposit",1000.0)
transaction2 = Transaction("T002",account2,"withdraw",150.0)

TransactionProcessor.process_transaction(transaction1)
TransactionProcessor.process_transaction(transaction2)

#display update balances
print(f"{customer1.name}'s Update Balance:{account1.get_balance()}")
print(f"{customer2.name}'s Update Balance:{account2.get_balance()}")