def acc_transfer(acc_from, acc_to, amount, checking_balance, saving_balance):
    transaction_status = ""
    trans_error = "unsuccessful, please enter amount less than "

    if acc_from == "savings" and acc_to == "checking":
        if amount < saving_balance:
            saving_balance -= amount
            checking_balance += amount
            transaction_status = "successful"
        else:
            transaction_status = f"{trans_error} {saving_balance}"
    elif acc_from == "cheking" and acc_to == "savings":
        if amount < checking_balance:
            checking_balance -= amount
            saving_balance += amount
            transaction_status = "successful"
        else:
            transaction_status = f"{trans_error} {checking_balance}"
    else:
        transaction_status = f'unsuccessful, please enter "checking" or "savings"'

    transaction_statement = f"Transfer of {amount} from you {acc_from} to your {acc_to} account was {transaction_status}"
    print(transaction_statement)
    return saving_balance, checking_balance
