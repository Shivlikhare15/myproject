from.transaction import Transaction
class TransactionProcessor:
    @staticmethod
    def process_transaction(transaction):
        if transaction.transaction_type == "deposit":
            transaction.account.deposit(transaction.amount)
        elif transaction.transaction_type == "withdraw":
            transaction.account.withdraw(transaction.amount)
        else:
            print("Invalid transaction type.")    