
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
    def getaccountno(self):
        return self.accnumber

    def setpasswd(self, newpasswd):
        self.passwd = newpasswd
    def getpasswd(self):
        return self.passwd

    def showBalance(self):
        return self.balance

    def withdraw(self,amount):
        self.balance -= amount

    def add(self,amount):
        self.balance += amount

    def printcust(self):
        print(f"Name: {self.name}\nAccount no: {self.accnumber}\nBalance: {self.balance}\n")


class BankingSystem:
    Customers = []

    def createAccount(self, name, deposit, passwd):
        self.Customers.append(Customer(name, deposit, passwd))
        return self.Customers[-1].printcust()
    def login(self, accno, passwd):
        for x in self.Customers:
            if (x.getaccountno() == accno and x.getpasswd() == passwd ):
                print(f"Welcome {x.getname}")
                return 0
            elif (x.getaccountno == accno and x.getpasswd != passwd):
                print("Enter the password correctly")
                return 1
            elif (x.getaccountno != accno and x.getpasswd == passwd):
                print("Enter the account no correctly")
                return 1
            else:
                print("Enter password and account number correctly")
                return 1


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
    def sendMoney(self, saccno, raccno, amount):
        for x in self.Customers:
            x.withdraw(saccno,amount)
        for y in self.Customers:
            y.addBalance(raccno, amount)



    def printcust(self):
        for cust in self.Customers:
            cust.printcust()



class BankingSystemInterface:
    bank = BankingSystem()
    print("Welcome to X Bank\nPlease choose from the following options")
    inp = 0
    while (inp != '3'):
        print("1) Create Account\n2)Log into my account\n3) Quit")
        print("Enter 1 or 2 or 3")
        print(">", end=' ')
        inp = input()
        if (inp == ""):
            print("\n>")
        elif (inp == "1"):
            print("Name: ", end=' ')
            name = input()
            print("Password: ", end=' ')
            passwdd = input()
            print("Initial Deposit: ", end=' ')
            initialDeposit = input()
            bank.createAccount(name, initialDeposit, passwdd)
        elif (inp == "2"):
            print("Account no: ", end="")
            accno = input()
            print("passwd: ", end=' ')
            passwd = input()
            lg = bank.login(accno, passwd)
            print(lg)
            while (lg == 1):
                print("Account no: ", end="")
                accno = input()
                print("passwd: ", end=' ')
                passwd = input()
                bank.login(accno, passwd)
            else:
                print("Select from the following options: ")
                print("1) Check Balance\n2) Withdraw Money\n3) Deposit Money\n 4) Transfer Money")
                print("Enter 1 or 2")
                print(">", end=' ')
                inpp = input()
                if (inpp == '1'):
                    bank.checkBalance(accno)
                elif (inpp == '2'):
                    print("Enter the amount: ", end='')
                    amount = input()
                    bank.withdraw(accno, amount)
                elif (inpp == '3'):
                    print("Enter the amount: ", end='')
                    amount = input()
                    bank.addBalance(accno, amount)
                elif (inpp == '4'):
                    print("Enter the account no of the receiver", end='')
                    accountn = input()
                    print("Enter the amount", end ="")
                    amount = input()
                    bank.sendMoney(accno, accountn, amount)
























