#del keyword
# abstraction using bank account
class Account:
    def __init__(self,balance,accno):
        self.balance=balance
        self.accno=accno
    def debit(self,amt):
        prev_balance=self.balance
        self.balance = self.balance - amt
        return f"the balance is {prev_balance} and the amount is {amt} after debiting is {self.balance }"
    def credit (self,amt):
        prev_balance=self.balance
        self.balance = self.balance + amt
        return f"the balance is {prev_balance} and the amount is {amt} after crediting is {self.balance}"
    def baleq(self):
        return f"your balance is {self.balance}"

b1=Account(5000,1234)
print(b1.credit(2500))
print(b1.debit(1000))
print(b1.baleq())
#del b1
#this is used to del an instance can be used also for del Account class
print(b1.baleq())


#dunder methods examples

a=10
b=20
print(a.__add__(b))
print(a.__sub__(b))
print(a.__gt__(b))