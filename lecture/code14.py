def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount>balance:
            return 'NOT SUFFICIENT FUNDS '
        else:
            balance=balance-amount
        return balance
    return withdraw