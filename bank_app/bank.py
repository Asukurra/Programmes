class Account:

    def __init__(self, filepath):
        self.path=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def test(self,int):
        return int + 1

    def withdraw(self,amount):
        self.balance=self.balance - amount
        
    def deposit(self,amount):
        self.balance = self.balance + amount

    def commit (self):
        with open(self.path, 'w') as file:
            file.write(str(self.balance))

    


# account=Account("MegaC folder/Programmes/bank_app/balance.txt")

# print(account.balance)
# print(account.test(1))
# account.withdraw(100)
# account.commit()
# print(account.balance)


class Checking(Account):
    """
    This class generats check account objects
    """

    type = "checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self,amount):
        self.balance=self.balance - amount - self.fee

        
jack_checking=Checking("MegaC folder/Programmes/bank_app/jack.txt", 1)
jack_checking.deposit(10)
jack_checking.deposit(20)
jack_checking.transfer(10)
jack_checking.commit()

john_checking=Checking("MegaC folder/Programmes/bank_app/john.txt", 1)
john_checking.deposit(10)
john_checking.deposit(20)
john_checking.transfer(10)
john_checking.commit()