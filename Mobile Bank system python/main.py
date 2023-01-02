
import random
class Customer:
    accnumber = 554499
    def __init__(self, name, initialdeposit, passwd):
        self.name = name
        self.balance = initialdeposit
        self.passwd = passwd
        self.accnumber = random.randint(1540,100000)

    def getname(self):
        return self.name

    def changename(self, newname):
        self.name = newname

    def setpasswd(self, newpasswd):
        self.passwd = newpasswd

    def showBalance(self):
        return self.balance

    def withdraw(self,amount):
        self.balance -= amount

    def add(self,amount):
        self.balance += amount

    def printcust(self):
        print(f"Name: {self.name}\n Account no: {self.accnumber} Balance: {self.balance}\n")









class BankingSystem:
    Customers = []

    def createAccount(self, name, deposit, passwd):
        self.Customers.append(Customer(name, deposit, passwd))
        return self.Customers[-1].printcust()

    def addBalance(self,AccountNo,amount):
        for x in self.Customers:
            if (x.getaccountno() == AccountNo):
                x.add(amount)
    def checkBalance(self, accountno):
        for x in self.Customers:
            if (x.getaccountno() == accountno):
                print(x.showBalance())

    def withdraw(self,AccountNo,amount):
        for x in self.Customers:
            if (x.getaccountno() == AccountNo):
                x.withdraw(amount)

    def printcust(self):
        for cust in self.Customers:
            cust.printcust()



class BankingSystemInterface:
    bank = BankingSystem()
    bank.createAccount("Tahshin",500,'ihfaz')
    bank.createAccount("Shahriar",900, 'iffuu')




