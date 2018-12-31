class Creditcard:
    """A customer credit card"""

    def __init__(self, customer, bank, account, limit):
        """Instance of a credit card
        customer -> John Doe
        bank -> king's maker
        account -> account type
        limit -> credit limit
        """
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.balance = 0
        self.newAccount = None

    def getCustomer(self):
        return self.customer

    def getBank(self):
        return self.bank

    def getAccount(self):
        return self.account

    def getLimit(self):
        return self.limit

    def getBalance(self):
        return self.balance

    def getNewAccount(self):
        return self.newAccount

    def charge(self, price):
        """
        Charge given at the store/online to the card,
        assuming there is sufficient credit.
        Return True if charge can be processed.
        Otherwise, charge would be denied.
        """
        if not isinstance(price, (int, float)):
            raise ValueError('It is a number')
        elif price < 0:
            raise ValueError('Price is always positive')
        if price + self.balance > self.limit:
            return False
        else:
            self.balance += price
            return True

    def makePayment(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError('It is a positive number')
        elif amount < 0:
            raise ValueError('Amount is always positive')
        self.balance -= amount

    def printBalance(self):
        print('Balance is ' + str(self.balance))

cc = Creditcard('John Doe', 'king\'s maker', '10000 5452 664534', 1000)
print('Customer -> ', cc.getCustomer())
print('Bank -> ', cc.getBank())
print('Account -> ', cc.getAccount())
print('Limit -> ', cc.getLimit())
cc.charge(100)
print('balance -> ', cc.getBalance())
print('----------------------------------------------')
#cc.printBalance()

if __name__ == '__main__':
    wallet = []
    wallet.append(Creditcard('John Bowman', 'California Savings', '5345 4423 3323 0023', 2500))
    wallet.append(Creditcard('John Bowman', 'California Capitol', '5005 5423 3113 0023', 6000))
    wallet.append(Creditcard('John Bowman', 'California Bank', '6545 1023 3343 6523', 7500))

    for val in range(1,17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)


    for c in range(3):
        print('Customer -> ', wallet[c].getCustomer())
        print('Bank -> ', wallet[c].getBank())
        print('Account -> ', wallet[c].getAccount())
        print('Limit -> ', wallet[c].getLimit())
        print('Balance -> ', wallet[c].getBalance())
        print('-------------------------------------------------------')

        while wallet[c].getBalance() > 100:
            wallet[c].makePayment(100)
            print('New Balance ->', wallet[c].getBalance())
            print('---------------------------------------------------')
