class BankAccount:
    def __init__(account, account_number, balance, owner_name):
        account.account_number = account_number
        account.balance = balance
        account.owner_name = owner_name
    
    def display_info(account_number):
        return(f"Account Number: {account_number.account_number}\n"
               f"Balance: {account_number.balance}\n"
               f"Owner Name: {account_number.owner_name}\n")