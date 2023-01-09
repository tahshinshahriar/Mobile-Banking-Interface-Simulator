
import mysql.connector
import pickle
import random

connection = mysql.connector.connect(host='localhost',
                                     database='tshahriar',
                                     user='****',
                                     password='****')
cursor = connection.cursor()

class Customer:

    def __init__(self, name, initialdeposit, passwd):
        self.name = name
        self.balance = int(initialdeposit)
        self.passwd = passwd
        self.accnumber = random.randint(1540, 100000)

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

    def withdraww(self, amount):
        self.balance -= int(amount)

    def add(self, amount):
        self.balance += int(amount)

    def printcust(self):
        print(f"Name: {self.name}\nAccount no: {self.accnumber}\nBalance: {self.balance}\n")


class BankingSystem:


    def createAccount(self, name, deposit, passwd):
        x = Customer(name, deposit, passwd)
        pickledObject = pickle.dumps(x)
        sql = "INSERT INTO Users VALUES (%s, %s, %s, %s, %s)"
        val = (x.getaccountno(), x.getname(), x.getpasswd(), int(x.showBalance()), pickledObject)
        cursor.execute(sql, val)
        connection.commit()

    def getObject(self, accno):
        unpickle = ''
        sqli = ("SELECT User_object FROM Users WHERE Account_no = %s")
        cursor.execute(sqli, (accno,))
        rows = cursor.fetchall()
        for x in rows:
            for y in x:
                unpickle = (pickle.loads(y))
                print(unpickle)
        if (unpickle == ''):
            return False
        else:
            return unpickle



    def login(self, accno, passwd):
        code = 1
        msg = ''
        x = self.getObject(accno)
        if (type(x) == Customer):
            if (x.getpasswd() == passwd):
                print(f"Welcome {x.getname()}")
                code = 0
            else:
                msg = "Input the password correctly"
        else:
            msg = "Input the account no correctly"

        print(code)


        return code,msg

    def updatee(self, accno, userobj):
        sql = "UPDATE Users SET User_object = %s WHERE Account_no = %s"
        uobj = pickle.dumps(userobj)
        val = (uobj, accno)
        cursor.execute(sql, val)
        connection.commit()

    def addBalance(self, accountNo, amount):
        x = self.getObject(accountNo)
        x.add(amount)
        self.updatee(accountNo, x)

    def checkBalance(self, accountno):
        x = self.getObject(accountno)
        print(f"Your Balance is {x.showBalance()}")

    def withdraw(self,AccountNo,amount):
        x = self.getObject(AccountNo)
        x.withdraww(amount)
        self.updatee(AccountNo, x)
        msg = "Success! The new balance is " + str(x.showBalance())
        return msg

    def sendMoney(self, saccno, raccno, amount):
        self.addBalance(raccno,amount)
        return self.withdraw(saccno, amount)


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
            accno = int(input())
            print("Password: ", end='')
            passwd = input()
            lg = bank.login(accno, passwd)
            while (lg[0] == 1):
                print(lg[1])
                print("Account no: ", end="")
                accno = int(input())
                print("passwd: ", end='')
                passwd = input()
                lg = bank.login(accno, passwd)
            else:
                    inpp = 0
                    while (inpp != '5'):
                        print("Select from the following options: ")
                        print("1) Check Balance\n2) Withdraw Money\n3) Deposit Money\n4) Transfer Money\n5) Logout")
                        print("Enter 1 or 2 or 3 or 4 or 5")
                        print(">", end=' ')
                        inpp = input()
                        if (inpp == '1'):
                            bank.checkBalance(accno)
                        elif (inpp == '2'):
                            print("Enter the amount: ", end='')
                            amount = int(input())
                            bank.withdraw(accno, amount)
                        elif (inpp == '3'):
                            print("Enter the amount: ", end='')
                            amount = int(input())
                            bank.addBalance(accno, amount)
                        elif (inpp == '4'):
                            print("Enter the account no of the receiver: ", end='')
                            accountn = int(input())
                            print("Enter the amount: ", end='')
                            amount = int(input())
                            print(bank.sendMoney(accno, accountn, amount))
                        elif (inpp == '5'):
                            break
                        else:
                            print("Input the option correctly")


if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")



























