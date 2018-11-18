class Account:
    def __init__(self,id=0,balance=100.0,annualInterestRate=0.0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def getMonthlyInterestRate(self):
        return self.getAnnualInterestRate() / (12 * 100)

    def getMonthlyInterest(self):
        return self.__balance * self.getMonthlyInterestRate()

    def withdraws(self,amount):
        self.__balance -= amount

    def deposits(self,amount):
        self.__balance += amount

a1 = Account(1122,20000,4.5)
a1.withdraws(2500)
a1.deposits(3000)
print('ID',a1.getId())
print('Balance',a1.getBalance())
print('Annual interest rate',a1.getAnnualInterestRate())
print('Monthly interest rate',a1.getMonthlyInterestRate())
print('Monthly interest : ',a1.getMonthlyInterest())
