def make_withdraw(balance):
    b=[balance]
    def withdraw(amount):
        if amount>balance:
            return 'NOT SUFFICIENT FUNDS'
        else:
            b[0]=b[0]-amount
        return b[0]
    return withdraw