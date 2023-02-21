"""1"""
class smplstring(): 
    def __init__(self): 
        self.str1 = "" 
 
    def get_String(self): 
        self.str1 = input() 
 
    def print_String(self): 
        print(self.str1.upper()) 
 
 
str1 = smplstring() 
str1.get_String() 
str1.print_String()

"""2"""
class Shape(object): 
    def __init__(self): 
        pass 
 
    def area(self): 
        return 0 
 
 
class Square(Shape): 
    def __init__(self, l): 
        Shape.__init__(self) 
        self.length = l 
 
    def area(self): 
        return self.length * self.length 
 
 
aSquare = Square(3) 
print(aSquare.area())

"""3"""

class rec(): 
    def __init__(self, a, b): 
        self.a = a 
        self.b = b 
 
    def area(self): 
        return self.a * self.b 
 
 
ind1 = int(input()) 
ind2 = int(input()) 
rec = rec(ind1, ind2) 
print(rec.area())

"""4"""

import math 
 
class point(object): 
    def init(self, x, y): 
        self.x = x 
        self.y = y 
 
    def show(self): 
        return self.x, self.y 
 
    def move(self, x, y): 
        self.x += x 
        self.y += y 
 
    def dist(self, pt): 
        dx = pt.x - self.x 
        dy = pt.y - self.y

"""5"""
class Account: 
    def __init__(self, owner, balance=0): 
        self.owner = owner 
        self.balance = balance 
 
    def __str__(self): 
        return f'Account owner:   {self.owner}\nAccount balance:  ${self.balance}' 
 
    def deposit(self, dep_amt): 
        self.balance += dep_amt 
        print('Deposit Accepted') 
 
    def withdraw(self, wd_amt): 
        if self.balance >= wd_amt: 
            self.balance -= wd_amt 
            print('Withdrawal Accepted') 
        else: 
            print('Funds Unavailable!') 
        return Account(self.owner, self.balance) 
 
 
acct1 = Account(input(), int(input())) 
print(Account.withdraw(acct1, int(input()))) 
acct1.owner 
acct1.balance 
acct1.deposit(50) 
acct1.withdraw(75) 
acct1.withdraw(500)

"""6"""

print(list(filter(lambda x: x % 2 != 0 and x % 3 != 0 or x == 3 or x == 2, [1, 3, 2, 23, 61, 5, 20, 21])))